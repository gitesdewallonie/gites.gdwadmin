## Script (Python) "getTypeTableHoteMajByHebPk"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=heb_pk
##title=
##
# récupération de tous les types de table d'hôtes de l'hébergement dont on passe la heb_k en paramètre

tablesHoteHebergementMaj=context.admin_base.table_hote.zsql_table_hote_maj_select_by_hebpk(heb_pk=heb_pk)


typeTableHoteMajForHeb=[]
for table in tablesHoteHebergementMaj:
    typeTableHoteMajForHeb.append(table.hebhot_maj_tabho_fk)


return typeTableHoteMajForHeb
