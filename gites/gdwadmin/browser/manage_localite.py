# -*- coding: utf-8 -*-

from z3c.sqlalchemy import getSAWrapper
from Products.Five.browser import BrowserView
from zope.interface import implements
from interfaces import ILocaliteView
from gites.db.content import Localite


class LocaliteView(BrowserView):
    implements(ILocaliteView)
    """
    """
    def getAllLocalites(self):
        """
        recuperation de toutes les localites
        """
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Localite)
        query = query.order_by(Localite.localite_nom)
        allLocalites = query.all()
        return allLocalites

    def getLocaliteByPk(self, localitePk):
        """
        recuperation d'une localite selon sa PK
        """
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Localite)
        query = query.filter(Localite.localite_pk == localitePk)
        localite = query.one()
        return localite

    def insertLocalite(self):
        """
        Add a localite
        """
        fields = self.request.form
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        newEntry = Localite(localite_nom=fields.get('com_nom'),
                            localitecom_cp=fields.get('com_cp'),
                            localite_ins=fields.get('com_ins'),
                            localite_commune_fk=fields.get('com_ins'))
        session.add(newEntry)
        session.flush()
        cible = "%s/portal_skins/gestion_gites/lister-les-communes" % self.context.portal_url()
        self.request.response.redirect(cible)
        return ''
