## Script (Python) "changeExclusionAlloCHProprio"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=

proPk = context.REQUEST.fpro_pk

etatExclusion = context.REQUEST.heb_desactivation_alloch
etatExclusion = etatExclusion == "True" and True or False

etatCourant = context.isProprioExcludedFromAlloCH(pro_pk=proPk)

if etatCourant == etatExclusion:
    return

hebergements = context.admin_base.hebergement.zsql_heb_select_alloch_exclusion_by_propk(pro_pk=proPk)

for heb in hebergements:
    hebPk = heb.heb_pk
    context.admin_base.hebergement.zsql_heb_update_alloch_exclusion_by_hebpk(heb_pk=hebPk, heb_desactivation_alloch=etatExclusion)

return
