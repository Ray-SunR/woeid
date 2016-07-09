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
        if q and type(q) is str or type(q) is tuple:
            filters['q'] = q
        elif woeid and type(woeid) is list:
            # Make sure the values are str
            filters['woeid'] = [str(val) for val in woeid if type(val) is int]

        if typ and type(typ) is list or type(typ) is int:
            filters['type'] = typ

        if degree and type(degree) is int:
            filter['degree'] = degree

        if aand and type(aand) is bool:
            filter['and'] = aand
        self._filters = filters


    def IsQstrQuery(self):
        if 'q' in self._filters:
            return True
        else:
            return False

    def IsWoeidQuery(self):
        if 'woeid' in self._filters:
            return True
        else:
            return False

    def IsValid(self):
        if type(self._filters) is dict:
            return True
        else:
            return False

    def __str__(self):
        if self.IsQstrQuery():
            qstr = ''
            if type(self._filters['q'] is str):
                qstr = self.filters['q']
            elif type(self._filters['q']) is tuple:
                # Second item will be a focus value
                # Focus can be either an ISO-3166-1 country code or a WOEID.
                qstr += urllib.quote(self._filters['q'][0]) + ',' + urllib.quote(self._filters['q'][1])
            else:
                raise error.WoeidError("Unexpected usage of function! query filter is %s"%self._filters['q'])
            #.q can be omitted if it's not a tuple
            return '.q(%s)'%qstr if ',' in qstr else qstr

        if self.IsWoeidQuery():
            woeidstr = ''
            if type(self._filters['woeid']) is list and len(self._filters['woeid']) > 1:
                for item in self._filters['woeid']:
                    woeidstr += urllib.quote(item) + ','
                # tick out the last comma
                woeidstr = woeidstr[:-1]
            elif type(self._filters['woeid']) is list and len(self._filters['woeid']) == 1:
                woeidstr = urllib.quote(self._filters['woeid'][0])
            else:
                raise error.WoeidError("Unexpected usage of function! query filter is %s"%self._filters['woeid'])
            #.woeid can be omitted if there is only one item
            if ',' in woeidstr:
                return '.woeid(%s)'%woeidstr
            else:
                return woeidstr
        return ''


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

    def __str__(self):
        if self._parent:
            return '/'.join('parent')

        if self._ancestor:
            return '/'.join('ancestors')

        if self._belongtos:
            return '/'.join('belongtos')

        if self._neighbors:
            return '/'.join('neighbors')

        if self._siblings:
            return '/'.join('siblings')

        if self._children:
            return '/'.join('children')

        if self._descrendants:
            return '/'.join('descendants')

        return ''

