# -*- coding: utf-8 -*-

from z3c.sqlalchemy import getSAWrapper
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from gites.gdwadmin.table.metadata import MetadataTable
from gites.db.content import Metadata


class MetadataView(BrowserView):
    """
    Metadatas edition view
    """

    def getTable(self):
        """
        Returns the render of the table
        """
        table = MetadataTable(self.context, self.request)
        table.update()
        return table.render()

    def getValuesForIndexAndPk(self, index, pk=None):
        """
        """
        form = self.request.form
        keys = ['met_titre_fr',
                'met_titre_en',
                'met_titre_nl',
                'met_titre_it',
                'met_titre_de']
        results = {}
        for key in keys:
            results[key] = form.get(key)[index]
        # if pk is None (for new metadata), filterable should always be False
        results['met_filterable'] = form.get("filterable-%s" % pk, False)
        return results

    def updateMetadata(self):
        """
        Updates metadatas
        """
        pu = getToolByName(self.context, 'plone_utils')
        pks = self.request.form.get('met_pk')
        titles = self.request.form.get('met_titre_fr')

        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        metadataTable = wrapper.getMapper('metadata')
        query = session.query(metadataTable)

        for idx in range(0, len(titles)):
            pk = None
            metadata = Metadata()

            if idx < len(pks):
                # existing metadata needs to be changed
                pk = pks[idx]
                metadata = query.get(pk)

            for key, value in self.getValuesForIndexAndPk(idx, pk).items():
                setattr(metadata, key, value)

            if not metadata.met_id:
                metadata.met_id = pu.normalizeString(metadata.met_titre_fr)

            session.add(metadata)

        session.flush()

        cible = "%s/@@metadataEdition" % (self.context.portal_url())
        self.request.response.redirect(cible)
        return ''
