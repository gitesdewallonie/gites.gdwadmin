## Script (Python) "modificaton_proprio"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##title=
##
#
# appelle par "traiter_modification_proprio"
# table proprio
# mise à jour des infos proprio par validation des données
#
from DateTime import DateTime


fpro_pk=context.REQUEST.fpro_pk
fpro_nom1=context.REQUEST.fpro_nom1
fpro_nom2=context.REQUEST.fpro_nom2
fpro_prenom1=context.REQUEST.fpro_prenom1
fpro_prenom2=context.REQUEST.fpro_prenom2
fpro_societe=context.REQUEST.fpro_societe
fpro_adresse=context.REQUEST.fpro_adresse
fpro_cp =context.REQUEST.fpro_cp
fpro_email =context.REQUEST.fpro_email
fpro_tel_priv =context.REQUEST.fpro_tel_priv
fpro_tel_bur =context.REQUEST.fpro_tel_bur
fpro_fax_priv =context.REQUEST.fpro_fax_priv
fpro_fax_bur =context.REQUEST.fpro_fax_bur
fpro_gsm1 =context.REQUEST.fpro_gsm1
fpro_gsm2 =context.REQUEST.fpro_gsm2
fpro_tva =context.REQUEST.fpro_tva
fpro_langue =context.REQUEST.fpro_langue
fpro_date_naiss =context.REQUEST.fpro_date_naiss
fpro_etat =context.REQUEST.fpro_etat
fpro_motif_out =context.REQUEST.fpro_motif_out
fpro_justif_out =context.REQUEST.fpro_justif_out
fpro_date_in =context.REQUEST.fpro_date_in
fpro_date_out =context.REQUEST.fpro_date_out
fpro_log =context.REQUEST.fpro_log
fpro_pass =context.REQUEST.fpro_pass
fpro_employe_modification =context.REQUEST.fpro_employe_modification
fpro_date_modification = DateTime()
fpro_civ_fk=context.REQUEST.fpro_civ_fk

if fpro_log == '':
      fpro_log = None
else :
      fpro_log = fpro_log

if fpro_pass == '':
      fpro_pass = None
else :
      fpro_pass = fpro_pass



# update des donnes du proprio dans la table proprio
# etat de maj-info du proprio repasse à confirmé
context.admin_base.proprio.zsql_proprio_update(fpro_pk=fpro_pk,\
                                                 fpro_nom1=fpro_nom1,\
                                                 fpro_nom2=fpro_nom2,\
                                                 fpro_prenom1=fpro_prenom1,\
                                                 fpro_prenom2=fpro_prenom2,\
                                                 fpro_societe=fpro_societe,\
                                                 fpro_adresse=fpro_adresse,\
                                                 fpro_cp=fpro_cp,\
                                                 fpro_email=fpro_email,\
                                                 fpro_tel_priv=fpro_tel_priv,\
                                                 fpro_tel_bur=fpro_tel_bur,\
                                                 fpro_fax_priv=fpro_fax_priv,\
                                                 fpro_fax_bur=fpro_fax_bur,\
                                                 fpro_gsm1=fpro_gsm1,\
                                                 fpro_gsm2=fpro_gsm2,\
                                                 fpro_tva=fpro_tva,\
                                                 fpro_langue=fpro_langue, \
                                                 fpro_date_naiss=fpro_date_naiss or None,\
                                                 fpro_etat=fpro_etat,\
                                                 fpro_motif_out=fpro_motif_out,\
                                                 fpro_justif_out=fpro_justif_out,\
                                                 fpro_date_in=fpro_date_in,\
                                                 fpro_date_out=fpro_date_out,\
                                                 fpro_log=fpro_log,\
                                                 fpro_pass=fpro_pass,\
                                                 fpro_employe_modification=fpro_employe_modification,\
                                                 fpro_date_modification=fpro_date_modification,\
                                                 fpro_civ_fk=fpro_civ_fk,\
                                                 )


#retour sur la page qui liste les proprio en attente de confirmation
return context.REQUEST.RESPONSE.redirect('liste_actif')
