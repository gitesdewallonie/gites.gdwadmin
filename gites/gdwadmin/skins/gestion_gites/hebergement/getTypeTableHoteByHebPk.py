## Script (Python) "getTypeTableHoteByHebPk"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=heb_pk
##title=
##
# r�cup�ration de tous les types de table d'h�tes de l'h�bergement dont on passe la heb_k en param�tre

tablesHoteHebergement=context.admin_base.table_hote.zsql_table_hote_select_by_hebpk(heb_pk=heb_pk)


typeTableHoteForHeb=[]
for table in tablesHoteHebergement:
    typeTableHoteForHeb.append(table.hebhot_tabho_fk)


return typeTableHoteForHeb
