# -*- coding: utf-8 -*-

from datetime import datetime
from sqlalchemy import and_
from z3c.sqlalchemy import getSAWrapper
from Products.Five.browser import BrowserView


class ProprioView(BrowserView):
    """
    """

    def insertProprio(self):
        fields = self.request.form
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        insertProprio = wrapper.getMapper('proprio')
        newEntry = insertProprio(pro_civ_fk=fields.get('fpro_civ_fk'),
                                 pro_nom1=fields.get('fpro_nom1'),
                                 pro_nom2=fields.get('fpro_nom2'),
                                 pro_prenom1=fields.get('fpro_prenom1'),
                                 pro_prenom2=fields.get('fpro_prenom2'),
                                 pro_societe=fields.get('fpro_societe'),
                                 pro_adresse=fields.get('fpro_adresse'),
                                 pro_email=fields.get('fpro_email'),
                                 pro_tel_priv=fields.get('fpro_tel_priv'),
                                 pro_tel_bur=fields.get('fpro_tel_bur'),
                                 pro_fax_priv=fields.get('fpro_fax_priv'),
                                 pro_fax_bur=fields.get('fpro_fax_bur'),
                                 pro_gsm1=fields.get('fpro_gsm1'),
                                 pro_gsm2=fields.get('fpro_gsm2'),
                                 pro_tva=fields.get('fpro_tva'),
                                 pro_etat=fields.get('fpro_etat'),
                                 pro_employe_creation=fields.get('fpro_employe_creation'),
                                 pro_date_creation=datetime.now(),
                                 pro_com_fk=fields.get('fpro_com_fk'))
        session.add(newEntry)
        session.flush()
        cible = "%s/portal_skins/gestion_gites/proprietaire/liste_actif" % self.context.portal_url()
        self.request.response.redirect(cible)
        return ''

    def canActivateProprio(self, proPk):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        proprioTable = wrapper.getMapper('proprio')
        proprio = session.query(proprioTable).get(proPk)
        login = proprio.pro_log
        query = session.query(proprioTable)
        query = query.filter(and_(proprioTable.pro_log == login,
                                  proprioTable.pro_etat == True,
                                  proprioTable.pro_pk != proPk))
        otherLogins = query.count()
        return (not otherLogins)
