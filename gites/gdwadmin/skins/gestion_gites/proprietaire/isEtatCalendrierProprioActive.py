## Script (Python) "isEtatCalendrierProprioActive"
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
# table hebergement
# selectionne les hebergement d'un prorio et check l'etet du calendrier 
#

hebergements = context.admin_base.hebergement.zsql_heb_select_hebcalendar_by_propk(pro_pk=pro_pk)

etatCalendrierProprioActive = True

for heb in hebergements:
    if heb.heb_calendrier_proprio == 'bloque':
        etatCalendrierProprioActive = False

return etatCalendrierProprioActive
