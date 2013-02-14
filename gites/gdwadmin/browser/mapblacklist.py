# -*- coding: utf-8 -*-

import json

from Products.Five.browser import BrowserView


class MapBlacklist(BrowserView):
    """
    Map blacklist view
    """
    def getBlacklist(self):
        result = [{'id': 'id4',
                   'name':"item4",
                   'description':"descriptionitem4",
                   'provider':"fournisseuritem4"},
                  {'id': 'id5',
                   'name':"item5",
                   'description':"descriptionitem5",
                   'provider':"fournisseuritem5"},
                  {'id': 'id6',
                   'name':"item6",
                   'description':"descriptionitem6",
                   'provider':"fournisseuritem6"},
                  ]
        return result

    def removeData(self):
        dataId = self.request.dataId
        return dataId

    def addData(self):
        dataId = self.request.dataId

        #XXX insert in database

        #return what we inserted in database
        result = {'id': dataId,
                  'name': dataId + '_name',
                  'description': dataId + '_description',
                  'provider': dataId + '_provider'}
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
        result = [{'id': "id1" + searchValue,
                   'name': "item1" + searchValue,
                   'description': "descriptionitem1",
                   'provider': "fournisseuritem1"},
                  {'id': "id2" + searchValue,
                   'name': "item2" + searchValue,
                   'description': "descriptionitem2",
                   'provider': "fournisseuritem2"},
                  {'id': "id3" + searchValue,
                   'name': "item3" + searchValue,
                   'description': "descriptionitem3",
                   'provider': "fournisseuritem3"},
                  ]
        return result
