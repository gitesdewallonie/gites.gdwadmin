## Script (Python) "getTypeTableHote"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=heb_pk
##title=select box
##
# rÃ©cupÃ©ration de tous les types de table d'hÃ´te
type_table_hote=context.admin_base.table_hote.zsql_table_hote_select_all()

# rÃ©cupÃ©ration de tous les types de table d'hÃ´tes de l'hÃ©bergement dont on passe la heb_k en paramÃ¨tre
tableHoteHebergement=context.admin_base.table_hote.zsql_table_hote_select_by_hebpk(heb_pk=heb_pk)


table_hote=[]
heb_table_hote=[]
chaine=""

# construction d'une liste avec les pk des types de table d'hote
# table table_hote
# champ tabho_pk
for elem in type_table_hote:
   table_hote.append((elem.tabho_pk,elem.tabho_type_fr))
#print table_hote

# construction d'une liste avec les fk des types de table d'hote d'un hebergement selon sa pk
# table heb_tab_hote
# champ hebhot_heb_fk >> table hebergement.heb_pk
# champ hebhot_tabho_fk >> table table_hote.tabho_pk
for elem in tableHoteHebergement:
   heb_table_hote.append(elem.hebhot_tabho_fk)
#print heb_table_hote


# crÃ©ation du bloc de input type check
# je parcours de tous les types de table d'hÃ´te
# je teste la prÃ©sence du type de table d'hÃ´te dans la liste des type de table de l'hÃ©bergement
# si l'hebergement possÃ¨de le type alors le input est checked
# sinon c'est un simple input

for elem in table_hote:
   if elem[0] in heb_table_hote:
      txt="""<input type="checkbox" name="hebhot_tabho_fk" value="%s" checked />%s<br />"""%(elem[0], elem[1])
   else:
      txt="""<input type="checkbox" name="hebhot_tabho_fk" value="%s" />%s<br />"""%(elem[0], elem[1])
   chaine=chaine+txt

return chaine
