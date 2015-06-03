# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.hebergement.typehebergement import TypeHebergement


class AddTypeHebergement(BrowserView):
    # @property
    # def type_heb_pk(self):
    #     return self.request.get('ftype_heb_pk')

    def add_typehebergement(self):

        typehebergement = TypeHebergement()
        typehebergement.type_heb_code = self.request.get('ftype_heb_code')
        typehebergement.type_heb_nom = self.request.get('ftype_heb_nom')
        typehebergement.type_heb_nom_nl = self.request.get('ftype_heb_nom_nl')
        typehebergement.type_heb_nom_uk = self.request.get('ftype_heb_nom_uk')
        typehebergement.type_heb_nom_de = self.request.get('ftype_heb_nom_de')
        typehebergement.type_heb_nom_it = self.request.get('ftype_heb_nom_it')
        typehebergement.type_heb_id = self.request.get('ftype_heb_id')
        typehebergement.type_heb_id_nl = self.request.get('ftype_heb_id_nl')
        typehebergement.type_heb_id_uk = self.request.get('ftype_heb_id_uk')
        typehebergement.type_heb_id_de = self.request.get('ftype_heb_id_de')
        typehebergement.type_heb_id_it = self.request.get('ftype_heb_id_it')

        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        session.add(typehebergement)
        return u'Le type d\'hébergement a été ajouté'


