# -*- coding: utf-8 -*-

#-----------------------------
#type d'hegergement | chiffre de la province | arrondissement | commune | chiffre incremente^M
#     2lettres                  1chiffre           1chiffre    3chiffres        4chiffres^M
#         |         -----------------------------------------------------
#         |                                   |
# gr mt ch gf cf mv mm              code ins de la commune


from os import chdir
from datetime import datetime
from z3c.sqlalchemy import getSAWrapper
from Products.Five.browser import BrowserView

dir_gdw = "/home/gdw"


def lire_compteur_gdw():
    chdir(dir_gdw)
    gdw_file = open('compteur_gdw.ame', 'r')
    compteur = gdw_file.readlines()
    gdw_file.close()
    return compteur


def ecrire_compteur_gdw(compteur):
    chdir(dir_gdw)
    gdw_file = open('compteur_gdw.ame', 'w')
    gdw_file.write(compteur)
    gdw_file.close()


def generer_code_gdw(heb, ins):
    compteur = lire_compteur_gdw()
    compteur = int(compteur[0]) + 1
    print compteur
    ecrire_compteur_gdw(str(compteur))
    gdw = heb + str(ins) + str(compteur)
    return gdw


class UtilsView(BrowserView):
    """
    """

    def generer_code_gdw(self, heb, ins):
        return generer_code_gdw(heb, ins)

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
                                 pro_url=fields.get('fpro_url'),
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
