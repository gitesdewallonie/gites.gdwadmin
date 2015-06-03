# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.maisontourisme import MaisonTourisme


class UpdateMaisonTourisme(BrowserView):
    @property
    def mais_pk(self):
        return self.request.get('fmais_pk')

    def update_maisontourisme(self):

        maisontourisme = self.maisontourisme()
        maisontourisme.mais_nom = self.request.get('fmais_nom')
        maisontourisme.mais_url = self.request.get('fmais_url')
        maisontourisme.mais_code = self.request.get('fmais_code')
        maisontourisme.mais_gps_long = self.request.get('fmais_gps_long')
        maisontourisme.mais_gps_lat = self.request.get('fmais_gps_lat')
        maisontourisme.mais_id = self.request.get('fmais_id')

        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        session.add(maisontourisme)
        return u'La maisontourisme a été ajoutée'

    def maisontourisme(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        mais_pk = self.request.get('fmais_pk')
        query = session.query(MaisonTourisme).filter(MaisonTourisme.mais_pk == mais_pk)
        return query.first()


