========
Examples
========

Example 1: Create an ``woeid`` api object
*****************************************
::

    import woeid
    api = woeid.Api(client*id=`YOUR-CLIENT-ID`, select='long', format='xml')

    # Specify the requesting language
    api.Lang = 'zh*Hans'

    # Specify the view
    api.Select = 'short'

    # Set the response format
    api.Format = 'json'

    # Set the maximum number of records returned
    api.Count = 5

Example 2: Retrieving the Most Likely Place for a Given Place Name'
*******************************************************************

::

    woeid.PrettyPrintResult(api.GetPlaces(q=u'福州'))

Example 3: Retrieving the Five Most Likely Places for a Given Placename'
************************************************************************

::

    woeid.PrettyPrintResult(api.GetPlaces(q=u'中国'))

Example 4: Retrieving All Places for a Given ``place name`` and ``placetype``'
******************************************************************************

::

    woeid.PrettyPrintResult(api.GetPlaces(q='Long Island', typ=22, nd=True))

Example 5: Retrieving Places That Have the Given ``woeids``'
************************************************************

::

    woeid.PrettyPrintResult(api.GetPlaces(woeid=[2488042, 2488836, 2486340]))

Example 6: Retrieving a Place Using a Given ``woeid``'
******************************************************

::

    woeid.PrettyPrintResult(api.GetPlace(woeid=2507854))

Example 7: Retrieving a Place with a Given ``woeid``, in `short` Representation
*******************************************************************************

::

    api.Select = 'short'
    woeid.PrettyPrintResult(api.GetPlace(woeid=2507854))

Example 8: Retrieving the Parent Place of a Given ``woeid``, as a ``long`` Representation
*****************************************************************************************

::

    api.Select = 'long'
    woeid.PrettyPrintResult(api.GetPlace(woeid=638242, parent=True))

Example 9. Retrieving the Ancestors for a Given ``woeid``'
**********************************************************

::

    woeid.PrettyPrintResult(api.GetPlace(woeid=12587712, ancestors=True))

Example 10. Retrieving a Place That is a ``common`` Ancestor of Two Places'
***************************************************************************

::

    woeid.PrettyPrintResult(api.GetPlace(woeid=(2507854, 2380824), common=True))

Example 11. Retrieving a Place That is ``common`` Ancestor of Three Places'
***************************************************************************

::

    woeid.PrettyPrintResult(api.GetPlace(woeid=(2488042, 2488836, 2486340), common=True))

Example 12. Retrieving All Continents'
**************************************

::

    woeid.PrettyPrintResult(api.GetContinents())

Example 13. Retrieving the Seas Adjacent to or Part of the Pacific Ocean'
*************************************************************************

::

   woeid.PrettyPrintResult(api.GetSeas(place='Pacific Ocean'))

Example 14. Retrieving the Countries Within North America (NA)'
***************************************************************

::

    woeid.PrettyPrintResult(api.GetCountries(place='NA'))

Example 15. Retrieving the States Within the United States (US)'
****************************************************************

::

    woeid.PrettyPrintResult(api.GetStates(country='US'))

Example 16. Retrieving the Districts of Greater London'
*******************************************************

::

    woeid.PrettyPrintResult(api.GetDistricts(county='Greater London'))

Example 17. Retrieving the WOEID and FIPs Code for a Given ISO Code'
********************************************************************

::

    woeid.PrettyPrintResult(api.GetConcordance(namespace='iso', id='CA-BC'))

Example 18. Retrieving a Partial Collection of Place Types'
***********************************************************

::

    woeid.PrettyPrintResult(api.GetPlacetypes(typ=[0,2,22,37,38,15,16]))

