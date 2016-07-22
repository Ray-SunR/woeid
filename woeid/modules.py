try:
	from urllib import quote
except ImportError as e:
	from urllib.parse import quote
from woeid import WoeidError
from six import string_types

__author__ = 'Renchen'

class Filters:
	"""A class that encapsulates all filters
		Args:
			q(``str`` or ``tuple``, optional):
				Specify a place name to search for or a tuple that has a place name and a focus. This filter is mutually exclusive with the `woeid` filter. The specified place can be any unicode characters. Focus can be either an ISO-3166-1 country code or a WOEID. For a "startswith" filter, specify the place as a string followed by an asterisk (*).
			woeid(``list``(``str``) or ``list``(``int``), optional):
				Specify a `Where On Earth Identifier` (`woeid`). Up to ten WOEIDs may be specified. This filter is mutually exclusive with the `q` filter. Example: woeid=(1,2,3)
			typ(``list``(``str``) or ``list``(``int``) or ``int``, optional):
				Specify one or more place type codes (https://developer.yahoo.com/geo/geoplanet/guide/concepts.html#placetypes). Up to ten place type codes or names may be provided.
			degree(``int`` or ``str``, optional):
				`.degree` specifier which represents the degree to which two places are neighborhoods. Only consider valid if either `neighbors` or `children` filters are set.
			nd(``boolean``, optional):
				Specify a join operations on two filters. Example:

				 >>> import woeid
				 >>> api = woeid.Api(client_id='YOUR_CLIENT_ID')
				 >>> ret = api.GetPlaces(q='StringField', typ=22, nd=True)

		"""
	def __init__(self,
				 q=None,
				 woeid=None,
				 typ=None,
				 degree=None,
				 aand=None):
		filters = {}

		# q and woeid are mutually exclusive
		if isinstance(q, string_types) or isinstance(q, tuple):
			filters['q'] = q
		elif woeid and isinstance(woeid, list):
			# Make sure the values are str
			filters['woeid'] = [str(val) for val in woeid if isinstance(val, int) or isinstance(val, string_types)]

		if typ and isinstance(typ, list) or isinstance(typ, int):
			filters['type'] = typ

		if degree and isinstance(degree, int):
			filters['degree'] = degree

		if aand and isinstance(aand, bool):
			filters['and'] = aand
		self._filters = filters


	def HasQ(self):
		"""Return if the filter object has `.q` filter.
		"""
		return 'q' in self._filters

	def HasWoeid(self):
		"""Return if the filter object has `.woeid` filter.
		"""
		return 'woeid' in self._filters

	def HasType(self):
		"""Return if the filter object has `.type` filter
		"""
		return 'type' in self._filters

	def HasDegree(self):
		"""Return if the filter object has `.degree` filter
		"""
		return 'degree' in self._filters

	def HasAnd(self):
		"""Return if the filter object has `$and` filter
		"""
		return 'and' in self._filters

	def IsValid(self):
		return isinstance(self._filters, dict)

	def __str__(self):
		qstr = ''
		woeidstr = ''
		typestr = ''
		degreestr = ''
		andstr = ''
		# work on .q filter
		if self.HasQ():
			if isinstance(self._filters['q'], string_types):
				qstr = quote(self._filters['q'].encode('utf-8'))
			elif isinstance(self._filters['q'], tuple):
				stra = self._filters['q'][0].encode('utf-8')
				strb = self._filters['q'][1].encode('utf-8')
				# Second item will be a focus value
				# Focus can be either an ISO-3166-1 country code or a WOEID.
				qstr += quote(stra + ',' + strb)
			else:
				raise WoeidError("Unexpected usage of function! query filter is %s" % self._filters['q'])
			qstr = '.q(%s)'%qstr

		# work on .woeid filter
		if self.HasWoeid():
			if isinstance(self._filters['woeid'], list) and len(self._filters[
			'woeid']) > 1:
				for item in self._filters['woeid']:
					if (isinstance(item, string_types) and item.isdigit()) or isinstance(item, int):
						woeidstr += quote(item) + ','
				# tick out the last comma
				woeidstr = woeidstr[:-1]
			elif isinstance(self._filters['woeid'], list) and len(
					self._filters['woeid']) == 1:
				woeidstr = '/' + quote(self._filters['woeid'][0])
			else:
				raise WoeidError("Unexpected usage of function! query filter is %s"%self._filters['woeid'])
			#.woeid can be omitted if there is only one item
			if ',' in woeidstr:
				woeidstr = '.woeid(%s)'%woeidstr

		# work on .type filter
		if 'type' in self._filters:
			tpitem = self._filters['type']
			if isinstance(tpitem, list):
				for item in tpitem:
					if (isinstance(item, string_types) and item.isdigit()) or isinstance(item, int):
						typestr += quote(str(item)) + ','
				typestr = typestr[:-1]
				typestr = '.type(%s)'%typestr
			elif (type(tpitem) is str and tpitem.isdigit()) or isinstance(tpitem, int):
				typestr = '.type(%s)'%quote(str(tpitem))

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

		if andstr:
			return andstr


		query_or_woeid_str = qstr if qstr else woeidstr

		return query_or_woeid_str + typestr + degreestr


