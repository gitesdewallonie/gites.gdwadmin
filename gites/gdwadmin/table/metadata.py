# encoding: utf-8

from five import grok
from zope.interface import implements, Interface
from zope.component import getMultiAdapter
from zope.publisher.interfaces.browser import IBrowserRequest

from z3c.sqlalchemy import getSAWrapper
from z3c.table import column
from z3c.table.interfaces import IColumn, IValues
from z3c.table.table import Table
from z3c.table.value import ValuesMixin

from gites.gdwadmin.table.interfaces import IMetadataTable


class MetadataTable(Table):
    implements(IMetadataTable)

    cssClasses = {'table': 'z3c-listing percent100 listing nosort'}
    cssClassEven = u'odd'
    cssClassOdd = u'even'
    sortOn = 'table-number-0'

    @property
    def values(self):
        adapter = getMultiAdapter((self.context, self.request, self), IValues)
        return adapter.values


class MetadataValues(ValuesMixin, grok.MultiAdapter):
    grok.provides(IValues)
    grok.adapts(Interface, IBrowserRequest, IMetadataTable)

    @property
    def values(self):
        """
        Return metadata values
        """
        wrapper = getSAWrapper('gites_wallons')
        metadataTable = wrapper.getMapper('metadata')
        query = wrapper.session.query(metadataTable)
        query = query.order_by(metadataTable.metadata_type_id).order_by(
            metadataTable.met_titre_fr)
        return query.all()


class MetadataType(column.GetAttrColumn, grok.MultiAdapter):
    grok.provides(IColumn)
    grok.name('metadata_type')
    grok.adapts(Interface, Interface, IMetadataTable)

    header = u'Catégorie'
    cssClasses = {'td': 'center'}
    weight = 0

    def get_types(self):
        wrapper = getSAWrapper('gites_wallons')
        metadataTypeTable = wrapper.getMapper('metadata_type')
        return wrapper.session.query(metadataTypeTable).all()

    def renderCell(self, item):
        value = item.type.met_typ_id
        types = []
        for type in self.get_types():
            types.append(u'<option value="%s" %s>%s</option>' % (
                type.met_typ_id,
                type.met_typ_id == value and 'selected="selected"' or '',
                type.met_typ_titre))
        return u'<select name="metadata_type_id">%s</select>' % ''.join(types)

    def getSortKey(self, item):
        return item.type.met_typ_id


class TitreColumn(column.GetAttrColumn):
    """
    Base class for titre columns
    """
    grok.provides(IColumn)
    grok.adapts(Interface, Interface, IMetadataTable)
    cssClasses = {'td': 'center'}

    def renderCell(self, item):
        return u'''<input type="text" name="%s:list" value="%s" required />
                ''' % (self.attrName, getattr(item, self.attrName))


class TitreFR(TitreColumn, grok.MultiAdapter):
    grok.name('titre_fr')
    header = u'Titre (FR)'
    attrName = 'met_titre_fr'
    weight = 10


class TitreEN(TitreColumn, grok.MultiAdapter):
    grok.name('titre_en')
    header = u'Titre (EN)'
    attrName = 'met_titre_en'
    cssClasses = {'td': 'center'}
    weight = 20


class TitreNL(TitreColumn, grok.MultiAdapter):
    grok.name('titre_nl')
    header = u'Titre (NL)'
    attrName = 'met_titre_nl'
    cssClasses = {'td': 'center'}
    weight = 30


class TitreIT(TitreColumn, grok.MultiAdapter):
    grok.name('titre_it')
    header = u'Titre (IT)'
    attrName = 'met_titre_it'
    cssClasses = {'td': 'center'}
    weight = 40


class TitreDE(TitreColumn, grok.MultiAdapter):
    grok.name('titre_de')
    header = u'Titre (DE)'
    attrName = 'met_titre_de'
    cssClasses = {'td': 'center'}
    weight = 50


class Filterable(column.GetAttrColumn, grok.MultiAdapter):
    grok.provides(IColumn)
    grok.name('filterable')
    grok.adapts(Interface, Interface, IMetadataTable)

    header = u'Filtre de recherche'
    attrName = 'met_filterable'
    cssClasses = {'td': 'center'}
    weight = 60

    def renderCell(self, item):
        value = getattr(item, self.attrName, False)
        return u'''
            <input type="checkbox" name="filterable-%s" %s />
            <input type="hidden" name="met_pk:list" value="%s" />
                ''' % (item.met_pk, value and 'checked="CHECKED"' or '',
                       item.met_pk)
