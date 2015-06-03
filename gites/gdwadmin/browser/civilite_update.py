# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.proprio.civilite import Civilite


class UpdateCivilite(BrowserView):
    @property
    def civ_pk(self):
        return self.request.get('fciv_pk')

    def update_civilite(self):

        civilite = self.civilite()
        civilite.civ_titre = self.request.get('fciv_titre')

        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        session.add(civilite)
        return u'Cette civilité a été modifiée'

    def civilite(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        civ_pk = self.request.get('fciv_pk')
        query = session.query(Civilite).filter(Civilite.civ_pk == civ_pk)
        return query.first()


