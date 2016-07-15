import urllib
import error

__author__ = 'Renchen'

class Filters:
    def __init__(self,
                 q=None,
                 woeid=None,
                 typ=None,
                 degree=None,
                 aand=None):
        '''A user-end initializer for Filter class. Can take in a family selector object
        Args:
            q:
                The query target. Should be a string or a tuple. [Optional]
            woeid:
                The woeid list of ids. Should be a list. [Optional]

            typ:
            degree:
            aand:
            family_selector:

        '''
        filters = {}

         # q and woeid are mutually exclusive
        if q and type(q) is str or type(q) is tuple or type(q) is unicode:
            filters['q'] = q
        elif woeid and type(woeid) is list:
            # Make sure the values are str
            filters['woeid'] = [str(val) for val in woeid if type(val) is int or type(val) is str]

        if typ and type(typ) is list or type(typ) is int:
            filters['type'] = typ

        if degree and type(degree) is int:
            filters['degree'] = degree

        if aand and type(aand) is bool:
            filters['and'] = aand
        self._filters = filters


    def HasQ(self):
        return 'q' in self._filters

    def HasWoeid(self):
        return 'woeid' in self._filters

    def HasType(self):
        return 'type' in self._filters

    def HasDegree(self):
        return 'degree' in self._filters

    def HasAnd(self):
        return 'and' in self._filters

    def IsValid(self):
        return type(self._filters) is dict

    def __str__(self):
        qstr = ''
        woeidstr = ''
        typestr = ''
        degreestr = ''
        andstr = ''
        # work on .q filter
        if self.HasQ():
            if type(self._filters['q']) is str or type(self._filters['q'] is unicode):
                qstr = urllib.quote(self._filters['q'].encode('utf-8'))
            elif type(self._filters['q']) is tuple:
                stra = self._filters['q'][0].encode('utf-8')
                strb = self._filters['q'][1].encode('utf-8')
                # Second item will be a focus value
                # Focus can be either an ISO-3166-1 country code or a WOEID.
                qstr += urllib.quote(stra + ',' + strb)
            else:
                raise error.WoeidError("Unexpected usage of function! query filter is %s"%self._filters['q'])
            qstr = '.q(%s)'%qstr

        # work on .woeid filter
        if self.HasWoeid():
            if type(self._filters['woeid']) is list and len(self._filters['woeid']) > 1:
                for item in self._filters['woeid']:
                    if (type(item) is str and item.isdigit()) or type(item) is int:
                        woeidstr += urllib.quote(item) + ','
                # tick out the last comma
                woeidstr = woeidstr[:-1]
            elif type(self._filters['woeid']) is list and len(self._filters['woeid']) == 1:
                woeidstr = '/' + urllib.quote(self._filters['woeid'][0])
            else:
                raise error.WoeidError("Unexpected usage of function! query filter is %s"%self._filters['woeid'])
            #.woeid can be omitted if there is only one item
            if ',' in woeidstr:
                woeidstr = '.woeid(%s)'%woeidstr

        # work on .type filter
        if 'type' in self._filters:
            tpitem = self._filters['type']
            # TODO: add check for api type because `.type(list)` filter can only apply to /places resources
            if type(tpitem) is list:
                for item in tpitem:
                    if (type(item) is str and item.isdigit()) or type(item) is int:
                        typestr += urllib.quote(str(item)) + ','
                typestr = typestr[:-1]
                typestr = '.type(%s)'%typestr
            elif (type(tpitem) is str and tpitem.isdigit()) or type(tpitem) is int:
                typestr = '.type(%s)'%urllib.quote(str(tpitem))

        # work on .degree filter
        if 'degree' in self._filters:
            degree = str(self._filters['degree'])
            degreestr = '.degree(%s)'%degree

        # work on .and filter
        if 'and' in self._filters:
            conda = ''
            condb = ''
            if self.HasQ() and qstr:
                conda = qstr
            if self.HasWoeid() and woeidstr:
                conda = woeidstr

            if typestr:
                condb = typestr
            if degreestr:
                condb = degreestr

            if conda and condb:
                andstr = '$and(%s,%s)'%(conda,condb)

        # TODO: add check for api type because `$and` filter can only apply to /places resources
        if andstr:
            return andstr


        query_or_woeid_str = qstr if qstr else woeidstr

        return query_or_woeid_str + typestr + degreestr


class Relationships:
    def __init__(self,
                 parent=False,
                 ancestors=False,
                 belongstos=False,
                 neighbors=False,
                 siblings=False,
                 children=False,
                 descendants=False,
                 common=False):

        self._parent=parent
        self._ancestors=ancestors
        self._belongtos=belongstos
        self._neighbors=neighbors
        self._siblings=siblings
        self._children=children
        self._descendants=descendants
        self._common=common

    def __str__(self):
        if self._parent:
            return '/parent'

        if self._ancestors:
            return '/ancestors'

        if self._belongtos:
            return '/belongtos'

        if self._neighbors:
            return '/neighbors'

        if self._siblings:
            return '/siblings'

        if self._children:
            return '/children'

        if self._descendants:
            return '/descendants'

        if self._common:
            return '/common/'

        return ''

    def Validate(self, filters):
        if type(filters) is not Filters:
            raise error.WoeidError("Unexpected modules usage: %s"%"Validate takes a Filters object as its argument")

        if not filters.IsValid():
            raise error.WoeidError("Unexpected API usage: %s"%"filters should be a dictionary")

        ''' /parent, /ancestors, /siblings, /common/ don't support any filters'''
        if self._parent and filters.keys():
            raise error.WoeidError("Unexpected API usage: %s"%"woeid/parent doesn't support filters")

        if self._ancestors and filters.keys():
            raise error.WoeidError("Unexpected API usage: %s"%"woeid/ancestors doesn't support filters")

        if self._siblings and filters.keys():
            raise error.WoeidError("Unexpected API usage: %s"%"woeid/siblings doesn't support filters")

        if self._common and filters.keys():
            raise error.WoeidError("Unexpected API usage: %s"%"woeid1/common/woeid2 doesn't support filters")

        '''/belongtos and /descendants and /children support .type filter'''
        if self._belongtos and (filters.HasAnd() or filters.HasDegree() or filters.HasQ() or filters.HasWoeid()):
            raise error.WoeidError("Unexpected API usage: %s"%"woeid/belongtos supports .type filter only")

        if self._descendants and (filters.HasAnd() or filters.HasDegree() or filters.HasQ() or filters.HasWoeid()):
            raise error.WoeidError("Unexpected API usage: %s"%"woeid/descendants supports .type filter only")

        if self._children and (filters.HasWoeid() or filters.HasQ() or filters.HasAnd()):
            raise error.WoeidError("Unexpected API usage: %s"%"woeid/children supports .degree or .type filters only")

        '''/neighbors support .degree filter'''
        if self._neighbors and (filters.HasWoeid() or filters.HasType() or filters.HasQ() or filters.HasAnd()):
            raise error.WoeidError("Unexpected API usage: %s"%"woeid/neighbors supports .degree filter only")







