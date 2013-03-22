# encoding: utf-8
"""
gites.gdwadmin

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

import zope.interface
from five import grok

from gites.gdwadmin.table import hebmetadata


class HebMetadataView(grok.View):
    grok.context(zope.interface.Interface)
    grok.name(u'hebergement-metadata')
    grok.require('zope2.View')

    def get_table(self):
        """ Returns the render of the table """
        table = hebmetadata.HebergementMetadataTable(self.context,
                                                     self.request)
        table.update()
        return table.render()
