# encoding: utf-8
"""
gites.gdwadmin

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

import zope.interface
from five import grok

from gites.gdwadmin.table import hebmetadata, hebmetadataupdate


class HebMetadataView(grok.View):
    grok.context(zope.interface.Interface)
    grok.name(u'hebergement-metadata')
    grok.require('zope2.View')
    grok.template('hebmetadatatable')

    def get_table(self):
        """ Returns the render of the table """
        table = hebmetadata.HebergementMetadataTable(self.context,
                                                     self.request)
        table.update()
        return table.render()


class HebMetadataUpdateView(grok.View):
    grok.context(zope.interface.Interface)
    grok.name(u'hebergement-metadata-update')
    grok.require('gdw.ViewAdmin')
    grok.template('hebmetadatatable')

    def get_table(self):
        """ Returns the render of the table """
        table = hebmetadataupdate.HebergementUpdateMetadataTable(
            self.context, self.request)
        table.update()
        return table.render()