class Relationships:
	""""A class that encapsulates all relationships

		Args:
			parent(``boolean``, optional):
				A relationship specifier used to return a parent place of a given woeid.
			ancestors(``boolean``, optional):
				A relationship specifier used to return one or more acestors of a place of a given woeid.
			belongtos(``boolean``, optional):
				A relationship specifier used to return a collection of places that have a place as a child or descendant (child of a child).
			neighbors(``boolean``, optional):
				A relationship specifier used to return a collection of places that neighbor of a place.
			children(``boolean``, optional):
				A relationship specifier used to return a collection of places that are children of a place.
			siblings(``boolean``, optional):
				A relationship specifier used to return a collection of places that are siblings of a place.
			descendants(``boolean``, optional):
				A relationship specifier used to return a collection of places that are in the child hierarchy (the child, the child of child, etc).
			common(``boolean``, optional):
				A relationship specifier used to return the common ancestor of both places.
		"""
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

	def __Validate(self, filters):
		if isinstance(filters, Filters):
			raise WoeidError("Unexpected modules usage: %s"%"Validate takes a Filters object as its argument")

		if not filters.IsValid():
			raise WoeidError("Unexpected API usage: %s"%"filters should be a dictionary")

		''' /parent, /ancestors, /siblings, /common/ don't support any filters'''
		if self._parent and filters.keys():
			raise WoeidError("Unexpected API usage: %s"%"woeid/parent doesn't support filters")

		if self._ancestors and filters.keys():
			raise WoeidError("Unexpected API usage: %s"%"woeid/ancestors doesn't support filters")

		if self._siblings and filters.keys():
			raise WoeidError("Unexpected API usage: %s"%"woeid/siblings doesn't support filters")

		if self._common and filters.keys():
			raise WoeidError("Unexpected API usage: %s"%"woeid1/common/woeid2 doesn't support filters")

		'''/belongtos and /descendants and /children support .type filter'''
		if self._belongtos and (filters.HasAnd() or filters.HasDegree() or filters.HasQ() or filters.HasWoeid()):
			raise WoeidError("Unexpected API usage: %s"%"woeid/belongtos supports .type filter only")

		if self._descendants and (filters.HasAnd() or filters.HasDegree() or filters.HasQ() or filters.HasWoeid()):
			raise WoeidError("Unexpected API usage: %s"%"woeid/descendants supports .type filter only")

		if self._children and (filters.HasWoeid() or filters.HasQ() or filters.HasAnd()):
			raise WoeidError("Unexpected API usage: %s"%"woeid/children supports .degree or .type filters only")

		'''/neighbors support .degree filter'''
		if self._neighbors and (filters.HasWoeid() or filters.HasType() or filters.HasQ() or filters.HasAnd()):
			raise WoeidError("Unexpected API usage: %s"%"woeid/neighbors supports .degree filter only")







