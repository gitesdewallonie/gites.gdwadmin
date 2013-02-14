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
