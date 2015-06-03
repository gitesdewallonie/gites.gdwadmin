# -*- coding: utf-8 -*-
# En rajoutant la ligne ci-dessus, on pourra utiliser des caractères particuliers dans
# les commentaires. Cette ligne doit toujours être placée sur la première ligne de code
# il ne peut rien y avoir avant.

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.province import Province


class ModifProvince(BrowserView):

    @property
    def prov_pk(self):
        return self.request.get('fprov_pk')

    def table_prov(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Province).filter(Province.prov_pk == self.prov_pk)
        return query.first()
