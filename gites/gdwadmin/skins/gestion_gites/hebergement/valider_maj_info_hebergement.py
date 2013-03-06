## Script (Python) "valider_maj_info_hebergement"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
#
# appelle par "form_valider_hebergement_info"  
# table hebergement
# mise à jour des infos hebergement par validation des données 
#
heb_pk = context.REQUEST.get('heb_pk', None)
heb_maj_pk = context.REQUEST.get('heb_maj_pk', None)
heb_nom = context.REQUEST.get('heb_nom', None)
heb_adresse = context.REQUEST.get('heb_adresse', None)
heb_localite = context.REQUEST.get('heb_localite', None)
heb_fumeur = context.REQUEST.get('heb_fumeur', None)
heb_animal = context.REQUEST.get('heb_animal', None)
heb_tenis = context.REQUEST.get('heb_tenis', None)
heb_nautisme = context.REQUEST.get('heb_nautisme', None)
heb_sky = context.REQUEST.get('heb_sky', None)
heb_rando = context.REQUEST.get('heb_rando', None)
heb_piscine = context.REQUEST.get('heb_piscine', None)
heb_peche = context.REQUEST.get('heb_peche', None)
heb_equitation = context.REQUEST.get('heb_equitation', None)
heb_velo = context.REQUEST.get('heb_velo', None)
heb_vtt = context.REQUEST.get('heb_vtt', None)
heb_ravel = context.REQUEST.get('heb_ravel', None)
heb_tenis_distance = context.REQUEST.get('heb_tenis_distance', None)
heb_nautisme_distance = context.REQUEST.get('heb_nautisme_distance', None)
heb_sky_distance = context.REQUEST.get('heb_sky_distance', None)
heb_rando_distance = context.REQUEST.get('heb_rando_distance', None)
heb_piscine_distance = context.REQUEST.get('heb_piscine_distance', None)
heb_peche_distance = context.REQUEST.get('heb_peche_distance', None)
heb_equitation_distance = context.REQUEST.get('heb_equitation_distance', None)
heb_velo_distance = context.REQUEST.get('heb_velo_distance', None)
heb_vtt_distance = context.REQUEST.get('heb_vtt_distance', None)
heb_ravel_distance = context.REQUEST.get('heb_ravel_distance', None)
heb_confort_tv = context.REQUEST.get('heb_confort_tv', None)
heb_confort_feu_ouvert = context.REQUEST.get('heb_confort_feu_ouvert', None)
heb_confort_lave_vaiselle = context.REQUEST.get('heb_confort_lave_vaiselle', None)
heb_confort_micro_onde = context.REQUEST.get('heb_confort_micro_onde', None)
heb_confort_lave_linge = context.REQUEST.get('heb_confort_lave_linge', None)
heb_confort_seche_linge = context.REQUEST.get('heb_confort_seche_linge', None)
heb_confort_congelateur = context.REQUEST.get('heb_confort_congelateur', None)
heb_confort_internet = context.REQUEST.get('heb_confort_internet', None)
heb_taxe_sejour = context.REQUEST.get('heb_taxe_sejour', None)
heb_taxe_montant = context.REQUEST.get('heb_taxe_montant', None)
heb_forfait_montant = context.REQUEST.get('heb_forfait_montant', None)
heb_lit_1p = context.REQUEST.get('heb_lit_1p', None)
heb_lit_2p = context.REQUEST.get('heb_lit_2p', None)
heb_lit_sup = context.REQUEST.get('heb_lit_sup', None)
heb_lit_enf = context.REQUEST.get('heb_lit_enf', None)
heb_distribution_fr = context.REQUEST.get('heb_distribution_fr', None)
heb_descriptif_fr = context.REQUEST.get('heb_descriptif_fr', None)
heb_pointfort_fr = context.REQUEST.get('heb_pointfort_fr', None)
heb_commerce = context.REQUEST.get('heb_commerce', None)
heb_restaurant = context.REQUEST.get('heb_restaurant', None)
heb_gare = context.REQUEST.get('heb_gare', None)
heb_gare_distance = context.REQUEST.get('heb_gare_distance', None)
heb_restaurant_distance = context.REQUEST.get('heb_restaurant_distance', None)
heb_commerce_distance = context.REQUEST.get('heb_commerce_distance', None)

