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
        query = query.order_by(Localite.localite_commune_fk)
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
        localiteNom = fields.get('localite_nom'),
        localiteCp = fields.get('localite_cp'),
        localiteIns = fields.get('localite_ins', None),
        localiteCommuneFk = fields.get('localite_commune_fk')
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        newEntry = Localite(localite_nom=localiteNom,
                            localite_cp=localiteCp,
                            localite_ins=localiteIns,
                            localite_commune_fk=localiteCommuneFk)
        session.add(newEntry)
        session.flush()
        cible = "%s/portal_skins/gestion_gites/lister-les-localites" % self.context.portal_url()
        self.request.response.redirect(cible)
        return ''

    def updateLocalite(self):
        """
        Update a localite
        """
        fields = self.context.REQUEST
        localitePk = getattr(fields, 'localite_pk', None)
        localiteNom = getattr(fields, 'localite_nom', None)
        localiteCp = getattr(fields, 'localite_cp', None)
        localiteIns = getattr(fields, 'localite_ins', None)
        localiteCommuneFk = getattr(fields, 'localite_commune_fk', None)

        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Localite)
        query = query.filter(Localite.localite_pk == localitePk)
        localite = query.one()
        localite.localite_nom = unicode(localiteNom, 'utf-8')
        localite.localite_cp = unicode(localiteCp, 'utf-8')
        localite.localite_ins = unicode(localiteIns, 'utf-8')
        localite.localite_commune_fk = localiteCommuneFk
        session.flush()

        cible = "%s/portal_skins/gestion_gites/lister-les-localites" % self.context.portal_url()
        self.request.response.redirect(cible)
        return ''

    def deleteLocalite(self):
        """
        Delete a localite
        """
        fields = self.context.REQUEST
        localitePk = getattr(fields, 'localite_pk', None)
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Localite)
        query = query.filter(Localite.localite_pk == localitePk)
        localite = query.one()
        session.delete(localite)
        session.flush()

        cible = "%s/portal_skins/gestion_gites/lister-les-localites" % self.context.portal_url()
        self.request.response.redirect(cible)
        return ''
