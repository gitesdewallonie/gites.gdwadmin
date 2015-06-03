# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.info.infopratique import InfoPratique


class AddInfoPratique(BrowserView):

    def add_infopratique(self):

        infopratique = InfoPratique()
        infopratique.infoprat_nom = self.request.get('finfoprat_nom')
        infopratique.infoprat_adresse = self.request.get('finfoprat_adresse')
        infopratique.infoprat_commune_fk = self.request.get('finfoprat_commune_fk')
        infopratique.infoprat_localite = self.request.get('finfoprat_localite')
        infopratique.infoprat_url = self.request.get('finfoprat_url')
        infopratique.infoprat_gps_long = self.request.get('finfoprat_gps_long')
        infopratique.infoprat_gps_lat = self.request.get('finfoprat_gps_lat')
        infopratique.infoprat_type_infoprat_fk = self.request.get('finfoprat_type_infoprat_fk')
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        session.add(infopratique)
        return u'L\'info pratique a été ajoutée'


