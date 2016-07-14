import utility

__author__ = 'Renchen'
import config
from modules import(
    Filters,
    Selectors,
)
from utility import Utility
BuildParams = Utility.BuildParams
BuildUrls = Utility.BuildUrls
MakeRequest = Utility.MakeRequest
PrettyPrintResult = Utility.PrettyPrintResult

class Api():
    def __init__(self,
                 appid,
                 select='long',
                 format='json'):
        self._base_url = 'http://where.yahooapis.com/v1/'
        self._appid = appid
        self._format = format
        self._select = select

    def GetPlace(self,
                 woeid,
                 degree=None,
                 typ=None,
                 nd=None,
                 parent=False,
                 ancestors=False,
                 belongtos=False,
                 neighbors=False,
                 children=False,
                 siblings=False,
                 descendants=False,
                 common=False):
        if type(woeid) == int:
            extra_paths = ['place/' + str(woeid)]
        else:
            extra_paths = ['place/' + str(woeid[0])]

        filters = Filters(typ=typ,
                          degree=degree,
                          aand=nd)

        family_selectors = Selectors(parent,
                                     ancestors,
                                     belongtos,
                                     neighbors,
                                     siblings,
                                     children,
                                     descendants,
                                     common)

        extra_parms = BuildParams(appid=self._appid,
                                  format=self._format,
                                  select=self._select)

        url = BuildUrls(url=self._base_url,
                        path_elements=extra_paths,
                        extra_params=extra_parms,
                        extra_woeid=None if type(woeid) is int else woeid[1:],
                        filters=filters,
                        selectors=family_selectors)
        return MakeRequest(url)

    def GetPlaces(self,
                  q=None,
                  woeid=None,
                  typ=None,
                  nd=None,
                  count=None):

        '''
        Returns a collection of places that match a specified place name, and optionally, a specified place type. The resources in the collection are long representations of each place (unless short representations are explicitly requested).
        Supported Filters
            .q
            .type
            $and
            .woeid
        '''
        filters = Filters(q=q, woeid=woeid, typ=typ, aand=nd)
        extra_paths = ['places']

        extra_params = BuildParams(self._appid,
                                   format=self._format,
                                   select=self._select)

        url = BuildUrls(url=self._base_url,
                        path_elements=extra_paths,
                        extra_params=extra_params,
                        filters=filters,
                        count=count)
        return MakeRequest(url)
