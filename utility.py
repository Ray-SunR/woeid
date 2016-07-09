import json
import urllib
import requests
import error
from modules import FamilySelectors, Filters

__author__ = 'Renchen'
import urlparse
class Utility:
    @staticmethod
    def BuildUrls(url,
              path_elements,
              extra_params=None,
              filters=None,
              familyselectors=None):
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

        if filters and isinstance(filters, Filters) and filters.IsValid():
            path += str(filters)

        if familyselectors and isinstance(familyselectors, FamilySelectors):
            '''# only apply it if the query or woeid operator only has one target'''
            path += str(familyselectors)
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
                    select='short'):
        return {
            'format':format,
            'appid':appid,
            'select':select
        }

    @staticmethod
    def MakeRequest(url):
        print("Making requests on: %s"%url)
        ret = {}
        try:
            response = requests.get(url)
            if response.status_code != 200:
                raise error.WoeidError("Error on non-200 response code. Details: %s"%response.reason)
            else:
                ret = response.json()
        except:
            raise error.WoeidError("Unknown error occur")
        finally:
            return ret

    @staticmethod
    def PrettyPrintResult(jsonstr):
        print(json.dumps(jsonstr, indent=4, separators={',', ': '}))