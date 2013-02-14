# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView


class MapBlacklistSearchResult(BrowserView):
    """
    Map blacklist search result view
    """
    def searchData(self):
        searchValue = self.request.get("searchValue")
        result = [{'id':"id1"+searchValue,
                   'name':"item1"+searchValue,
                   'description':"descriptionitem1",
                   'provider':"fournisseuritem1"},
                  {'id':"id2"+searchValue,
                   'name':"item2"+searchValue,
                   'description':"descriptionitem2",
                   'provider':"fournisseuritem2"},
                  {'id':"id3"+searchValue,
                   'name':"item3"+searchValue,
                   'description':"descriptionitem3",
                   'provider':"fournisseuritem3"},
                  ]
        return result
