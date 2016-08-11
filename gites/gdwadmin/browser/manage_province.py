# -*- coding: utf-8 -*-

from z3c.sqlalchemy import getSAWrapper
from Products.Five.browser import BrowserView
from zope.interface import implements
from interfaces import IProvinceView
from gites.db.content import Province


class ProvinceView(BrowserView):
    implements(IProvinceView)
    """
    """
    def getAllProvinces(self):
        """
        recuperation de toutes les provinces
        """
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Province)
        query = query.order_by(Province.prov_code)
        allProvinces = query.all()
        return allProvinces

    def getProvinceByPk(self, provincePk):
        """
        recuperation d'une province selon sa PK
        """
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Province)
        query = query.filter(Province.prov_pk == provincePk)
        province = query.one()
        return province

    def insertProvince(self):
        """
        Add une province
        """
        fields = self.request.form
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        newEntry = Province(prov_nom=fields.get('prov_nom'),
                            prov_code=fields.get('prov_code'))
        session.add(newEntry)
        session.flush()
        cible = "%s/portal_skins/gestion_gites/lister-les-provinces" % self.context.portal_url()
        self.request.response.redirect(cible)
        return ''
