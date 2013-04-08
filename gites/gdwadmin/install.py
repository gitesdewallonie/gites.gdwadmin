# encoding: utf-8
"""
gites.gdwadmin

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from Products.CMFCore.utils import getToolByName
from plone import api


def setup(context):
    if context.readDataFile('gites.gdwadmin_various.txt') is None:
        return
    # Setup the permission for gdwadmin views
    portal_skins = getToolByName(api.portal.get(), 'portal_skins')
    gestion_gites = getattr(portal_skins, 'gestion_gites')
    gestion_gites.__ac_local_roles_block__ = True
    gestion_gites.manage_permission('View', ('Site Administrator', 'Manager'))
    gestion_gites.reindexObjectSecurity()
