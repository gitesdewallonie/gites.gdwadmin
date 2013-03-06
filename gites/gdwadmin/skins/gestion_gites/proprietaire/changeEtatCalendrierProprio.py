## Script (Python) "changeEtatCalendrierProprio"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
#
# appelle par "traiter_modification_proprio"  
# table hebergement
# selectionne les hebergement d'un prorio et update l'etat du calendrier 
#

proPk = context.REQUEST.fpro_pk

etatCalendrier = context.REQUEST.heb_calendrier_proprio
etatCourant = context.isEtatCalendrierProprioActive(pro_pk=proPk)
hebergements = context.admin_base.hebergement.zsql_heb_select_hebcalendar_by_propk(pro_pk=proPk)

for heb in hebergements:
    hebPk=heb.heb_pk
    context.admin_base.hebergement.zsql_heb_update_hebcalendar_by_hebpk(heb_pk=hebPk,heb_calendrier_proprio=etatCalendrier)

return
