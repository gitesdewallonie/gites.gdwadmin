# -*- coding: utf-8 -*-
# En rajoutant la ligne ci-dessus, on pourra utiliser des caractères particuliers dans
# les type_hebmentaires. Cette ligne doit toujours être placée sur la première ligne de code
# il ne peut rien y avoir avant.

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.hebergement.typehebergement import TypeHebergement


class ModifTypeHebergement(BrowserView):

    @property
    def type_heb_pk(self):
        return self.request.get('ftype_heb_pk')

    def type_hebergement(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(TypeHebergement.type_heb_pk,
                              TypeHebergement.type_heb_code,
                              TypeHebergement.type_heb_nom,
                              TypeHebergement.type_heb_nom_nl,
                              TypeHebergement.type_heb_nom_uk,
                              TypeHebergement.type_heb_nom_de,
                              TypeHebergement.type_heb_nom_it,
                              TypeHebergement.type_heb_id,
                              TypeHebergement.type_heb_id_nl,
                              TypeHebergement.type_heb_id_uk,
                              TypeHebergement.type_heb_id_de,
                              TypeHebergement.type_heb_id_it).filter(TypeHebergement.type_heb_pk == self.type_heb_pk)
        return query.first()
