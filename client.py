import config

__author__ = 'Renchen'
import api

def main(args=None):
    myapi = api.Api(appid=config.key,select='short',format='json')
    #api.PrettyPrintResult(myapi.GetPlaces(woeid=[2507854, 12521721, 638242]))
    api.PrettyPrintResult(myapi.GetPlaces(q='long island', typ=22, nd=True))
    #api.PrettyPrintResult(myapi.GetPlace(woeid=['23424775']))
    #api.PrettyPrintResult(myapi.GetPlace(9807,parent=True))
    # print(json.dumps(GetWoeid("China"), indent=4, separators={',', ': '}))


if __name__ == "__main__":
    main()