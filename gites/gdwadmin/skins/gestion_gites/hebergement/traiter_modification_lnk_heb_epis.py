## Script (Python) "traiter_modification_lnk_heb_epis"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=heb_pk, heb_nombre_epis
##title=
##
#
# appelle par "traiter_modification_heb"  
# table link_hebergement_epis
# a chaque modification d'un hebergement on delete dans cette table toutes les entrees
# et ensuite on reinsere avec les nouvelles donnes.
#

context.admin_base.hebergement.zsql_lnk_heb_nbre_epis_delete(heb_pk=heb_pk)




for nbreEpis in heb_nombre_epis:
     context.admin_base.hebergement.zsql_lnk_heb_nbre_epis_insert(heb_pk=heb_pk, \
                                                                  heb_nombre_epis=nbreEpis)