hebhot_tabhot_fk = context.REQUEST.get('hebhot_tabhot_fk', None)

heb_typeheb_fk = context.REQUEST.heb_typeheb_fk

if int(heb_typeheb_fk) in (5,6,9):
    heb_tarif_chmbr_avec_dej_1p = context.REQUEST.get('heb_tarif_chmbr_avec_dej_1p', None)
    heb_tarif_chmbr_avec_dej_2p = context.REQUEST.get('heb_tarif_chmbr_avec_dej_2p', None)
    heb_tarif_chmbr_avec_dej_3p = context.REQUEST.get('heb_tarif_chmbr_avec_dej_3p', None)
    heb_tarif_chmbr_sans_dej_1p = context.REQUEST.get('heb_tarif_chmbr_sans_dej_1p', None)
    heb_tarif_chmbr_sans_dej_2p = context.REQUEST.get('heb_tarif_chmbr_sans_dej_2p', None)
    heb_tarif_chmbr_sans_dej_3p = context.REQUEST.get('heb_tarif_chmbr_sans_dej_3p', None)
    heb_tarif_chmbr_table_hote_1p = context.REQUEST.get('heb_tarif_chmbr_table_hote_1p', None)
    heb_tarif_chmbr_table_hote_2p = context.REQUEST.get('heb_tarif_chmbr_table_hote_2p', None)
    heb_tarif_chmbr_table_hote_3p = context.REQUEST.get('heb_tarif_chmbr_table_hote_3p', None)
    heb_tarif_chmbr_autre_1p = context.REQUEST.get('heb_tarif_chmbr_autre_1p', None)
    heb_tarif_chmbr_autre_2p = context.REQUEST.get('heb_tarif_chmbr_autre_2p', None)
    heb_tarif_chmbr_autre_3p = context.REQUEST.get('heb_tarif_chmbr_autre_3p', None)
    heb_charge_fk = 2
    context.admin_base.hebergement.zsql_maj_hebergement_update(heb_pk = heb_pk, \
                                                               heb_nom = heb_nom, \
                                                               heb_adresse = heb_adresse, \
                                                               heb_localite = heb_localite, \
                                                               heb_tenis = heb_tenis, \
                                                               heb_nautisme = heb_nautisme, \
                                                               heb_sky = heb_sky, \
                                                               heb_rando = heb_rando, \
                                                               heb_piscine = heb_piscine, \
                                                               heb_peche = heb_peche, \
                                                               heb_equitation = heb_equitation, \
                                                               heb_velo = heb_velo, \
                                                               heb_vtt = heb_vtt, \
                                                               heb_ravel = heb_ravel, \
                                                               heb_tenis_distance = heb_tenis_distance, \
                                                               heb_nautisme_distance = heb_nautisme_distance, \
                                                               heb_sky_distance = heb_sky_distance, \
                                                               heb_rando_distance = heb_rando_distance, \
                                                               heb_piscine_distance = heb_piscine_distance, \
                                                               heb_peche_distance = heb_peche_distance, \
                                                               heb_equitation_distance = heb_equitation_distance, \
                                                               heb_velo_distance = heb_velo_distance, \
                                                               heb_vtt_distance = heb_vtt_distance, \
                                                               heb_ravel_distance = heb_ravel_distance, \
                                                               heb_animal = heb_animal, \
                                                               heb_fumeur = heb_fumeur, \
                                                               heb_confort_tv = heb_confort_tv, \
                                                               heb_confort_feu_ouvert = heb_confort_feu_ouvert, \
                                                               heb_confort_lave_vaiselle = heb_confort_lave_vaiselle, \
                                                               heb_confort_micro_onde = heb_confort_micro_onde, \
                                                               heb_confort_lave_linge = heb_confort_lave_linge, \
                                                               heb_confort_seche_linge = heb_confort_seche_linge, \
                                                               heb_confort_congelateur = heb_confort_congelateur, \
                                                               heb_confort_internet = heb_confort_internet, \
                                                               heb_taxe_sejour = heb_taxe_sejour, \
                                                               heb_taxe_montant = heb_taxe_montant, \
                                                               heb_forfait_montant = heb_forfait_montant, \
                                                               heb_lit_1p = heb_lit_1p, \
                                                               heb_lit_2p = heb_lit_2p, \
                                                               heb_lit_sup = heb_lit_sup, \
                                                               heb_lit_enf = heb_lit_enf, \
                                                               heb_distribution_fr = heb_distribution_fr, \
                                                               heb_descriptif_fr = heb_descriptif_fr, \
                                                               heb_pointfort_fr = heb_pointfort_fr, \
                                                               heb_commerce = heb_commerce, \
                                                               heb_restaurant = heb_restaurant, \
                                                               heb_gare = heb_gare, \
                                                               heb_gare_distance = heb_gare_distance, \
                                                               heb_restaurant_distance = heb_restaurant_distance, \
                                                               heb_commerce_distance = heb_commerce_distance, \
                                                               heb_tarif_chmbr_avec_dej_1p = heb_tarif_chmbr_avec_dej_1p, \
                                                               heb_tarif_chmbr_avec_dej_2p = heb_tarif_chmbr_avec_dej_2p, \
                                                               heb_tarif_chmbr_avec_dej_3p = heb_tarif_chmbr_avec_dej_3p, \
                                                               heb_tarif_chmbr_sans_dej_1p = heb_tarif_chmbr_sans_dej_1p, \
                                                               heb_tarif_chmbr_sans_dej_2p = heb_tarif_chmbr_sans_dej_2p, \
                                                               heb_tarif_chmbr_sans_dej_3p = heb_tarif_chmbr_sans_dej_3p, \
                                                               heb_tarif_chmbr_table_hote_1p = heb_tarif_chmbr_table_hote_1p, \
                                                               heb_tarif_chmbr_table_hote_2p = heb_tarif_chmbr_table_hote_2p, \
                                                               heb_tarif_chmbr_table_hote_3p = heb_tarif_chmbr_table_hote_3p, \
                                                               heb_tarif_chmbr_autre_1p = heb_tarif_chmbr_autre_1p, \
                                                               heb_tarif_chmbr_autre_2p = heb_tarif_chmbr_autre_2p, \
                                                               heb_tarif_chmbr_autre_3p = heb_tarif_chmbr_autre_3p, \
                                                               heb_charge_fk = heb_charge_fk)
