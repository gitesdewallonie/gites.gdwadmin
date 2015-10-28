## Script (Python) "valider_maj_info_proprio"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=pro_pk
##title=
##
#
# appelle par "form_valider_maj_proprio_info"  
# table proprio
# mise à jour des infos proprio par validation des données 
#

pro_nom1=context.REQUEST.pro_nom1
pro_nom2=context.REQUEST.pro_nom2
pro_prenom1=context.REQUEST.pro_prenom1
pro_prenom2=context.REQUEST.pro_prenom2
pro_societe=context.REQUEST.pro_societe
pro_adresse=context.REQUEST.pro_adresse
pro_email=context.REQUEST.pro_email
pro_tel_priv=context.REQUEST.pro_tel_priv
pro_fax_priv=context.REQUEST.pro_fax_priv
pro_gsm1=context.REQUEST.pro_gsm1
pro_langue=context.REQUEST.pro_langue
pro_tva=context.REQUEST.pro_tva
pro_date_naiss=context.REQUEST.pro_date_naiss
pro_maj_info_etat=context.REQUEST.pro_maj_info_etat
pro_com_fk=context.REQUEST.pro_com_fk
pro_civ_fk=context.REQUEST.pro_civ_fk
pro_maj_pk=context.REQUEST.pro_maj_pk



# update des donnes du proprio dans la table proprio
# etat de maj-info du proprio repasse à confirmé
context.admin_base.proprio.zsql_proprio_update_with_maj_info(pro_pk=pro_pk,\
                                                             pro_nom1=pro_nom1,\
                                                             pro_nom2=pro_nom2,\
                                                             pro_prenom1=pro_prenom1,\
                                                             pro_prenom2=pro_prenom2,\
                                                             pro_societe=pro_societe,\
                                                             pro_adresse=pro_adresse,\
                                                             pro_email=pro_email,\
                                                             pro_tel_priv=pro_tel_priv,\
                                                             pro_fax_priv=pro_fax_priv,\
                                                             pro_gsm1=pro_gsm1,\
                                                             pro_langue=pro_langue,\
                                                             pro_tva=pro_tva, \
                                                             pro_date_naiss=pro_date_naiss,\
                                                             pro_maj_info_etat=pro_maj_info_etat,\
                                                             pro_com_fk=pro_com_fk,\
                                                             pro_civ_fk=pro_civ_fk)


#suppression des infos de maj dans la table proprio_maj
context.admin_base.proprio.zsql_maj_proprio_delete_by_pro_maj_pk(pro_maj_pk=pro_maj_pk)

#retour sur la page qui liste les proprio en attente de confirmation
return context.REQUEST.RESPONSE.redirect('listing_maj_proprio_info')
