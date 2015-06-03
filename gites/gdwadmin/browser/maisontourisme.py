# -*- coding: utf-8 -*-
# En rajoutant la ligne ci-dessus, on pourra utiliser des caractères particuliers dans
# les commentaires. Cette ligne doit toujours être placée sur la première ligne de code
# il ne peut rien y avoir avant.

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.maisontourisme import MaisonTourisme


class MaisonTourismeView(BrowserView):

    def maison_tourisme(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(MaisonTourisme).order_by(MaisonTourisme.mais_nom)
        return query.all()
