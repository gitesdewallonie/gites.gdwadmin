# -*- coding: utf-8 -*-

from sqlalchemy.sql import not_
from z3c.sqlalchemy import getSAWrapper
from Products.Five.browser import BrowserView

from gites.db.content.hebergement.hebergement import Hebergement


class HebCriteriaView(BrowserView):
    """
    Hebs criteria values edition view
    """

    @property
    def hebergement(self):
        """ Returns the heb """
        return Hebergement.first(heb_pk=self.request.get('pk'))

    def getCriteriasValueForHeb(self, hebPk):
        """
        """
        if not hebPk:
            return []
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        linkHebMetadataTable = wrapper.getMapper('link_hebergement_metadata')
        metadataTable = wrapper.getMapper('metadata')
        query = session.query(linkHebMetadataTable).join('metadata_info')
        query = query.filter(linkHebMetadataTable.heb_fk == hebPk)
        query = query.order_by(metadataTable.met_titre_fr)

        heb_metadata = query.all()

        query = session.query(metadataTable)
        query = query.filter(not_(metadataTable.met_pk.in_(
            [m.metadata_fk for m in heb_metadata])))
        query = query.order_by(metadataTable.met_titre_fr)
        for metadata in query.all():
            criterion = type('criterion', (object, ), {
                'heb_fk': hebPk,
                'metadata_fk': metadata.met_pk,
                'link_met_value': None,
                'metadata_info': metadata})()
            heb_metadata.append(criterion)
        heb_metadata.sort(key=lambda x: x.metadata_info.met_titre_fr)
        return heb_metadata

    def updateHebCriteria(self):
        """
        Updates criteria values for heb
        """
        form = self.request.form
        hebPk = form.get('hebPk')

        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        linkHebMetadataTable = wrapper.getMapper('link_hebergement_metadata')
        query = session.query(linkHebMetadataTable)
        query = query.filter(linkHebMetadataTable.heb_fk == hebPk)
        links = query.all()

        for link in links:
            link.link_met_value = str(link.metadata_fk) in form
            session.add(link)
        # Inserts the new links that are not defined in the existing links list
        for met_pk in [i for i in form.get('metadata_fk') if int(i) not in \
                       [l.metadata_fk for l in links]]:
            link = linkHebMetadataTable()
            link.heb_fk = hebPk
            link.metadata_fk = met_pk
            link.link_met_value = str(link.metadata_fk) in form
            session.add(link)

        session.flush()

        cible = "%s/@@hebCriteriaEdition?pk=%s" % (self.context.portal_url(),
                                                   hebPk)
        self.request.response.redirect(cible)
        return ''
