# -*- coding: utf-8 -*-
# En rajoutant la ligne ci-dessus, on pourra utiliser des caractères particuliers dans
# les maismentaires. Cette ligne doit toujours être placée sur la première ligne de code
# il ne peut rien y avoir avant.

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.maisontourisme import MaisonTourisme


class ModifMaisonTourisme(BrowserView):

    @property
    def mais_pk(self):
        return self.request.get('fmais_pk')

    def maison_tourisme(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(MaisonTourisme.mais_pk,
                              MaisonTourisme.mais_nom,
                              MaisonTourisme.mais_url,
                              MaisonTourisme.mais_code,
                              MaisonTourisme.mais_gps_long,
                              MaisonTourisme.mais_gps_lat,
                              MaisonTourisme.mais_id).filter(MaisonTourisme.mais_pk == self.mais_pk)
        return query.first()
