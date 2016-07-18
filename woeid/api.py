
#!/usr/bin/env python

#
#
# Copyright 2016 Renchen Sun.
#
# Licensed under the The MIT License (MIT) Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A library that provides a Python interface to the Yahoo GeoPlanet API"""

from woeid import (WoeidError, Filters, Relationships, MakeRequest, BuildParams, BuildUrls)
from urllib import quote

class Api(object):
    """A python interface into the Woeid API
     Example usage:
         To create an instance of the woeid.Api class

         >>> import woeid
         >>> api = woeid.Api(appid='YOUR_APPID')

         To retrie the Most Likely Place for a Given Place Name, eg SFO'
        places = api.GetPlaces(q='SFO')
        print(places)
    """
    def __init__(self,
                 appid,
                 select='long',
                 format='json',
                 lang='en-us',
                 count=0,# a count of 0 means no maximum (all resources)
                 start=0):
        self.__base_url = 'http://where.yahooapis.com/v1/'
        self.__appid = appid
        self.__format = format
        self.__select = select
        self.__lang = lang
        self.__count = count
        self.__start = start

    @property
    def BaseUrl(self):
        return self.__base_url

    @BaseUrl.setter
    def BaseUrl(self, url):
        try:
            self.__base_url = str(url)
        except ValueError:
            raise WoeidError("Expect a string type for url")

    @property
    def AppId(self):
        return self.__appid

    @AppId.setter
    def AppId(self, appid):
        try:
            self.__appid = str(appid)
        except ValueError:
            raise WoeidError("Expect a string type for appid")

    @property
    def Format(self):
        return self.__format

    @Format.setter
    def Format(self, format):
        try:
            self.__format = str(format)
        except ValueError:
            raise WoeidError("Expect a string type for format")

    @property
    def Select(self):
        return self.__select

    @Select.setter
    def Select(self, select):
        try:
            if str(select).lower() == 'short' or str(select).lower() == 'long':
                self.__select = str(select)
            else:
                raise WoeidError("select can be either 'short' or 'long'")
        except ValueError:
            raise WoeidError("Expect a string type for select")

    @property
    def Lang(self):
        return self.__lang

    @Lang.setter
    def Lang(self, lang):
        try:
            self.__lang = str(lang)
        except ValueError:
            raise WoeidError("Expect a stirng type for lang")

    @property
    def Count(self):
        return self.__count

    @Count.setter
    def Count(self, count):
        try:
            self.__count = int(count)
        except ValueError:
            raise WoeidError("Expect an integer type for count")

    @property
    def Start(self):
        return self._Start

    @Start.setter
    def Start(self, start):
        try:
            self.__start = int(start)
        except ValueError:
            raise WoeidError("Expect an integer type for start")

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

        url = BuildUrls(url=self.__base_url,
                        path_elements=extra_paths,
                        extra_params=extra_parms,
                        extra_woeid=None if type(woeid) is int else woeid[1:],
                        filters=filters,
                        relationships=relationships,
                        count=self.__count,
                        start=self.__start)
        return MakeRequest(url)

    def GetPlaces(self,
                  q=None,
                  woeid=None,
                  typ=None,
                  nd=None):

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

        url = BuildUrls(url=self.__base_url,
                        path_elements=extra_paths,
                        extra_params=extra_params,
                        filters=filters,
                        count=self.__count,
                        start=self.__start)
        return MakeRequest(url)

    def __BuildParams(self):
        return BuildParams(self.__appid,
                           format=self.__format,
                           select=self.__select,
                           lang=self.__lang)

    def __GetHelper(self,
                    path=None,
                    place=None,
                    filters=None):
        extra_paths = [path] if type(path) is not list else path

        if type(place) is str and place:
            extra_paths.append(quote(place))

        extra_params = self.__BuildParams()

        url = BuildUrls(url=self.__base_url,
                        path_elements=extra_paths,
                        extra_params=extra_params,
                        filters=filters,
                        count=self.__start,
                        start=self.__start)
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

