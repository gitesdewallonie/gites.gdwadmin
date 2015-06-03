# -*- coding: utf-8 -*-
# En rajoutant la ligne ci-dessus, on pourra utiliser des caractères particuliers dans
# les commentaires. Cette ligne doit toujours être placée sur la première ligne de code
# il ne peut rien y avoir avant.

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.info.infopratique import InfoPratique
from gites.db.content.info.typeinfopratique import TypeInfoPratique
from gites.db.content.commune import Commune
from gites.db.content.maisontourisme import MaisonTourisme


class InfoPratiqueView(BrowserView):

    def infopratique(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(InfoPratique, Commune, MaisonTourisme).filter(Commune.com_pk == InfoPratique.infoprat_commune_fk,
                                                                            MaisonTourisme.mais_pk == Commune.com_mais_fk).order_by(InfoPratique.infoprat_nom)
        return query.all()

    def commune(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Commune.com_pk,
                              Commune.com_nom,
                              Commune.com_cp).order_by(Commune.com_cp)
        return query.all()

    def typeinfopratique(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(TypeInfoPratique.typinfoprat_nom_fr,
                              TypeInfoPratique.typinfoprat_pk)
        return query.all()

