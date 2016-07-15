# -*- coding: utf-8 -*-
__author__ = 'Renchen'
import config
import api

def main(args=None):
    myapi = api.Api(appid=config.key,select='long',format='xml')

    '''Example 8. Retrieving the Most Likely Place for a Given Place Name'''
    api.PrettyPrintResult(myapi.GetPlaces(q='SFO'))

    '''Example 9. Retrieving the Five Most Likely Places for a Given Placename'''
    myapi._lang = 'zh-Hans'
    api.PrettyPrintResult(myapi.GetPlaces(q=u'中国',count=5))

    '''Example 10. Retrieving All Places for a Given Place Name and Place Type'''
    api.PrettyPrintResult(myapi.GetPlaces(q='Long Island',typ=22,nd=True))

    '''Example 11. Retrieving Places That Have the Given WOEIDs'''
    api.PrettyPrintResult(myapi.GetPlaces(woeid=[2488042,2488836,2486340]))

    '''Example 12. Retrieving a Place Using a Given WOEID'''
    api.PrettyPrintResult(myapi.GetPlace(woeid=2507854))

    '''Example 13. Retrieving a Place with a Given WOEID, in Short Representation'''
    myapi._select = 'short'
    api.PrettyPrintResult(myapi.GetPlace(woeid=2507854))

    '''Example 14. Retrieving a Place with a Given WOEID, in JSON format'''
    myapi._format = 'json'
    api.PrettyPrintResult(myapi.GetPlace(woeid=12521721))

    '''Example 15. Retrieving the Parent Place of a Given WOEID, as a Long Representation'''
    myapi._select = 'long'
    api.PrettyPrintResult(myapi.GetPlace(woeid=638242, parent=True))

    '''Example 16. Retrieving the Ancestors for a Given WOEID'''
    api.PrettyPrintResult(myapi.GetPlace(woeid=12587712, ancestors=True))

    '''Example 17. Retrieving the Belongto Places of a Given WOEID'''
    api.PrettyPrintResult(myapi.GetPlace(woeid=23424900, belongtos=True))

    '''Example 18. Retrieving Neighboring Places of a Given WOEID'''
    api.PrettyPrintResult(myapi.GetPlace(woeid=2347563, neighbors=True))

    '''Example 19. Retrieving Neighbors of the Neighbors of a Place With a Given WOEID'''
    api.PrettyPrintResult(myapi.GetPlace(woeid=2347563, neighbors=True, degree=2))

    '''Example 20. Retrieving Sibling Places of a Given WOEID'''
    api.PrettyPrintResult(myapi.GetPlace(woeid=2347563, siblings=True))

    '''Example 21. Retrieving Children of Places of a Given WOEID'''
    api.PrettyPrintResult(myapi.GetPlace(woeid=23424977, children=True))

    '''Example 22. Retrieving Children of the Children of a Place With a Given WOEID'''
    api.PrettyPrintResult(myapi.GetPlace(woeid=2488042, children=True, degree=2))

    '''Example 23. Retrieving Descendants for a Given WOEID'''
    api.PrettyPrintResult(myapi.GetPlace(woeid=2507854, descendants=True))

    '''Example 24. Retrieving a Place That is a Common Ancestor of Two Places'''
    api.PrettyPrintResult(myapi.GetPlace(woeid=(2507854, 2380824), common=True))

    '''Example 25. Retrieving a Place That is Common Ancestor of Three Places'''
    api.PrettyPrintResult(myapi.GetPlace(woeid=(2488042, 2488836, 2486340), common=True))

    '''Example 26. Retrieving All Continents'''
    api.PrettyPrintResult(myapi.GetContinents())

    '''Example 27. Retrieving All Oceans'''
    api.PrettyPrintResult(myapi.GetOceans())

    '''Example 28. Retrieving All Seas'''
    api.PrettyPrintResult(myapi.GetSeas())

    '''Example 29. Retrieving the Seas Adjacent to or Part of the Pacific Ocean'''
    myapi._select='short'
    api.PrettyPrintResult(myapi.GetSeas(place='Pacific Ocean'))

    '''Example 30. Retrieving All Countries'''
    api.PrettyPrintResult(myapi.GetCountries())

    '''Example 31. Retrieving the Countries Within North America (NA)'''
    api.PrettyPrintResult(myapi.GetCountries(place='NA'))

    '''Example 32. Retrieving the States Within the United States (US)'''
    api.PrettyPrintResult(myapi.GetStates(country='US'))

    '''Example 33. Retrieving the Counties Within California (CA)'''
    api.PrettyPrintResult(myapi.GetCounties(state='CA'))

    '''Example 34. Retrieving the Districts of Greater London'''
    api.PrettyPrintResult(myapi.GetDistricts(county='Greater London'))

    '''Example 35. Retrieving the WOEID and FIPs Code for a Given ISO Code'''
    api.PrettyPrintResult(myapi.GetConcordance(namespace='iso', id='CA-BC'))

    '''Example 36. Retrieving a Collection of Place Types'''
    api.PrettyPrintResult(myapi.GetPlacetypes())

    '''Example 37. Retrieving a Collection of Place Types and Their Descriptions'''
    myapi._select = 'long'
    api.PrettyPrintResult(myapi.GetPlacetypes())

    '''Example 38. Retrieving a Partial Collection of Place Types'''
    myapi._select = 'short'
    api.PrettyPrintResult(myapi.GetPlacetypes(typ=[0,2,22,37,38,15,16]))

    '''Example 39. Retrieving All Placetypes for Spain'''
    api.PrettyPrintResult(myapi.GetPlacetypes(country='ES'))

    '''Example 40. Retrieving a Short Representation of the Resource for a Place Type'''
    api.PrettyPrintResult(myapi.GetPlacetypes(typ=35))

    '''Example 41. Retrieving a Long Representation of the Resource for a Place Type'''
    myapi._select = 'long'
    api.PrettyPrintResult(myapi.GetPlacetypes(typ=35))

    '''Example 42. Retrieving the Province Placetype for Spain'''
    api.PrettyPrintResult(myapi.GetPlacetype(typ=9,country='ES'))


if __name__ == "__main__":
    main()