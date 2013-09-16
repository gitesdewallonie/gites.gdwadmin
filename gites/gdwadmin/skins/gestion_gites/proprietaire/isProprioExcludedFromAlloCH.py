## Script (Python) "isProprioExcludedFromAlloCH"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=pro_pk
##title=

hebergements = context.admin_base.hebergement.zsql_heb_select_alloch_exclusion_by_propk(pro_pk=pro_pk)

isProprioExcludedFromAlloCH = False

for heb in hebergements:
    if heb.heb_desactivation_alloch:
        isProprioExcludedFromAlloCH = True

return isProprioExcludedFromAlloCH
