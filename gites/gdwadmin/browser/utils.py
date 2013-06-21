# -*- coding: utf-8 -*-

#-----------------------------
#type d'hegergement | chiffre de la province | arrondissement | commune | chiffre incremente^M
#     2lettres                  1chiffre           1chiffre    3chiffres        4chiffres^M
#         |         -----------------------------------------------------
#         |                                   |
# gr mt ch gf cf mv mm              code ins de la commune


from os import chdir
from Products.Five.browser import BrowserView

dir_gdw = "/Users/laurent/Desktop"


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
