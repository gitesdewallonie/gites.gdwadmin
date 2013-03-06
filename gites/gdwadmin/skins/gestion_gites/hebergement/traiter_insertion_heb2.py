## Script (Python) "traiter_insertion_heb2"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
fheb_nom=context.REQUEST.fheb_nom
fheb_adresse=context.REQUEST.fheb_adresse
fheb_code_cgt=context.REQUEST.fheb_code_cgt
fheb_cgt_cap_min=context.REQUEST.fheb_cgt_cap_min
fheb_cgt_cap_max=context.REQUEST.fheb_cgt_cap_max
fheb_cgt_nbre_chmbre=context.REQUEST.fheb_cgt_nbre_chmbre


fheb_com_fk=context.REQUEST.fheb_com_fk
fheb_cgt_fk=context.REQUEST.fheb_cgt_fk
fheb_typeheb_fk=context.REQUEST.fheb_typeheb_fk
fheb_pro_fk=context.REQUEST.fheb_pro_fk
fheb_date_creation = DateTime()
fheb_employe_creation = context.REQUEST.fheb_employe_creation

charge_pk=2

typeHeb=''
comIns=''

dataTypeHeb=context.admin_base.type_heb.zsql_select_type_heb_typehebpk(type_heb_pk=context.REQUEST.fheb_typeheb_fk)
for elem in dataTypeHeb:
   typeHeb=elem.type_heb_code  

dataCommune=context.admin_base.commune.zsql_select_commune_compk(fcom_pk=context.REQUEST.fheb_com_fk)
for elem in dataCommune:
   comIns=elem.com_ins



gdw=context.generer_code_gdw(typeHeb,comIns)


context.admin_base.hebergement.zsql_insert_heb(GDW=gdw, \
                                               fheb_nom=fheb_nom, \
                                               fheb_adresse=fheb_adresse, \
                                               fheb_code_cgt=fheb_code_cgt, \
                                               fheb_cgt_cap_min=fheb_cgt_cap_min, \
                                               fheb_cgt_cap_max=fheb_cgt_cap_max, \
                                               fheb_cgt_nbre_chmbre=fheb_cgt_nbre_chmbre, \
                                               fheb_com_fk=fheb_com_fk, \
                                               fheb_cgt_fk=fheb_cgt_fk, \
                                               fheb_typeheb_fk=fheb_typeheb_fk, \
                                               fheb_date_creation = fheb_date_creation, \
                                               fheb_employe_creation = fheb_employe_creation, \
                                               fheb_site_public='0', \
                                               fheb_charge_fk= charge_pk, \
                                               fheb_pro_fk=fheb_pro_fk)


return context.REQUEST.RESPONSE.redirect('liste_non_actif?code_gdw='+gdw)
