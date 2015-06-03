# -*- coding: utf-8 -*-
# En rajoutant la ligne ci-dessus, on pourra utiliser des caractères particuliers dans
# les type_hebmentaires. Cette ligne doit toujours être placée sur la première ligne de code
# il ne peut rien y avoir avant.

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.proprio.civilite import Civilite


class ModifCivilite(BrowserView):

    @property
    def civ_pk(self):
        return self.request.get('fciv_pk')

    def civilite(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(Civilite.civ_pk,
                              Civilite.civ_titre).filter(Civilite.civ_pk == self.civ_pk)
        return query.first()
