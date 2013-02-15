# -*- coding: utf-8 -*-

import json

from Products.Five.browser import BrowserView
from zope.component import getUtility
from z3c.sqlalchemy import getSAWrapper
from googleplaces import GooglePlaces, types, lang
from affinitic.pwmanager.interfaces import IPasswordManager

class MapBlacklist(BrowserView):
    """
    Map blacklist view
    """
    def getBlacklist(self):
        result = [{'dataId': 'id4',
                   'name':"item4",
                   'description':"descriptionitem4",
                   'provider':"quefaire.be"},
                  {'dataId': 'id5',
                   'name':"item5",
                   'description':"descriptionitem5",
                   'provider':"resto.be"},
                  {'dataId': 'id6',
                   'name':"item6",
                   'description':"descriptionitem6",
                   'provider':"google"},
                  ]
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session

        mapBlacklistTable = wrapper.getMapper('map_blacklist')

        query = session.query(mapBlacklistTable)
        result = query.all()
        return result

    def removeData(self):
        dataId = self.request.get('dataId')
        provider = self.request.get('provider')

        #XXX remove in database
        removeBlacklistData(dataId, provider)

    def addData(self):
        dataId = self.request.get('dataId')
        name = self.request.get('name')
        description = self.request.get('description')
        provider = self.request.get('provider')

        #XXX insert in database
        insertBlacklistData(dataId, name, description, provider)

        #return what we inserted in database
        result = {'dataId': dataId,
                  'name': name,
                  'description': description,
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
        # Google Place API KEY
        pwManager = getUtility(IPasswordManager, 'googleapi')
        apiKey = pwManager.password
        google_places = GooglePlaces(apiKey)

        query_result = google_places.query(
                location='Région wallonne', keyword=searchValue,
                radius=50000)

        result = []
        for place in query_result.places:
            item = dict(dataId = place.reference,
                        name = place.name,
                        description = place.vicinity,
                        provider = 'google')
            result.append(item)
        return result


def insertBlacklistData(dataId, name, description, provider):
    """
    Insert a new map data in map_blacklist table in database
    """
    wrapper = getSAWrapper('gites_wallons')
    session = wrapper.session

    mapBlacklistTable = wrapper.getMapper('map_blacklist')
    mapBlacklistRow = mapBlacklistTable()
    mapBlacklistRow.blacklist_id = dataId
    mapBlacklistRow.blacklist_name = name
    mapBlacklistRow.blacklist_description = description
    mapBlacklistRow.blacklist_provider_pk = provider

    session.add(mapBlacklistRow)
    session.flush()
    session.refresh(mapBlacklistRow)


def removeBlacklistData(dataId, provider):
    """
    Remove a map data in map_blacklist table in database
    """
    wrapper = getSAWrapper('gites_wallons')
    session = wrapper.session

    mapBlacklistTable = wrapper.getMapper('map_blacklist')

    query = session.query(mapBlacklistTable)
    query = query.filter(mapBlacklistTable.blacklist_id==dataId)
    query = query.filter(mapBlacklistTable.blacklist_provider_pk==provider)
    result = query.one()
    session.delete(result)
    session.flush()
