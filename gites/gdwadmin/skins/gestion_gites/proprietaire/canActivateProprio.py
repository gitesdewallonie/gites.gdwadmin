## Script (Python) "canActivateProprio"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=pro_pk
##title=

canActivateProprio = context.restrictedTraverse('@@canActivateProprio')
result = canActivateProprio(pro_pk)

return result
