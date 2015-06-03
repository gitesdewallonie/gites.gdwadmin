# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from datetime import datetime
from gites.db.content.proprio.proprio import Proprio


class AddProprio(BrowserView):
    # @property
    # def pro_pk(self):
    #     return self.request.get('fpro_pk')

    def add_proprio(self):

        proprio = Proprio()
        proprio.pro_nom1 = self.request.get('fpro_nom1')
        proprio.pro_civ_fk = self.request.get('fpro_civ_fk')
        proprio.pro_nom1 = self.request.get('fpro_nom1')
        proprio.pro_prenom1 = self.request.get('fpro_prenom1')
        proprio.pro_nom2 = self.request.get('fpro_nom2')
        proprio.pro_prenom2 = self.request.get('fpro_prenom2')
        proprio.pro_societe = self.request.get('fpro_societe')
        proprio.pro_adresse = self.request.get('fpro_adresse')
        proprio.pro_com_fk = self.request.get('fpro_com_fk')
        proprio.pro_email = self.request.get('fpro_email')
        proprio.pro_tel_priv = self.request.get('fpro_tel_priv')
        proprio.pro_tel_bur = self.request.get('fpro_tel_bur')
        proprio.pro_fax_priv = self.request.get('fpro_fax_priv')
        proprio.pro_fax_bur = self.request.get('fpro_fax_bur')
        proprio.pro_gsm1 = self.request.get('fpro_gsm1')
        proprio.pro_gsm2 = self.request.get('fpro_gsm2')
        proprio.pro_tva = self.request.get('fpro_tva')
        proprio.pro_langue = self.request.get('fpro_langue')
        # XXX proprio.pro_pass = self.request.get('fpro_pass')
        proprio.pro_etat = self.request.get('fpro_etat')


        # XXX Faut-il ajouter ces champs suivants dans le formulaire ?
        # proprio.pro_date_in = self.request.get('fpro_date_in')
        # proprio.pro_date_out = self.request.get('fpro_date_out')
        # proprio.pro_motif_out = self.request.get('fpro_motif_out')
        # proprio.pro_justif_out = self.request.get('fpro_justif_out')
        proprio.pro_etat = self.request.get('fpro_etat')
        proprio.pro_employe_creation = self.request.get('fpro_employe_creation')
        proprio.pro_date_creation = datetime.now()

        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        session.add(proprio)
        return u'Le propriétaire a été ajouté'

