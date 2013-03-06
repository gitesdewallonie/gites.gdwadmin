## Script (Python) "log_activite"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=log_heb_fk, log_info
##title=
##
#
#log_heb_fk=context.REQUEST.log_heb_fk
#log_info=context.REQUEST.log_info


login=context.REQUEST.AUTHENTICATED_USER.getUserName()


context.admin_base.log_employe.log_employe_insert(login=login,
                                                  log_heb_fk=log_heb_fk,
                                                  log_info=log_info)
