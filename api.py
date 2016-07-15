__author__ = 'Renchen'
from modules import(
    Filters,
    Relationships,
)
from urllib import quote
from utility import Utility
BuildParams = Utility.BuildParams
BuildUrls = Utility.BuildUrls
MakeRequest = Utility.MakeRequest
PrettyPrintResult = Utility.PrettyPrintResult

class Api():
    def __init__(self,
                 appid,
                 select='long',
                 format='json',
                 lang='en-us'):
        self._base_url = 'http://where.yahooapis.com/v1/'
        self._appid = appid
        self._format = format
        self._select = select
        self._lang = lang

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

        relationships = Relationships(parent,
                                     ancestors,
                                     belongtos,
                                     neighbors,
                                     siblings,
                                     children,
                                     descendants,
                                     common)

        extra_parms = self.__BuildParams()

        url = BuildUrls(url=self._base_url,
                        path_elements=extra_paths,
                        extra_params=extra_parms,
                        extra_woeid=None if type(woeid) is int else woeid[1:],
                        filters=filters,
                        relationships=relationships)
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

        extra_params = self.__BuildParams()

        url = BuildUrls(url=self._base_url,
                        path_elements=extra_paths,
                        extra_params=extra_params,
                        filters=filters,
                        count=count)
        return MakeRequest(url)

    def __BuildParams(self):
        return BuildParams(self._appid,
                           format=self._format,
                           select=self._select,
                           lang=self._lang)

    def __GetHelper(self,
                    path=None,
                    place=None,
                    filters=None):
        extra_paths = [path] if type(path) is not list else path

        if type(place) is str and place:
            extra_paths.append(quote(place))

        extra_params = self.__BuildParams()

        url = BuildUrls(url=self._base_url,
                        path_elements=extra_paths,
                        extra_params=extra_params,
                        filters=filters)
        return MakeRequest(url)

    def GetContinents(self):
        return self.__GetHelper('continents')

    def GetOceans(self):
        return self.__GetHelper('oceans')

    def GetSeas(self,
                place=None):
        return self.__GetHelper('seas', place=place)

    def GetCountries(self,
                     place=None):
        return self.__GetHelper('countries', place=place)

    def GetStates(self,
                  country=None):
        return self.__GetHelper('states', place=country)

    def GetCounties(self,
                    state=None):
        return self.__GetHelper('counties', place=state)

    def GetDistricts(self,
                     county=None):
        return self.__GetHelper('districts', place=county)

    def GetConcordance(self,
                       namespace,
                       id):
        paths = ['concordance', namespace, id]
        return self.__GetHelper(paths)

    def GetPlacetypes(self,
                      country=None,
                      typ=None):
        filters = Filters(typ=typ)
        paths = ['placetypes']
        paths.append(country)
        return self.__GetHelper(path=paths,filters=filters)

    def GetPlacetype(self,
                     typ,
                     country):
        paths = ['placetype']
        typ = str(typ)
        country = str(country)
        paths.append(typ)
        paths.append(country)
        return self.__GetHelper(path=paths)

