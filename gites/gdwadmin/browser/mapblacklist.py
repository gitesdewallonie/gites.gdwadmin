# -*- coding: utf-8 -*-

import json

from Products.Five.browser import BrowserView


class MapBlacklist(BrowserView):
    """
    Map blacklist view
    """
    def getBlacklist(self):
        result = [{'dataId': 'id4',
                   'name':"item4",
                   'description':"descriptionitem4",
                   'provider':"quefaire"},
                  {'dataId': 'id5',
                   'name':"item5",
                   'description':"descriptionitem5",
                   'provider':"resto"},
                  {'dataId': 'id6',
                   'name':"item6",
                   'description':"descriptionitem6",
                   'provider':"google"},
                  ]
        return result

    def removeData(self):
        dataId = self.request.dataId
        return dataId

    def addData(self):
        dataId = self.request.get('dataId')
        provider = self.request.get('provider')

        #XXX insert in database
        import time
        time.sleep(3)

        #return what we inserted in database
        result = {'dataId': dataId,
                  'name': dataId + '_name',
                  'description': dataId + '_description',
                  'provider': provider}
        return json.dumps(result)


class MapBlacklistLiveSearch(BrowserView):
    """
    Map blacklist view
    """

    def __call__(self):
        return json.dumps(['hello', 'world'])


class MapBlacklistSearchResult(BrowserView):
    """
    Map blacklist search result view
    """
    def searchData(self):
        searchValue = self.request.get("searchValue")
        if searchValue == "":
            return None
        result = [{'dataId': "id1",
                   'name': "item1" + searchValue,
                   'description': "descriptionitem1",
                   'provider': "quefaire"},
                  {'dataId': "id2",
                   'name': "item2" + searchValue,
                   'description': "descriptionitem2",
                   'provider': "google"},
                  {'dataId': "id3",
                   'name': "item3" + searchValue,
                   'description': "descriptionitem3",
                   'provider': "resto"},
                  ]
        return result
