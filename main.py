__author__ = 'Renchen'
import config
from requests_oauthlib import OAuth1
import requests
import json
import urllib
import urlparse
import error


auth = OAuth1(config.key, config.secret)
base_url = 'http://where.yahooapis.com/v1/'

def ConstructParams(appid,
                    format='json',
                    select='short'):
    return {
        'format':format
        ,'appid':appid
        ,'select':select
    }

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


def FiltersToStr(filters):
    qstr = ''
    woeidstr = ''

    if 'q' in filters.keys():
        qstr_tmp = ''
        if type(filters['q']) is str:
            qstr_tmp = filters['q']
        elif type(filters['q']) is tuple:
            # Second item will be a focus value
            # Focus can be either an ISO-3166-1 country code or a WOEID.
            qstr_tmp += urllib.quote(filters['q'][0]) + ',' + urllib.quote(filters['q'][1])
        else:
            raise error.WoeidError("Unexpected usage of function! query filter is %s"%filters['q'])

        qstr = qstr_tmp


    if 'woeid' in filters.keys():
        woeidstr_tmp = ''
        if type(filters['woeid']) is list and len(filters['woeid']) > 1:
            for item in filters['woeid']:
                woeidstr_tmp += urllib.quote(item) + ','
            # tick out the last comma
            woeidstr_tmp = woeidstr_tmp[:-1]
        elif type(filters['woeid']) is list and len(filters['woeid']) == 1:
            woeidstr_tmp = urllib.quote(filters['woeid'][0])
        else:
            raise error.WoeidError("Unexpected usage of function! query filter is %s"%filters['woeid'])
        woeidstr = woeidstr_tmp

    if len(qstr):
        #.q can be omitted if it's not a tuple
        return '.q(%s)'%qstr if ',' in qstr else qstr
    elif len(woeidstr):
        #.woeid can be omitted if there is only one item
        return '.woeid(%s)'%woeidstr if ',' in woeidstr else woeidstr
    else:
        return ''


def BuildUrls(url,
              path_elements=None,
              extra_params=None,
              filters=None,
              familyselectors=None):
    (scheme, netloc, path, params, query, fragment) = urlparse.urlparse(url)

    # Add any additional path elements to the path
    if path_elements:
        # Filter out the path elements that have a value of None
        p = [i for i in path_elements if i]
        if not path.endswith('/'):
            path += '/'
        path += '/'.join(p)

    # Add any additional query parameters to the query string
    if extra_params and len(extra_params) > 0:
        extra_query = EncodeParameters(extra_params)
        # Add it to the existing query
        if query:
            query += '&' + extra_query
        else:
            query = extra_query

    if len(filters.keys()):
        filterstr = FiltersToStr(filters)
        path += filterstr

    if familyselectors and isinstance(familyselectors, FamilySelectors):


    # Return the rebuilt URL
    return urlparse.urlunparse((scheme, netloc, path, params, query, fragment))


def BuildFilters(q=None,
                 woeid=None,
                 typ=None,
                 degree=None,
                 nd=None):
    filters = {}

    # q and woeid are mutually exclusive
    if q and type(q) is str or type(q) is tuple:
        filters['q'] = q
    elif woeid and type(woeid) is list:
        # Make sure the values are str
        filters['woeid'] = [str(val) for val in woeid if type(val) is int]

    if typ and type(typ) is list or type(typ) is int:
        filters['type'] = typ

    if degree and type(degree) is int:
        filter['degree'] = degree

    if nd and type(nd) is bool:
        filter['and'] = nd

    return filters


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


class FamilySelectors:
    def __init__(self,
                 parent=False,
              ancestors=False,
              belongstos=False,
              neighbors=False,
              siblings=False,
              children=False,
              descendants=False):
        self._parent=parent
        self._ancestor=ancestors
        self._belongtos=belongstos
        self._neighbors=neighbors
        self._siblings=siblings
        self._children=children
        self._descrendants=descendants


def GetPlaces(appid,
              q=None,
              woeid=None,
              typ=None,
              degree=None,
              nd=None,
              familyselectors=None,
              select='short',
              format='json'):
    extra_paths = ['places']
    extra_params = ConstructParams(appid,format=format,select=select)
    filter = BuildFilters(q,woeid,typ,degree,nd)
    url = BuildUrls(base_url, extra_paths, extra_params, filter)
    return MakeRequest(url)


def PrettyPrintResult(jsonstr):
    print(json.dumps(jsonstr, indent=4, separators={',', ': '}))


def main(args=None):
    PrettyPrintResult(GetPlaces(config.key, woeid=[2507854, 12521721, 638242]))
    #print(json.dumps(GetWoeid("China"), indent=4, separators={',', ': '}))

if __name__ == "__main__":
    main()