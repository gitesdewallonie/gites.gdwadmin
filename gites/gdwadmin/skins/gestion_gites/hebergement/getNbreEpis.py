## Script (Python) "getNbreEpis"
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
# certain hebergement peuvent avoir plusieurs nombre d'epis differents
# car plusieurs batiment ou plusieurs chambre sous le meme ID
#
# ce script extrait les epis et retourne une liste
#

nbreEpis=context.admin_base.hebergement.zsql_nbre_epis_select_by_heb_pk(heb_pk=heb_pk)

if len(nbreEpis)==0:
   epis=0
   print epis
   return printed


epis=''
c=1

for elem in nbreEpis:
   epis=epis+str(elem.heb_nombre_epis)
   if (len(nbreEpis) > 1 and  c < (len(nbreEpis))):
      epis=epis+'    '
   c=c+1

print epis
return printed
