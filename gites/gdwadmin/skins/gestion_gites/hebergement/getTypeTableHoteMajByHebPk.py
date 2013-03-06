## Script (Python) "getTypeTableHoteMajByHebPk"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=heb_pk
##title=
##
# r�cup�ration de tous les types de table d'h�tes de l'h�bergement dont on passe la heb_k en param�tre

tablesHoteHebergementMaj=context.admin_base.table_hote.zsql_table_hote_maj_select_by_hebpk(heb_pk=heb_pk)


typeTableHoteMajForHeb=[]
for table in tablesHoteHebergementMaj:
    typeTableHoteMajForHeb.append(table.hebhot_maj_tabho_fk)


return typeTableHoteMajForHeb
