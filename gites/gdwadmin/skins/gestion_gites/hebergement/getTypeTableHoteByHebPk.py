## Script (Python) "getTypeTableHoteByHebPk"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=heb_pk
##title=
##
# récupération de tous les types de table d'hôtes de l'hébergement dont on passe la heb_k en paramètre

tablesHoteHebergement=context.admin_base.table_hote.zsql_table_hote_select_by_hebpk(heb_pk=heb_pk)


typeTableHoteForHeb=[]
for table in tablesHoteHebergement:
    typeTableHoteForHeb.append(table.hebhot_tabho_fk)


return typeTableHoteForHeb
