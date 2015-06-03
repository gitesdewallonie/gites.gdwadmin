# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.province import Province


class UpdateProvince(BrowserView):
    @property
    def prov_pk(self):
        return self.request.get('fprov_pk')

    def update_province(self):

        province = self.province()
        province.prov_nom = self.request.get('fprov_nom')

        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        session.add(province)
        return u'La province a été modifiée'

    def province(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        prov_pk = self.request.get('fprov_pk')
        query = session.query(Province).filter(Province.prov_pk == prov_pk)
        results = query.first()
        return results

