# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.proprio.civilite import Civilite


class AddCivilite(BrowserView):
    # @property
    # def type_heb_pk(self):
    #     return self.request.get('ftype_heb_pk')

    def add_civilite(self):

        civilite = Civilite()
        civilite.civ_titre = self.request.get('fciv_titre')

        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        session.add(civilite)
        return u'La civilité a été ajoutée'


