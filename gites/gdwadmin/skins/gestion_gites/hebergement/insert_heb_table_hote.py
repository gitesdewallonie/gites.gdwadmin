## Script (Python) "insert_heb_table_hote"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=heb_pk, hebhot_tabho_fk
##title=
##
# insertion dans la table de jointure heb_tab_hote
# de la clé de l'hebergement et de la clé du type de table d'hote
# un hébergement peut avoir plusieurs type de table
#
# voir 
#   table hebergement heb_pk
#   table table_hote  tabho_pk

heb_pk=int(heb_pk)


# SI il y a un type de table d'hote coché,
#   je détruis toutes les infos qui se rapportent à cet hébergement
#   j'insère les nouvelles infos
# SINON
#   je détruis toutes les infos liées à cet hébergement

if hebhot_tabho_fk > -1:
   context.admin_base.table_hote.zsql_heb_tab_hote_delete(hebhot_heb_fk=heb_pk)
   for elem in hebhot_tabho_fk:
      context.admin_base.table_hote.zsql_heb_tab_hote_insert(hebhot_heb_fk=heb_pk, hebhot_tabho_fk=elem)
else:
   context.admin_base.table_hote.zsql_heb_tab_hote_delete(hebhot_heb_fk=heb_pk)
