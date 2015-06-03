# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.commune import Commune


class UpdateCommune(BrowserView):
    @property
    def com_pk(self):
        return self.request.get('fcom_pk')

    def update_table_com(self):

        commune = self.commune()
        commune.com_nom = self.request.get('fcom_nom')
        commune.com_cp = self.request.get('fcom_cp')
        commune.com_ins = self.request.get('fcom_ins')
        commune.com_reg_fk = self.request.get('fcom_reg_fk')
        commune.com_prov_fk = self.request.get('fcom_prov_fk')
        commune.com_mais_fk = self.request.get('fcom_mais_fk')
        commune.com_id = self.request.get('fcom_id')

        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        session.add(commune)
        return u'La commune a été ajoutée'

    def commune(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        com_pk = self.request.get('fcom_pk')
        query = session.query(Commune).filter(Commune.com_pk == com_pk)
        results = query.first()
        return results

