# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView


class MapBlacklistSearchResult(BrowserView):
    """
    Map blacklist search result view
    """
    def searchData(self):
        searchValue = self.request.get("searchValue")
        result = [{'name':"item1"+searchValue,
                   'description':"descriptionitem1",
                   'provider':"fournisseuritem1"},
                  {'name':"item2"+searchValue,
                   'description':"descriptionitem2",
                   'provider':"fournisseuritem2"},
                  {'name':"item3"+searchValue,
                   'description':"descriptionitem3",
                   'provider':"fournisseuritem3"},
                  ]
        return result
