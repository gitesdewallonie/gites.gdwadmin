# -*- coding: utf-8 -*-
# En rajoutant la ligne ci-dessus, on pourra utiliser des caractères particuliers dans
# les commentaires. Cette ligne doit toujours être placée sur la première ligne de code
# il ne peut rien y avoir avant.

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.proprio.proprio import Proprio
from gites.db.content.proprio.civilite import Civilite
from gites.db.content.commune import Commune
from gites.db.content.hebergement.hebergement import Hebergement
from gites.db.content.hebergement.hebergementview import HebergementView
from sqlalchemy import func, and_


class ModifProprioView(BrowserView):
    #On récupère la valeur de pro_pk, transmise par la page précédente,
    # on l'appelera dans les requêtes ci-dessous en utilisant self.pro_pk
    @property
    def pro_pk(self):
        return self.request.get('fpro_pk')


    def proprio(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Proprio).filter(Proprio.pro_pk == self.pro_pk)
        results = query.first()
        return results

    def civilite(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Civilite.civ_pk,
                              Civilite.civ_titre).join(Proprio).filter(Proprio.pro_pk == self.pro_pk)
        return query.all()

    def commune(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Commune.com_pk,
                              Commune.com_nom,
                              Commune.com_cp).join(Proprio).filter(Proprio.pro_pk == self.pro_pk)
        return query.all()

    def proprio_calendrier(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb = session.query(Hebergement.heb_calendrier_proprio).join(Proprio).filter(Proprio.pro_pk == self.pro_pk)
        # heb = session.query(Hebergement.heb_calendrier_proprio).filter(Hebergement.heb_pk == self.pro_pk)
        results = heb.first()
        etat_calendrier = True
        if results == 'bloque':
            etat_calendrier = False
        return etat_calendrier

    def heb_alloch(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb = session.query(Hebergement.heb_desactivation_alloch).join(Proprio).filter(Proprio.pro_pk == self.pro_pk)
        results = heb.first()
        alloch = False
        if results:
            alloch = True
        return alloch

    def hebergement_view(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(HebergementView.heb_site_public).join(Proprio).filter(Proprio.pro_pk == self.pro_pk)
        results = query.first()
        heb_site = True
        if results == '0':
            heb_site = False
        return heb_site

    def hebergement(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Hebergement.heb_code_gdw,
                              Hebergement.heb_nom,
                              Hebergement.heb_pk,
                              Hebergement.heb_cgt_cap_max,
                              Hebergement.heb_typeheb_fk
                              ).join(Proprio).filter(Proprio.pro_pk == self.pro_pk)
        results = query.all()
        return results

    def com(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Commune.com_nom,
                              Commune.com_cp,
                              Commune.com_pk).join(Proprio).filter(and_(Commune.com_pk == Proprio.pro_com_fk,
                                                                        Proprio.pro_pk == self.pro_pk))
        return query.all()



    def localite(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Hebergement.heb_com_fk).join(Proprio).filter(Proprio.pro_pk == self.pro_pk)
        heb = query.first()

        query = session.query(Commune.com_nom, Commune.com_cp).filter(and_(Commune.com_pk == heb))
        return query.all()


    def etat_doublon_log(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session

        query = session.query(Proprio.pro_log).filter(Proprio.pro_pk == self.pro_pk)
        log = query.scalar()
        # return log

        etat = session.query(func.count(Proprio.pro_pk)).filter(and_(
            Proprio.pro_etat == 't',
            Proprio.pro_log == log,
            Proprio.pro_pk != self.pro_pk))
        etat = etat.scalar()
        # return etat

        proprio_etat = False
        if etat > 0:
            proprio_etat = True
        return proprio_etat




