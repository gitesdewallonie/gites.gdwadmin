# -*- coding: utf-8 -*-

from z3c.sqlalchemy import getSAWrapper
from Products.Five.browser import BrowserView
from gites.gdwadmin.table.metadata import MetadataTable


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

    def getValuesForIndexAndPk(self, index, pk):
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
        results['met_filterable'] = form.get("filterable-%s" % pk, False)
        return results

    def updateMetadata(self):
        """
        Updates metadatas
        """
        pks = self.request.form.get('met_pk')

        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        metadataTable = wrapper.getMapper('metadata')
        query = session.query(metadataTable)

        for idx, pk in enumerate(pks):
            metadata = query.get(pks[idx])
            for key, value in self.getValuesForIndexAndPk(idx, pk).items():
                setattr(metadata, key, value)
            session.add(metadata)
        session.flush()

        cible = "%s/@@metadataEdition" % (self.context.portal_url())
        self.request.response.redirect(cible)
        return ''