else: 
    heb_tarif_we_3n = context.REQUEST.get('heb_tarif_we_3n', None)
    heb_tarif_we_4n = context.REQUEST.get('heb_tarif_we_4n', None)
    heb_tarif_semaine_fin_annee = context.REQUEST.get('heb_tarif_semaine_fin_annee', None)
    heb_tarif_we_bs = context.REQUEST.get('heb_tarif_we_bs', None)
    heb_tarif_we_ms = context.REQUEST.get('heb_tarif_we_ms', None)
    heb_tarif_we_hs = context.REQUEST.get('heb_tarif_we_hs', None)
    heb_tarif_sem_bs = context.REQUEST.get('heb_tarif_sem_bs', None)
    heb_tarif_sem_ms = context.REQUEST.get('heb_tarif_sem_ms', None)
    heb_tarif_sem_hs = context.REQUEST.get('heb_tarif_sem_hs', None)
    heb_tarif_garantie = context.REQUEST.get('heb_tarif_garantie', None)
    heb_tarif_divers = context.REQUEST.get('heb_tarif_divers', None)
    heb_charge_fk = context.REQUEST.get('heb_charge_fk', 2)
    context.admin_base.hebergement.zsql_maj_hebergement_update(heb_pk = heb_pk, \
                                                               heb_nom = heb_nom, \
                                                               heb_adresse = heb_adresse, \
                                                               heb_localite = heb_localite, \
                                                               heb_tenis = heb_tenis, \
                                                               heb_nautisme = heb_nautisme, \
                                                               heb_sky = heb_sky, \
                                                               heb_rando = heb_rando, \
                                                               heb_piscine = heb_piscine, \
                                                               heb_peche = heb_peche, \
                                                               heb_equitation = heb_equitation, \
                                                               heb_velo = heb_velo, \
                                                               heb_vtt = heb_vtt, \
                                                               heb_ravel = heb_ravel, \
                                                               heb_tenis_distance = heb_tenis_distance, \
                                                               heb_nautisme_distance = heb_nautisme_distance, \
                                                               heb_sky_distance = heb_sky_distance, \
                                                               heb_rando_distance = heb_rando_distance, \
                                                               heb_piscine_distance = heb_piscine_distance, \
                                                               heb_peche_distance = heb_peche_distance, \
                                                               heb_equitation_distance = heb_equitation_distance, \
                                                               heb_velo_distance = heb_velo_distance, \
                                                               heb_vtt_distance = heb_vtt_distance, \
                                                               heb_ravel_distance = heb_ravel_distance, \
                                                               heb_animal = heb_animal, \
                                                               heb_fumeur = heb_fumeur, \
                                                               heb_confort_tv = heb_confort_tv, \
                                                               heb_confort_feu_ouvert = heb_confort_feu_ouvert, \
                                                               heb_confort_lave_vaiselle = heb_confort_lave_vaiselle, \
                                                               heb_confort_micro_onde = heb_confort_micro_onde, \
                                                               heb_confort_lave_linge = heb_confort_lave_linge, \
                                                               heb_confort_seche_linge = heb_confort_seche_linge, \
                                                               heb_confort_congelateur = heb_confort_congelateur, \
                                                               heb_confort_internet = heb_confort_internet, \
                                                               heb_taxe_sejour = heb_taxe_sejour, \
                                                               heb_taxe_montant = heb_taxe_montant, \
                                                               heb_forfait_montant = heb_forfait_montant, \
                                                               heb_tarif_we_bs = heb_tarif_we_bs, \
                                                               heb_tarif_we_ms = heb_tarif_we_ms, \
                                                               heb_tarif_we_hs = heb_tarif_we_hs, \
                                                               heb_tarif_sem_bs = heb_tarif_sem_bs, \
                                                               heb_tarif_sem_ms = heb_tarif_sem_ms, \
                                                               heb_tarif_sem_hs = heb_tarif_sem_hs, \
                                                               heb_tarif_garantie = heb_tarif_garantie, \
                                                               heb_tarif_divers = heb_tarif_divers, \
                                                               heb_tarif_we_3n = heb_tarif_we_3n, \
                                                               heb_tarif_we_4n = heb_tarif_we_4n, \
                                                               heb_tarif_semaine_fin_annee = heb_tarif_semaine_fin_annee, \
                                                               heb_lit_1p = heb_lit_1p, \
                                                               heb_lit_2p = heb_lit_2p, \
                                                               heb_lit_sup = heb_lit_sup, \
                                                               heb_lit_enf = heb_lit_enf, \
                                                               heb_distribution_fr = heb_distribution_fr, \
                                                               heb_descriptif_fr = heb_descriptif_fr, \
                                                               heb_pointfort_fr = heb_pointfort_fr, \
                                                               heb_commerce = heb_commerce, \
                                                               heb_restaurant = heb_restaurant, \
                                                               heb_gare = heb_gare, \
                                                               heb_gare_distance = heb_gare_distance, \
                                                               heb_restaurant_distance = heb_restaurant_distance, \
                                                               heb_commerce_distance = heb_commerce_distance, \
                                                               heb_charge_fk = heb_charge_fk)
     

#suppression des infos de maj dans la table hebergement
context.admin_base.hebergement.zsql_maj_hebergement_delete_by_heb_maj_pk(heb_maj_pk=heb_maj_pk)



# SI il y a un type de table d'hote coché,
#   je détruis toutes les infos qui se rapportent à cet hébergement
#   j'insère les nouvelles infos
# SINON
#   je détruis toutes les infos liées à cet hébergement
if hebhot_tabhot_fk > -1:
   context.admin_base.table_hote.zsql_heb_tab_hote_delete(hebhot_heb_fk=heb_pk)
   for elem in hebhot_tabhot_fk:
      context.admin_base.table_hote.zsql_heb_tab_hote_insert(hebhot_heb_fk=heb_pk, hebhot_tabho_fk=elem)
else:
   context.admin_base.table_hote.zsql_heb_tab_hote_delete(hebhot_heb_fk=heb_pk)



#suppression des infos de maj dans la table heb_tab_hote_maj
context.admin_base.table_hote.zsql_delete_heb_tab_hote_maj(hebhot_maj_heb_fk=heb_pk)







#retour sur la page qui liste les proprio en attente de confirmation
return context.REQUEST.RESPONSE.redirect('listing_maj_hebergement_info')
