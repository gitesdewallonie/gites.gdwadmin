# -*- coding: utf-8 -*-
# En rajoutant la ligne ci-dessus, on pourra utiliser des caractères particuliers dans
# les commentaires. Cette ligne doit toujours être placée sur la première ligne de code
# il ne peut rien y avoir avant.

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.proprio.proprio import Proprio
from gites.db.content.commune import Commune
from gites.db.content.proprio.civilite import Civilite
from sqlalchemy import func


class ProprioView(BrowserView):
    @property
    def etat(self):
        return self.request.get('activite')

    # Nombre de propriétaires :
    def proprio_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(func.count(Proprio.pro_pk))
        return query.scalar()

    # Nombre de propriétaires actifs :
    def proprio_active_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(func.count(Proprio.pro_pk)).filter(
            Proprio.pro_etat == 'True')
        return query.scalar()

    # Nombre de propriétaires désactivés :
    def proprio_desactive_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(func.count(Proprio.pro_pk)).filter(
            Proprio.pro_etat == 'False')
        return query.scalar()


    def proprio(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Proprio).join(Commune).order_by(Proprio.pro_nom1)
        return query.all()


    def localite(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        etat = self.etat
        if etat == 't' or etat == 'f':
            query = session.query(Proprio, Commune).filter(Commune.com_pk == Proprio.pro_com_fk,
                                                           Proprio.pro_etat == etat).order_by(Proprio.pro_nom1)
            return query.all()
        if etat == 'a':
            query = session.query(Proprio, Commune).filter(Commune.com_pk == Proprio.pro_com_fk).order_by(Proprio.pro_nom1)
            return query.all()




    def civilite(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Civilite).order_by(Civilite.civ_titre)
        return query.all()

    def commune(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Commune.com_pk,
                              Commune.com_nom,
                              Commune.com_cp).order_by(Commune.com_cp)
        return query.all()


    # def localite(self):
    #     wrapper = getSAWrapper('gites_wallons')
    #     session = wrapper.session
    #     etat = self.etat
    #     if etat == True:
    #         etat == True
    #     if etat == False:
    #         etat == False
    #     query = session.query(Proprio, Commune).filter(Commune.com_pk == Proprio.pro_com_fk,
    #                                                    Proprio.pro_etat == etat).order_by(Proprio.pro_nom1)
    #     return query.all()






