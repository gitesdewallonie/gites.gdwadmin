# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.proprio.proprio import Proprio


class UpdateProprio(BrowserView):
    @property
    def pro_pk(self):
        return self.request.get('fpro_pk')

    def update_proprio(self):

        proprio = self.proprio()
        proprio.pro_nom1 = self.request.get('fpro_nom1')
        proprio.pro_civ_fk = self.request.get('fpro_civ_fk')
        proprio.pro_nom1 = self.request.get('fpro_nom1')
        proprio.pro_prenom1 = self.request.get('fpro_prenom1')
        proprio.pro_nom2 = self.request.get('fpro_nom2')
        proprio.pro_prenom2 = self.request.get('fpro_prenom2')
        proprio.pro_societe = self.request.get('fpro_societe')
        proprio.pro_adresse = self.request.get('fpro_adresse')
        proprio.pro_cp = self.request.get('fpro_cp')
        proprio.pro_email = self.request.get('fpro_email')
        proprio.pro_tel_priv = self.request.get('fpro_tel_priv')
        proprio.pro_tel_bur = self.request.get('fpro_tel_bur')
        proprio.pro_fax_priv = self.request.get('fpro_fax_priv')
        proprio.pro_fax_bur = self.request.get('fpro_fax_bur')
        proprio.pro_gsm1 = self.request.get('fpro_gsm1')
        proprio.pro_gsm2 = self.request.get('fpro_gsm2')
        proprio.pro_tva = self.request.get('fpro_tva')
        proprio.pro_langue = self.request.get('fpro_langue')
        proprio.pro_pass = self.request.get('fpro_pass')
        proprio.pro_etat = self.request.get('fpro_etat')
        # XXX On s'occupera des suivantes séparemment plus tard
        # import pdb; pdb.set_trace()
        # hebergement.heb_calendrier_proprio = self.request.get('heb_calendrier_proprio')
        # hebergement.heb_desactivation_alloch = self.request.get('heb_desactivation_alloch')
        proprio.pro_date_in = self.request.get('fpro_date_in')
        proprio.pro_date_out = self.request.get('fpro_date_out')
        proprio.pro_motif_out = self.request.get('fpro_motif_out')
        proprio.pro_justif_out = self.request.get('fpro_justif_out')
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        session.add(proprio)
        return u'La modification a été effectuée'

        # query est un select donc update??

        # import pdb; pdb.set_trace()

    def proprio(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        pro_pk = self.request.get('fpro_pk')
        query = session.query(Proprio).filter(Proprio.pro_pk == pro_pk)
        results = query.first()
        return results
