# -*- coding: utf-8 -*-

from z3c.sqlalchemy import getSAWrapper
from Products.Five.browser import BrowserView


class HebCriteriaView(BrowserView):
    """
    Hebs criteria values edition view
    """

    def getCriteriasValueForHeb(self, hebPk):
        """
        """
        if not hebPk:
            return []
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        linkHebMetadataTable = wrapper.getMapper('link_hebergement_metadata')
        metadataTable = wrapper.getMapper('metadata')
        query = session.query(linkHebMetadataTable).join('metadata')
        query = query.filter(linkHebMetadataTable.heb_fk == hebPk)
        query = query.order_by(metadataTable.met_titre_fr)
        return query.all()

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
            link.link_met_value = str(link.link_met_pk) in form
            session.add(link)

        session.flush()

        cible = "%s/@@hebCriteriaEdition?pk=%s" % (self.context.portal_url(),
                                                   hebPk)
        self.request.response.redirect(cible)
        return ''
