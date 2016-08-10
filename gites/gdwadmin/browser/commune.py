# -*- coding: utf-8 -*-

from z3c.sqlalchemy import getSAWrapper
from Products.Five.browser import BrowserView
from zope.interface import implements
from interfaces import ICommuneView
from gites.db.content import Commune


class CommuneView(BrowserView):
    implements(ICommuneView)
    """
    """
    def getAllCommunes(self):
        """
        recuperation de toutes les communes
        """
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Commune)
        query = query.order_by(Commune.com_nom)
        allCommunes = query.all()
        return allCommunes

    def getAllCommunesByRegion(self, langue):
        """
        recuperation de toutes les communes selon leur langues
        basé sur la com_prov_pk  (table priovince)
        0 --> toutes les provinces flamandes
        """
        if langue == 'N':
            provincePk = [0]
        if langue == "F":
            provincePk = [1, 2, 3, 4, 5, 6]
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Commune)
        query = query.filter(Commune.com_prov_fk.in_(provincePk))
        query = query.order_by(Commune.com_nom)
        allCommunes = query.all()
        return allCommunes

    def getCommuneByPk(self, communePk):
        """
        recuperation d'une commune selon sa PK
        """
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Commune)
        query = query.filter(Commune.com_pk == communePk)
        commune = query.one()
        return commune

    def insertCommune(self):
        """
        Add a commune
        """
        fields = self.request.form
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        insertCommune = wrapper.getMapper('commune@')
        newEntry = insertCommune(com_nom=fields.get('com_nom'),
                                 com_cp=fields.get('com_cp'),
                                 com_ins=fields.get('com_ins'),
                                 com_id=fields.get('com_id'),
                                 com_reg_fk=fields.get('com_reg_fk'),
                                 com_prov_fk=fields.get('com_prov_fk'),
                                 com_mais_fk=fields.get('com_mais_fk'))
        session.add(newEntry)
        session.flush()
        cible = "%s/portal_skins/gestion_gites/communes/communes" % self.context.portal_url()
        self.request.response.redirect(cible)
        return ''
