# -*- coding: utf-8 -*-
# En rajoutant la ligne ci-dessus, on pourra utiliser des caractères particuliers dans
# les commentaires. Cette ligne doit toujours être placée sur la première ligne de code
# il ne peut rien y avoir avant.

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.hebergement.typehebergement import TypeHebergement


class TypeHebergementView(BrowserView):

    def type_hebergement(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(TypeHebergement).order_by(TypeHebergement.type_heb_nom)
        return query.all()
