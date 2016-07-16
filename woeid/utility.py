import json
import urllib
import requests
import error
from modules import Relationships, Filters
import xml.dom.minidom
from xml.etree import ElementTree as ET

__author__ = 'Renchen'
import urlparse

class ResponseCheck:
    def __init__(self,
                 code):
        if code == 400:
            raise error.WoeidError("The appid parameter was invalid or not specified. or the q filter was missing or incorrectly specified for this resource.")

        if code == 404:
            raise error.WoeidError("The URI has no match in the display map")

        if code ==406:
            raise error.WoeidError("The requested representation is not available for this resource")

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
        """Return a string in key=value&key=value form.
        Values of None are not included in the output string.
        Args:
          parameters (dict): dictionary of query parameters to be converted into a
          string for encoding and sending to Twitter.
        Returns:
          A URL-encoded string in "key=value&key=value" form
        """
        if parameters is None:
            return None
        if not isinstance(parameters, dict):
            raise error.WoeidError("`parameters` must be a dict.")
        else:
            return urllib.urlencode(dict((k, v) for k, v in parameters.items() if v is not None))

    @staticmethod
    def BuildParams(appid,
                    format='json',
                    select='short',
                    lang='en-us'):
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
            check = ResponseCheck(response.status_code)
            ret = response.text
        except error.WoeidError as e:
            print(e.message)
            return ret
        return ret

    @staticmethod
    def PrettyPrintResult(str):
        if not str or (type(str) is not str and type(str) is not unicode):
            return
        str = str.encode('utf8')
        try:
            print(json.dumps(json.loads(str), indent=4, separators={',',': '}, ensure_ascii=False).encode('utf8'))
        except TypeError as e:
            pass
        except ValueError as e:
            xxml = xml.dom.minidom.parseString(str)
            print(xxml.toprettyxml())
        finally:
            pass
