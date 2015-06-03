# -*- coding: utf-8 -*-
# En rajoutant la ligne ci-dessus, on pourra utiliser des caractères particuliers dans
# les commentaires. Cette ligne doit toujours être placée sur la première ligne de code
# il ne peut rien y avoir avant.

from Products.Five.browser import BrowserView
from z3c.sqlalchemy import getSAWrapper
from gites.db.content.hebergement.hebergementmaj import HebergementMaj
from gites.db.content.proprio.propriomaj import ProprioMaj
from gites.db.content.proprio.proprio import Proprio
from gites.db.content.hebergement.hebergement import Hebergement
from gites.db.content.hebergement.hebergementview import HebergementView
from gites.db.content.hebergement.typehebergement import TypeHebergement
from sqlalchemy import func, select, join, and_




class IntroView(BrowserView):

    # Hébergements en attente de confirmation :
    def hebergement_maj_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(func.count(HebergementMaj.heb_maj_pk))
        return query.scalar()

    # Propriétaires en attente de confirmation :
    def proprio_maj(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(func.count(ProprioMaj.pro_maj_pk))
        return query.scalar()

    # Nombre de propriétaires :
    def proprio_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(func.count(Proprio.pro_pk))
        return query.scalar()

    # Nombre de propriétaires actifs :
    def proprio_active_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(func.count(Proprio.pro_pk)).filter(
            Proprio.pro_etat == 'True')
        return query.scalar()

    # Nombre de propriétaires désactivés :
    def proprio_desactive_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(func.count(Proprio.pro_pk)).filter(
            Proprio.pro_etat == 'False')
        return query.scalar()



    # Nombre de d'hébergements par type :
    def hebergement_type_count(self):
        # on joint les deux tables
        heb_join = join(Hebergement, TypeHebergement,
                        # On ne cherche les Keys Primaire en commun
                        Hebergement.heb_typeheb_fk == TypeHebergement.type_heb_pk)
        # On compte le nombre d'hébergement correspondant au nom du type
        query = select([TypeHebergement.type_heb_nom,
                        func.count(Hebergement.heb_pk).label('heb_pk_count')])
        query = query.select_from(heb_join)
        # On groupe les données selon un critère, afin de ne pas tout afficher
        query = query.group_by(TypeHebergement.type_heb_nom)
        # On exécute notre fontion et on affiche toute les lignes,
        # pour n'en afficher qu'une seule, on utiliserait fetchone()
        query = query.execute().fetchall()
        # On retourne le résultat
        return query

    def hebergement_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(func.count(Hebergement.heb_pk))
        return query.scalar()


    # Nombre de CH et de MH dont le proprio est actif :
    def heb_CH_actif_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement, Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_actif_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_typeheb_fk.in_(['5', '6', '9'])))
        result = session.execute(query).fetchall()
        return result



    # Nombre de CH et de MH dont le proprio est actif et publié:
    def heb_CH_actif_public_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement, Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_actif_public_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_typeheb_fk.in_(['5', '6', '9']),
            Hebergement.heb_site_public == '1'))
        result = session.execute(query).fetchall()
        return result

    # Nombre de CH et de MH dont le proprio est actif et n'est pas publié:
    def heb_CH_actif_nopublic_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement, Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_actif_nopublic_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_typeheb_fk.in_(['5', '6', '9']),
            Hebergement.heb_site_public == '0'))
        result = session.execute(query).fetchall()
        return result


    # Nombre de GR GC GF MT MV dont le proprio est actif :
    def heb_GR_actif_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement, Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_actif_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_typeheb_fk.in_(['1', '2', '3', '4', '7', '10'])))
        result = session.execute(query).fetchall()
        return result



    # Nombre de GR GC GF MT MV dont le proprio est actif et publié:
    def heb_GR_actif_public_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement, Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_actif_public_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_typeheb_fk.in_(['1', '2', '3', '4', '7', '10']),
            Hebergement.heb_site_public == '1'))
        result = session.execute(query).fetchall()
        return result

    # Nombre de GR GC GF MT MV dont le proprio est actif et n'est pas publié:
    def heb_GR_actif_nopublic_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement, Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_actif_nopublic_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(
            Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_typeheb_fk.in_(['1', '2', '3', '4', '7', '10']),
            Hebergement.heb_site_public == '0'))
        result = session.execute(query).fetchall()
        return result


    # Nombre d'hébergement publiés sur le portail :
    def heb_public_portail_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement, Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_public_portail_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_site_public == '1'))
        result = session.execute(query).fetchall()
        return result


    # Nombre d'hébergement non-publiés sur le portail :
    def heb_nopublic_portail_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement,
            Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_nopublic_portail_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_site_public == '0'))
        result = session.execute(query).fetchall()
        return result






    # Nombre d'hébergement par thème Nature :
    def heb_theme_nature_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(func.count(
            HebergementView.heb_pk)).filter(
            HebergementView.heb_gid_activite_nature == 'oui')
        return query.scalar()

    # Nombre d'hébergement par thème Equestre :
    def heb_theme_equestre_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(func.count(
            HebergementView.heb_pk)).filter(
            HebergementView.heb_gid_theme_equestre == 'oui')
        return query.scalar()

    # Nombre d'hébergement par thème Peche :
    def heb_theme_peche_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(func.count(
            HebergementView.heb_pk)).filter(
            HebergementView.heb_gid_peche == 'oui')
        return query.scalar()

    # Nombre d'hébergement par thème Panda :
    def heb_theme_panda_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(func.count(
            HebergementView.heb_pk)).filter(
            HebergementView.heb_gid_panda == 'oui')
        return query.scalar()

    # Nombre d'hébergement par thème Patrimoine :
    def heb_theme_patrimoine_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        query = session.query(func.count(
            HebergementView.heb_pk)).filter(
            HebergementView.heb_gid_patrimoine == 'oui')
        return query.scalar()


    # Nombre d'hébergement dont le calendrier est actif :
    def heb_calend_proprio_actif_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement,
            Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_calend_proprio_actif_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_calendrier_proprio == 'actif'))
        result = session.execute(query).fetchall()
        return result

    # Nombre d'hébergement dont le calendrier est actif pour la recherche :
    def heb_calend_proprio_searchactif_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement,
            Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_calend_proprio_searchactif_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_calendrier_proprio == 'searchactif'))
        result = session.execute(query).fetchall()
        return result

    # Nombre d'hébergement dont le calendrier n'est pas actif :
    def heb_calend_proprio_noactif_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement,
            Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_calend_proprio_noactif_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_calendrier_proprio == 'non actif'))
        result = session.execute(query).fetchall()
        return result

    # Nombre d'hébergement dont le calendrier est bloqué :
    def heb_calend_proprio_bloc_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement,
            Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_calend_proprio_bloc_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_calendrier_proprio == 'bloque'))
        result = session.execute(query).fetchall()
        return result


    # Nombre d'hébergement de type "CH MH CHECR " dont le calendrier est actif :
    def heb_calend_CH_actif_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement,
            Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_calend_CH_actif_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_typeheb_fk.in_(['5', '6', '9']),
            Hebergement.heb_calendrier_proprio == 'actif'))
        result = session.execute(query).fetchall()
        return result

    # Nombre d'hébergement de type "CH MH CHECR " dont le calendrier n'est pas actif :
    def heb_calend_CH_noactif_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement,
            Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_calend_CH_noactif_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_typeheb_fk.in_(['5', '6', '9']),
            Hebergement.heb_calendrier_proprio == 'non actif'))
        result = session.execute(query).fetchall()
        return result


    # Nombre d'hébergement de type "CH MH CHECR " dont le calendrier est bloqué :
    def heb_calend_CH_bloc_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement, Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_calend_CH_bloc_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_typeheb_fk.in_(['5', '6', '9']),
            Hebergement.heb_calendrier_proprio == 'bloque'))
        result = session.execute(query).fetchall()
        return result

    # Nombre d'hébergement de type "CH MH CHECR " dont le calendrier est actif pour la recherche :
    def heb_calend_CH_searchactif_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement, Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_calend_CH_searchactif_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_typeheb_fk.in_(['5', '6', '9']),
            Hebergement.heb_calendrier_proprio == 'searchactif'))
        result = session.execute(query).fetchall()
        return result


    # Nombre d'hébergement de type "GR GC GF MT MV GRECR" dont le calendrier est actif :
    def heb_calend_GR_actif_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement,
            Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_calend_GR_actif_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_typeheb_fk.in_(['5', '6', '9']),
            Hebergement.heb_calendrier_proprio == 'actif'))
        result = session.execute(query).fetchall()
        return result

    # Nombre d'hébergement de type "GR GC GF MT MV GRECR" dont le calendrier n'est pas actif :
    def heb_calend_GR_noactif_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement,
            Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_calend_GR_noactif_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_typeheb_fk.in_(['5', '6', '9']),
            Hebergement.heb_calendrier_proprio == 'non actif'))
        result = session.execute(query).fetchall()
        return result


    # Nombre d'hébergement de type "GR GC GF MT MV GRECR" dont le calendrier est bloqué :
    def heb_calend_GR_bloc_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement,
            Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_calend_GR_bloc_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_typeheb_fk.in_(['5', '6', '9']),
            Hebergement.heb_calendrier_proprio == 'bloque'))
        result = session.execute(query).fetchall()
        return result

    # Nombre d'hébergement de type "GR GC GF MT MV GRECR" dont le calendrier est actif pour la reGRerGRe :
    def heb_calend_GR_searchactif_count(self):
        wrapper = getSAWrapper('gites_wallons')
        session = wrapper.session
        heb_proprio_join = join(
            Hebergement,
            Proprio,
            Hebergement.heb_pro_fk == Proprio.pro_pk)
        query = select([Proprio.pro_etat,
                        func.count(Hebergement.heb_pro_fk).label('heb_calend_GR_searchactif_count')])
        query = query.select_from(heb_proprio_join)
        query = query.group_by(Proprio.pro_etat)
        query.append_whereclause(and_(
            Proprio.pro_etat == True,
            Hebergement.heb_typeheb_fk.in_(['5', '6', '9']),
            Hebergement.heb_calendrier_proprio == 'searchactif'))
        result = session.execute(query).fetchall()
        return result
