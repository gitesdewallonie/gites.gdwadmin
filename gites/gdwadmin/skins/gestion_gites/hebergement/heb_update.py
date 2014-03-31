## Script (Python) "heb_update"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

fheb_com_fk = context.REQUEST.fheb_com_fk

fheb_pk = context.REQUEST.fheb_pk
fheb_nbre_epis = context.REQUEST.fheb_nbre_epis

if fheb_com_fk == '0':
    return context.REQUEST.RESPONSE.redirect('standard_error_message?error_message="Code postal manquant"')


context.admin_base.hebergement.zsql_heb_update()
context.admin_base.hebergement.zsql_heb_app_update()
context.hebergement.traiter_modification_lnk_heb_epis(heb_pk=fheb_pk, heb_nombre_epis=fheb_nbre_epis)

return context.REQUEST.RESPONSE.redirect('description?fheb_pk=' + fheb_pk)
