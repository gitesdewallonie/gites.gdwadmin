## Script (Python) "getIconeNbreEpis"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=heb_pk
##title=
##
#
# table link_hebergement_epis
# certain hebergement peuvent avoir plusieurs nombre d'épis différents
# car plusieurs batiment ou plusieurs chambre sous le même ID
#
# ce script extrait les epis et retourne une liste
#

nbreEpis=context.admin_base.hebergement.zsql_nbre_epis_select_by_heb_pk(heb_pk=heb_pk)

epis=''
c=1

for elem in nbreEpis:
   nbre=int(elem.heb_nombre_epis)
   for i in range(nbre):
     if elem.heb_typeheb_fk in (5,6):
        epis=epis + '<img src="images/1_clef.png">'
     else:
        epis=epis + '<img src="images/1_epis.gif">'
     if (i+1) == nbre:
        epis=epis+"&nbsp;&nbsp;"

print epis
return printed
