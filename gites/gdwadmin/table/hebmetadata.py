# encoding: utf-8
"""
gites.gdwadmin

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

import sqlalchemy as sa

import zope.component
import zope.interface
import zope.publisher
import z3c.table
from five import grok

from gites.db import content as mappers, session
from gites.gdwadmin.table import interfaces


class HebergementMetadataTable(z3c.table.table.Table):
    zope.interface.implements(interfaces.IHebergementMetadataTable)

    cssClasses = {'table': 'z3c-listing percent100 listing nosort'}
    cssClassEven = u'odd'
    cssClassOdd = u'even'
    sortOn = 'table-number-0'
    startBatchingAt = 9999

    @property
    def values(self):
        """ Returns the values for an hosting """
        adapter = zope.component.getMultiAdapter(
            (self.context, self.request, self), z3c.table.interfaces.IValues)
        return adapter.values


class HebergementMetadataValues(z3c.table.value.ValuesMixin,
                                grok.MultiAdapter):
    grok.provides(z3c.table.interfaces.IValues)
    grok.adapts(zope.interface.Interface,
                zope.publisher.interfaces.browser.IBrowserRequest,
                interfaces.IHebergementMetadataTable)

    @property
    def values(self):
        heb_pk = self.request.get('heb_pk')
        query = session().query(mappers.LinkHebergementMetadata)
        query = query.join('metadata_info', 'type')
        query = query.filter(mappers.LinkHebergementMetadata.heb_fk == heb_pk)
        query = query.order_by(mappers.Metadata.metadata_type_id)

        query_base = query.filter(sa.and_(
            sa.not_(mappers.Metadata.met_id.in_(['heb_animal'])),
            mappers.LinkHebergementMetadata.link_met_value == True))
        base = query_base.all()

        query_specials = query.filter(
            mappers.Metadata.met_id.in_(['heb_animal']))
        base.extend(query_specials.all())
        return base


class HebMetadataType(z3c.table.column.GetAttrColumn, grok.MultiAdapter):
    grok.provides(z3c.table.interfaces.IColumn)
    grok.name('heb_metadata_type')
    grok.adapts(zope.interface.Interface,
                zope.interface.Interface,
                interfaces.IHebergementMetadataTable)

    header = u'Catégorie'
    cssClasses = {'td': 'center'}
    weight = 0

    def renderCell(self, item):
        return item.metadata_info.type.met_typ_titre


class HebMetadataIcon(z3c.table.column.GetAttrColumn, grok.MultiAdapter):
    grok.provides(z3c.table.interfaces.IColumn)
    grok.name('heb_metadata_icon')
    grok.adapts(zope.interface.Interface,
                zope.interface.Interface,
                interfaces.IHebergementMetadataTable)

    header = u''
    cssClasses = {'td': 'center'}
    weight = 10

    def renderCell(self, item):
        metadata_id = item.metadata_info.met_id
        if item.link_met_value is False:
            metadata_id = '%s_off' % metadata_id
        return u'<img src="%(id)s.png" alt="%(title)s" title="%(title)s" />' % {
            'id': metadata_id,
            'title': item.metadata_info.met_titre_fr}


class HebMetadataDescription(z3c.table.column.GetAttrColumn,
                             grok.MultiAdapter):
    grok.provides(z3c.table.interfaces.IColumn)
    grok.name('heb_metadata_description')
    grok.adapts(zope.interface.Interface,
                zope.interface.Interface,
                interfaces.IHebergementMetadataTable)

    header = u'Description'
    cssClasses = {'td': 'center'}
    weight = 20

    def renderCell(self, item):
        return item.metadata_info.met_titre_fr
