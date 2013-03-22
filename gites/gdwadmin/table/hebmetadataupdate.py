# encoding: utf-8
"""
gites.gdwadmin

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

import zope.component
import zope.interface
import zope.publisher
import z3c.table
from five import grok

from gites.db import content as mappers
from gites.gdwadmin.table import interfaces


class HebergementUpdateMetadataTable(z3c.table.table.Table):
    zope.interface.implements(interfaces.IHebergementUpdateMetadataTable)

    cssClasses = {'table': 'z3c-listing percent100 listing nosort'}
    cssClassEven = u'odd'
    cssClassOdd = u'even'
    sortOn = 'table-number-0'

    @property
    def values(self):
        """ Returns the values for an hosting """
        adapter = zope.component.getMultiAdapter(
            (self.context, self.request, self), z3c.table.interfaces.IValues)
        return adapter.values


class HebergementUpdateMetadataValues(z3c.table.value.ValuesMixin,
                                grok.MultiAdapter):
    grok.provides(z3c.table.interfaces.IValues)
    grok.adapts(zope.interface.Interface,
                zope.publisher.interfaces.browser.IBrowserRequest,
                interfaces.IHebergementUpdateMetadataTable)

    @property
    def values(self):
        heb_pk = self.request.get('heb_pk')
        return mappers.LinkHebergementMetadataUpdate.get_updates(heb_pk)


class HebMetadataUpdateType(z3c.table.column.GetAttrColumn, grok.MultiAdapter):
    grok.provides(z3c.table.interfaces.IColumn)
    grok.name('heb_metadata_update_type')
    grok.adapts(zope.interface.Interface,
                zope.interface.Interface,
                interfaces.IHebergementUpdateMetadataTable)

    header = u'Catégorie'
    cssClasses = {'td': 'center'}
    weight = 0

    def renderCell(self, item):
        return item.metadata_info.type.met_typ_titre


class HebMetadataUpdateIcon(z3c.table.column.GetAttrColumn, grok.MultiAdapter):
    grok.provides(z3c.table.interfaces.IColumn)
    grok.name('heb_metadata_icon')
    grok.adapts(zope.interface.Interface,
                zope.interface.Interface,
                interfaces.IHebergementUpdateMetadataTable)

    header = u''
    cssClasses = {'td': 'center'}
    weight = 10

    def renderCell(self, item):
        return u'<img src="%(id)s" alt="%(title)s" title="%(title)s" />' % {
            'id': item.metadata_info.met_id,
            'title': item.metadata_info.met_titre_fr}


class HebMetadataUpdateDescription(z3c.table.column.GetAttrColumn,
                                   grok.MultiAdapter):
    grok.provides(z3c.table.interfaces.IColumn)
    grok.name('heb_metadata_update_description')
    grok.adapts(zope.interface.Interface,
                zope.interface.Interface,
                interfaces.IHebergementUpdateMetadataTable)

    header = u'Description'
    cssClasses = {'td': 'center'}
    weight = 20

    def renderCell(self, item):
        return item.metadata_info.met_titre_fr


class HebMetadataUpdateActualValue(z3c.table.column.GetAttrColumn,
                                   grok.MultiAdapter):
    grok.provides(z3c.table.interfaces.IColumn)
    grok.name('heb_metadata_update_actual_value')
    grok.adapts(zope.interface.Interface,
                zope.interface.Interface,
                interfaces.IHebergementUpdateMetadataTable)

    header = u'Valeur actuelle'
    cssClasses = {'td': 'center'}
    weight = 30

    def renderCell(self, item):
        return [u'oui', u'non'][int(item.link_metadata.link_met_value)]


class HebMetadataUpdateNewValue(z3c.table.column.GetAttrColumn,
                                   grok.MultiAdapter):
    grok.provides(z3c.table.interfaces.IColumn)
    grok.name('heb_metadata_update_new_value')
    grok.adapts(zope.interface.Interface,
                zope.interface.Interface,
                interfaces.IHebergementUpdateMetadataTable)

    header = u'Nouvelle valeur'
    cssClasses = {'td': 'center'}
    weight = 40

    def renderCell(self, item):
        return [u'oui', u'non'][int(item.link_met_value)]
