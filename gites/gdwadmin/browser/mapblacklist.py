# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView


class MapBlacklist(BrowserView):
    """
    Map blacklist view
    """
    def getBlacklist(self):
        result = [{'name':"item4",
                   'description':"descriptionitem4",
                   'provider':"fournisseuritem4"},
                  {'name':"item5",
                   'description':"descriptionitem5",
                   'provider':"fournisseuritem5"},
                  {'name':"item6",
                   'description':"descriptionitem6",
                   'provider':"fournisseuritem6"},
                  ]
        return result

    def removeData(self):
        dataId = self.request.dataId

    def addData(self):
        dataId = self.request.dataId
        return dataId

