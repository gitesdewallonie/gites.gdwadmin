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
heb_taxe_montant = context.REQUEST.get('heb_taxe_montant', None)
heb_forfait_montant = context.REQUEST.get('heb_forfait_montant', None)
heb_lit_1p = context.REQUEST.get('heb_lit_1p', None)
heb_lit_2p = context.REQUEST.get('heb_lit_2p', None)
heb_lit_sup = context.REQUEST.get('heb_lit_sup', None)
heb_lit_enf = context.REQUEST.get('heb_lit_enf', None)
heb_distribution_fr = context.REQUEST.get('heb_distribution_fr', None)
heb_descriptif_fr = context.REQUEST.get('heb_descriptif_fr', None)
heb_pointfort_fr = context.REQUEST.get('heb_pointfort_fr', None)

heb_typeheb_fk = context.REQUEST.heb_typeheb_fk

if int(heb_typeheb_fk) in (5, 6, 9):
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
    context.admin_base.hebergement.zsql_maj_hebergement_update(
        heb_pk=heb_pk,
        heb_nom=heb_nom,
        heb_adresse=heb_adresse,
        heb_localite=heb_localite,
        heb_taxe_montant=heb_taxe_montant,
        heb_forfait_montant=heb_forfait_montant,
        heb_lit_1p=heb_lit_1p,
        heb_lit_2p=heb_lit_2p,
        heb_lit_sup=heb_lit_sup,
        heb_lit_enf=heb_lit_enf,
        heb_distribution_fr=heb_distribution_fr,
        heb_descriptif_fr=heb_descriptif_fr,
        heb_pointfort_fr=heb_pointfort_fr,
        heb_tarif_chmbr_avec_dej_1p=heb_tarif_chmbr_avec_dej_1p,
        heb_tarif_chmbr_avec_dej_2p=heb_tarif_chmbr_avec_dej_2p,
        heb_tarif_chmbr_avec_dej_3p=heb_tarif_chmbr_avec_dej_3p,
        heb_tarif_chmbr_sans_dej_1p=heb_tarif_chmbr_sans_dej_1p,
        heb_tarif_chmbr_sans_dej_2p=heb_tarif_chmbr_sans_dej_2p,
        heb_tarif_chmbr_sans_dej_3p=heb_tarif_chmbr_sans_dej_3p,
        heb_tarif_chmbr_table_hote_1p=heb_tarif_chmbr_table_hote_1p,
        heb_tarif_chmbr_table_hote_2p=heb_tarif_chmbr_table_hote_2p,
        heb_tarif_chmbr_table_hote_3p=heb_tarif_chmbr_table_hote_3p,
        heb_tarif_chmbr_autre_1p=heb_tarif_chmbr_autre_1p,
        heb_tarif_chmbr_autre_2p=heb_tarif_chmbr_autre_2p,
        heb_tarif_chmbr_autre_3p=heb_tarif_chmbr_autre_3p,
        heb_charge_fk=heb_charge_fk)
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
    context.admin_base.hebergement.zsql_maj_hebergement_update(
        heb_pk=heb_pk,
        heb_nom=heb_nom,
        heb_adresse=heb_adresse,
        heb_localite=heb_localite,
        heb_taxe_montant=heb_taxe_montant,
        heb_forfait_montant=heb_forfait_montant,
        heb_tarif_we_bs=heb_tarif_we_bs,
        heb_tarif_we_ms=heb_tarif_we_ms,
        heb_tarif_we_hs=heb_tarif_we_hs,
        heb_tarif_sem_bs=heb_tarif_sem_bs,
        heb_tarif_sem_ms=heb_tarif_sem_ms,
        heb_tarif_sem_hs=heb_tarif_sem_hs,
        heb_tarif_garantie=heb_tarif_garantie,
        heb_tarif_divers=heb_tarif_divers,
        heb_tarif_we_3n=heb_tarif_we_3n,
        heb_tarif_we_4n=heb_tarif_we_4n,
        heb_tarif_semaine_fin_annee=heb_tarif_semaine_fin_annee,
        heb_lit_1p=heb_lit_1p,
        heb_lit_2p=heb_lit_2p,
        heb_lit_sup=heb_lit_sup,
        heb_lit_enf=heb_lit_enf,
        heb_distribution_fr=heb_distribution_fr,
        heb_descriptif_fr=heb_descriptif_fr,
        heb_pointfort_fr=heb_pointfort_fr,
        heb_charge_fk=heb_charge_fk)

# Updates the metadatas
context.admin_base.hebergement.zsql_maj_hebergement_metadata(heb_pk=heb_pk)

#suppression des infos de maj dans la table hebergement
context.admin_base.hebergement.zsql_maj_hebergement_delete_by_heb_maj_pk(heb_maj_pk=heb_maj_pk);
context.admin_base.hebergement.zsql_maj_hebergement_delete_metadata(heb_pk=heb_pk)

#retour sur la page qui liste les proprio en attente de confirmation
return context.REQUEST.RESPONSE.redirect('listing_maj_hebergement_info')
