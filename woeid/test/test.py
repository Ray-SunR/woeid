# -*- coding: utf-8 -*-
from __future__ import print_function
import woeid
from config import key
import unittest
try:
	import urlparse
	from urllib import urlencode
except ImportError:
	import urllib.parse
	urlparse = urllib.parse
	from urllib.parse import urlencode

class WoeidUnitTests(unittest.TestCase):

	def setUp(self):
		self.__api = woeid.Api(client_id=key, select='long', format='xml')
		self.__api.Lang = 'zh-hans-CN'
		self.__api.Select = 'short'
		self.__api.Format = 'json'
		self.__api.Count = 5

	def test_all(self):

		'''Example 8. Retrieving the Most Likely Place for a Given Place Name'''
		self.__api.GetPlaces(q=u'福州')
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/places.q(%E7%A6%8F%E5%B7%9E);count=5;start=0?format=json&select=short&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlaces(q=u'福州') ", 'pass')

		'''Example 9. Retrieving the Five Most Likely Places for a Given Placename'''
		self.__api.GetPlaces(q=u'中国')
		self.assertEqual(woeid.GetLastRequestUrl(),'http://where.yahooapis.com/v1/places.q(%E4%B8%AD%E5%9B%BD);count=5;start=0?format=json&select=short&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlaces(q=u'中国') ", 'pass')

		'''Example 10. Retrieving All Places for a Given Place Name and Place Type'''
		self.__api.GetPlaces(q='Long Island', typ=22, nd=True)
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/places$and(.q(Long%20Island),.type(22));count=5;start=0?format=json&select=short&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlaces(q='Long Island', typ=22, nd=True) ", 'pass')

		'''Example 11. Retrieving Places That Have the Given WOEIDs'''
		self.__api.GetPlaces(woeid=[2488042, 2488836, 2486340])
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/places.woeid(2488042,2488836,2486340);count=5;start=0?format=json&select=short&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlaces(woeid=[2488042, 2488836, 2486340]) ", 'pass')

		'''Example 12. Retrieving a Place Using a Given WOEID, in Long Representation'''
		self.__api.Select = 'long'
		self.__api.GetPlace(woeid=2507854)
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/place/2507854;count=5;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlace(woeid=2507854) ", 'pass')

		'''Example 13. Retrieving a Place with a Given WOEID, in Short Representation'''
		self.__api.Select = 'short'
		self.__api.GetPlace(woeid=2507854)
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/place/2507854;count=5;start=0?format=json&select=short&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlace(woeid=2507854) ", 'pass')

		'''Example 14. Retrieving a Place with a Given WOEID, in JSON format'''
		self.__api.Format = 'json'
		self.__api.GetPlace(woeid=12521721)
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/place/12521721;count=5;start=0?format=json&select=short&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlace(woeid=12521721) ", 'pass')

		'''Example 15. Retrieving the Parent Place of a Given WOEID, as a Long Representation'''
		self.__api.Select = 'long'
		self.__api.GetPlace(woeid=638242, parent=True)
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/place/638242/parent;count=5;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlace(woeid=638242, parent=True) ", 'pass')

		'''Example 16. Retrieving the Ancestors for a Given WOEID'''
		self.__api.GetPlace(woeid=12587712, ancestors=True)
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/place/12587712/ancestors;count=5;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlace(woeid=12587712, ancestors=True) ", 'pass')

		'''Example 17. Retrieving the Belongto Places of a Given WOEID'''
		self.__api.GetPlace(woeid=23424900, belongtos=True)
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/place/23424900/belongtos;count=5;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlace(woeid=23424900, belongtos=True) ", 'pass')

		'''Example 18. Retrieving Neighboring Places of a Given WOEID'''
		self.__api.GetPlace(woeid=2347563, neighbors=True)
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/place/2347563/neighbors;count=5;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlace(woeid=2347563, neighbors=True) ", 'pass')

		'''Example 19. Retrieving Neighbors of the Neighbors of a Place With a Given WOEID'''
		self.__api.GetPlace(woeid=2347563, neighbors=True, degree=2)
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/place/2347563/neighbors.degree(2);count=5;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlace(woeid=2347563, neighbors=True, degree=2) ", 'pass')

		'''Example 20. Retrieving Sibling Places of a Given WOEID'''
		self.__api.GetPlace(woeid=2347563, siblings=True)
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/place/2347563/siblings;count=5;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlace(woeid=2347563, siblings=True) ", 'pass')

		'''Example 21. Retrieving Children of Places of a Given WOEID'''
		self.__api.GetPlace(woeid=23424977, children=True)
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/place/23424977/children;count=5;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlace(woeid=23424977, children=True) ", 'pass')

		'''Example 22. Retrieving Children of the Children of a Place With a Given WOEID'''
		self.__api.GetPlace(woeid=2488042, children=True, degree=2)
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/place/2488042/children.degree(2);count=5;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlace(woeid=2488042, children=True, degree=2) ", 'pass')

		'''Example 23. Retrieving Descendants for a Given WOEID'''
		self.__api.GetPlace(woeid=2507854, descendants=True)
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/place/2507854/descendants;count=5;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlace(woeid=2507854, descendants=True) ", 'pass')

		'''Example 24. Retrieving a Place That is a Common Ancestor of Two Places'''
		self.__api.GetPlace(woeid=(2507854, 2380824), common=True)
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/place/2507854/common/2380824;count=5;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlace(woeid=(2507854, 2380824), common=True) ", 'pass')

		'''Example 25. Retrieving a Place That is Common Ancestor of Three Places'''
		self.__api.GetPlace(woeid=(2488042, 2488836, 2486340), common=True)
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/place/2488042/common/2488836/2486340;count=5;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlace(woeid=(2488042, 2488836, 2486340), common=True) ", 'pass')

		'''Example 26. Retrieving All Continents'''
		self.__api.GetContinents()
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/continents;count=0;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetContinents() ", 'pass')

		'''Example 27. Retrieving All Oceans'''
		self.__api.GetOceans()
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/oceans;count=0;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetOceans() ", 'pass')

		'''Example 28. Retrieving All Seas'''
		self.__api.GetSeas()
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/seas;count=0;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetSeas() ", 'pass')

		'''Example 29. Retrieving the Seas Adjacent to or Part of the Pacific Ocean'''
		self.__api.__select='short'
		self.__api.GetSeas(place='Pacific Ocean')
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/seas/Pacific%20Ocean;count=0;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetSeas(place='Pacific Ocean') ", 'pass')

		'''Example 30. Retrieving All Countries'''
		self.__api.GetCountries()
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/countries;count=0;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetCountries() ", 'pass')

		'''Example 31. Retrieving the Countries Within North America (NA)'''
		self.__api.GetCountries(place='NA')
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/countries/NA;count=0;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetCountries(place='NA') ", 'pass')

		'''Example 32. Retrieving the States Within the United States (US)'''
		self.__api.GetStates(country='US')
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/states/US;count=0;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetStates(country='US') ", 'pass')

		'''Example 33. Retrieving the Counties Within California (CA)'''
		self.__api.GetCounties(state='CA')
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/counties/CA;count=0;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetCounties(state='CA') ", 'pass')

		'''Example 34. Retrieving the Districts of Greater London'''
		self.__api.GetDistricts(county='Greater London')
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/districts/Greater%20London;count=0;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetDistricts(county='Greater London') ", 'pass')

		'''Example 35. Retrieving the WOEID and FIPs Code for a Given ISO Code'''
		self.__api.GetConcordance(namespace='iso', id='CA-BC')
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/concordance/iso/CA-BC;count=0;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetConcordance(namespace='iso', id='CA-BC') ", 'pass')

		'''Example 36. Retrieving a Collection of Place Types'''
		self.__api.GetPlacetypes()
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/placetypes;count=0;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlacetypes() ", 'pass')

		'''Example 37. Retrieving a Collection of Place Types and Their Descriptions'''
		self.__api.Select = 'long'
		self.__api.GetPlacetypes()
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/placetypes;count=0;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlacetypes() ", 'pass')

		'''Example 38. Retrieving a Partial Collection of Place Types'''
		self.__api.Select = 'short'
		self.__api.GetPlacetypes(typ=[0,2,22,37,38,15,16])
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/placetypes.type(0,2,22,37,38,15,16);count=0;start=0?format=json&select=short&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlacetypes(typ=[0,2,22,37,38,15,16]) ", 'pass')

		'''Example 39. Retrieving All Placetypes for Spain'''
		self.__api.GetPlacetypes(country='ES')
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/placetypes/ES;count=0;start=0?format=json&select=short&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlacetypes(country='ES') ", 'pass')

		'''Example 40. Retrieving a Short Representation of the Resource for a Place Type'''
		self.__api.GetPlacetypes(typ=35)
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/placetypes.type(35);count=0;start=0?format=json&select=short&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlacetypes(typ=35) ", 'pass')

		'''Example 41. Retrieving a Long Representation of the Resource for a Place Type'''
		self.__api.Select = 'long'
		self.__api.GetPlacetypes(typ=35)
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/placetypes.type(35);count=0;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlacetypes(typ=35) ", 'pass')

		'''Example 42. Retrieving the Province Placetype for Spain'''
		self.__api.GetPlacetype(typ=9,country='ES')
		self.assertEqual(woeid.GetLastRequestUrl(), 'http://where.yahooapis.com/v1/placetype/9/ES;count=0;start=0?format=json&select=long&lang=zh-hans-CN&appid=dj0yJmk9NEpTYVdQSllLVmtVJmQ9WVdrOVRtVkZSWGxFTm5NbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wMQ--')
		self.assertEqual(woeid.GetLastResponseCode(), 200)
		print("self.__api.GetPlacetype(typ=9,country='ES') ", 'pass')


if __name__ == "__main__":
	unittest.main()
