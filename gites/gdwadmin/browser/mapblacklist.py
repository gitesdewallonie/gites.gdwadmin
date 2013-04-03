# -*- coding: utf-8 -*-

import json

from googleplaces import GooglePlaces, types, lang

from Products.Five.browser import BrowserView
from zope.component import getUtility
from z3c.sqlalchemy import getSAWrapper

from affinitic.pwmanager.interfaces import IPasswordManager

#Région wallonne center location
WALLONIE_CENTER = "50.401078,5.133648"


class MapBlacklist(BrowserView):
    """
    Map blacklist view
    """
    def getBlacklist(self):
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
        word = self.request.get('client_contains')
        result = []
        for item in getExternalDatas(word):
            result.append(item['name'])
        for item in getGoogleDatas(word):
            result.append(item['name'])
        return json.dumps(result)


class MapBlacklistSearchResult(BrowserView):
    """
    Map blacklist search result view
    """
    def searchData(self):

        searchValue = self.request.get("searchValue")
        if searchValue == "":
            return None
        result = []
        result.extend(getGoogleDatas(searchValue))
        result.extend(getExternalDatas(searchValue))
        return result


def getGoogleDatas(searchValue):
    # Google Place API KEY
    pwManager = getUtility(IPasswordManager, 'googleapi')
    apiKey = pwManager.password
    google_places = GooglePlaces(apiKey)

    query_result = google_places.query(
        location=WALLONIE_CENTER,
        name='"%s"'%searchValue.decode('utf-8').lower().replace("'",""),
        radius=50000,
        language=lang.FRENCH)

    result = []
    for place in query_result.places:
        item = dict(dataId=place.id,
                    name=place.name,
                    description=place.vicinity,
                    provider='google',
                    #XXXtypes les types doivent etre défini suivant ce qui est utilisé dans les gites
                    types=[types.TYPE_FOOD])
        result.append(item)
    #XXXnext probleme pour les request, 60 result max par page, et python-google-places ne gere pas
    # le next_page_token et pagetoken
    # https://developers.google.com/places/documentation/search?hl=fr
#    if query_result.getAttr('next_page_token'):
#        pass
    return result

def getExternalDatas(searchValue):
    wrapper = getSAWrapper('gites_wallons')
    session = wrapper.session

    mapExternalDataTable = wrapper.getMapper('map_external_data')

    query = session.query(mapExternalDataTable)
    result = []
    for item in query.all():
        if searchValue.decode('utf-8').lower() in item.ext_data_title.lower():
            item = dict(dataId=item.ext_data_id,
                        name=item.ext_data_title,
                        description=item.ext_data_type,
                        provider=item.ext_data_provider_pk,
                        #XXXtypes les types doivent etre défini suivant ce qui est utilisé dans les gites
                        types=[types.TYPE_FOOD])
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
    query = query.filter(mapBlacklistTable.blacklist_id == dataId)
    query = query.filter(mapBlacklistTable.blacklist_provider_pk == provider)
    result = query.one()
    session.delete(result)
    session.flush()
