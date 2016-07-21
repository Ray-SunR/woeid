import json
import urllib
import requests
from woeid import (Relationships, Filters, WoeidError)
import xml.dom.minidom

__author__ = 'Renchen'
try:
	import urlparse
	from urllib import urlencode
except ImportError:
	import urllib.parse
	urlparse = urllib.parse
	from urllib.parse import urlencode


class ResponseCheck:
	"""A utility class reponsible for chekcing the reponse code and raise corresponding error

	Args:
		code(int):
			The response code in integer
	"""
	def __init__(self,
				 code):
		if code == 400:
			raise WoeidError("The appid parameter was invalid or not specified. or the q filter was missing or incorrectly specified for this resource.")

		if code == 404:
			raise WoeidError("The URI has no match in the display map")

		if code ==406:
			raise WoeidError("The requested representation is not available for this resource")

class Utility:
	@staticmethod
	def BuildUrls(url,
			  path_elements,
			  extra_params=None,
			  extra_woeid=None,
			  filters=None,
			  relationships=None,
			  count=None,
			  start=None):
		"""An utility class reponsible for building the url string

		Args:
			path_elements(list(str)):
				A list of paths that will be appended to the base url.
			extra_params(dict, optional):
				A dictionary representing the parameters for making the url.
			extra_woeid(list(int) or list(str), optional):
				This is useful when the `common` filter has been set. Aiming for making urls such as
				`1234/common/3456/73923`
			filters(Filters, optional):
				A `Filter` object
			relationships(Relationships, optional):
				A `Relationship` object
			count(int, optional):
				Specify the maximum number of results to return. A count of 0 is interpreted as `no maximum` (all resources)
			start(int, optional):
				Skip the first N results.
		Returns:
			A valid url containing all queries, filters, parameters.
		"""
		(scheme, netloc, path, params, query, fragment) = urlparse.urlparse(url)

		# Add any additional path elements to the path
		# Filter out the path elements that have a value of None
		p = [i for i in path_elements if i]
		if not path.endswith('/'):
			path += '/'
		path += '/'.join(p)

		# Add any additional query parameters to the query string
		if extra_params and len(extra_params) > 0:
			extra_query = Utility.EncodeParameters(extra_params)
			# Add it to the existing query
			if query:
				query += '&' + extra_query
			else:
				query = extra_query

		if relationships and isinstance(relationships, Relationships):
			path += str(relationships)

		if extra_woeid:
			for woeid in extra_woeid:
				path += str(woeid) + '/'
			path = path[:-1]

		if filters and isinstance(filters, Filters) and filters.IsValid():
			path += str(filters)

		if type(count) is int:
			path += ';count=%s'%str(count)

		if type(start) is int:
			path += ';start=%s'%str(start)
		# Return the rebuilt URL
		return urlparse.urlunparse((scheme, netloc, path, params, query, fragment))


	@staticmethod
	def EncodeParameters(parameters):
		"""Return a string in key=value&key=value form. Values of None are not included in the output string.

		Args:
			parameters (dict):
				dictionary of query parameters to be converted into a string for encoding and sending to Twitter.

		Returns:
			A URL-encoded string in "key=value&key=value" form
		"""
		if parameters is None:
			return None
		if not isinstance(parameters, dict):
			raise WoeidError("`parameters` must be a dict.")
		else:
			return urlencode(dict((k, v) for k, v in parameters.items() if v is not None))

	@staticmethod
	def BuildParams(appid,
					format='json',
					select='short',
					lang='en-us'):
		"""For constructing a parameter dictionary.
		"""
		return {
			'format':format,
			'appid':appid,
			'select':select,
			'lang':lang
		}

	@staticmethod
	def MakeRequest(url):
		print("Making requests on: %s"%url)
		ret = {}
		try:
			response = requests.get(url)
			ResponseCheck(response.status_code)
			ret = response.text.encode('ascii')
		except WoeidError as e:
			print(e.message)
			return ret
		return ret

	@staticmethod
	def PrettyPrintResult(retstr):
		if isinstance(retstr, bytes):
			retstr = retstr.decode()
		if not retstr:
			return
		try:
			print(json.dumps(json.loads(retstr), indent=4, separators={',' , ': '}, ensure_ascii=False))
		except TypeError as e:
			print(e)
		except ValueError as e:
			xxml = xml.dom.minidom.parseString(retstr)
			print(xxml.toprettyxml())
		finally:
			pass
