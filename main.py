import utility

__author__ = 'Renchen'
import config
from modules import(
    Filters,
    FamilySelectors,
)
from utility import Utility
BuildParams = Utility.BuildParams
BuildUrls = Utility.BuildUrls
MakeRequest = Utility.MakeRequest
PrettyPrintResult = Utility.PrettyPrintResult

class Api():
    def __init__(self,appid):
        self._base_url = 'http://where.yahooapis.com/v1/'
        self._appid = appid

    def GetPlaces(self,
                  q=None,
                  woeid=None,
                  typ=None,
                  degree=None,
                  nd=None,
                  parent=False,
                  ancestors=False,
                  belongtos=False,
                  neighbors=False,
                  siblings=False,
                  children=False,
                  descredants=False,
                  select='short',
                  format='json'):
        family_selectors = FamilySelectors(parent,ancestors,belongtos,siblings,children,descredants)
        filters = Filters(q, woeid, typ, degree, nd)
        extra_paths = ['places']
        extra_params = BuildParams(self._appid, format=format, select=select)
        url = BuildUrls(self._base_url, extra_paths, extra_params, filters, family_selectors)
        return MakeRequest(url)


def main(args=None):
    api = Api(appid=config.key)
    PrettyPrintResult(api.GetPlaces(woeid=[2507854, 12521721, 638242]))
    # print(json.dumps(GetWoeid("China"), indent=4, separators={',', ': '}))


if __name__ == "__main__":
    main()