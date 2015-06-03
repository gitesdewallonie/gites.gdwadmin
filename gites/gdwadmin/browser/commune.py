# -*- coding: utf-8 -*-
# En rajoutant la ligne ci-dessus, on pourra utiliser des caractères particuliers dans
# les commentaires. Cette ligne doit toujours être placée sur la première ligne de code
# il ne peut rien y avoir avant.

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.commune import Commune
from gites.db.content.regionguide import RegionGuide
from gites.db.content.province import Province
from gites.db.content.maisontourisme import MaisonTourisme


class CommuneView(BrowserView):

    def table_com(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Commune).join('province').join('regionGuide').join('maisonTourisme').order_by(Commune.com_nom)
        return query.all()


    def regionguide(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(RegionGuide).order_by(RegionGuide.reg_nom)
        return query.all()


    def province(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Province).order_by(Province.prov_nom)
        return query.all()


    def maisontourisme(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(MaisonTourisme).order_by(MaisonTourisme.mais_nom)
        return query.all()

