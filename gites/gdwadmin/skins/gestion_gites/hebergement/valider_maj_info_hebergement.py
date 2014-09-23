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
heb_url = context.REQUEST.get('heb_url', None)
heb_adresse = context.REQUEST.get('heb_adresse', None)
heb_localite = context.REQUEST.get('heb_localite', None)
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
    context.admin_base.hebergement.zsql_maj_hebergement_update(
        heb_pk=heb_pk,
        heb_nom=heb_nom,
        heb_url=heb_url,
        heb_adresse=heb_adresse,
        heb_localite=heb_localite,
        heb_forfait_montant=heb_forfait_montant,
        heb_lit_1p=heb_lit_1p,
        heb_lit_2p=heb_lit_2p,
        heb_lit_sup=heb_lit_sup,
        heb_lit_enf=heb_lit_enf,
        heb_distribution_fr=heb_distribution_fr,
        heb_descriptif_fr=heb_descriptif_fr,
        heb_pointfort_fr=heb_pointfort_fr)
else:
    context.admin_base.hebergement.zsql_maj_hebergement_update(
        heb_pk=heb_pk,
        heb_nom=heb_nom,
        heb_url=heb_url,
        heb_adresse=heb_adresse,
        heb_localite=heb_localite,
        heb_forfait_montant=heb_forfait_montant,
        heb_lit_1p=heb_lit_1p,
        heb_lit_2p=heb_lit_2p,
        heb_lit_sup=heb_lit_sup,
        heb_lit_enf=heb_lit_enf,
        heb_distribution_fr=heb_distribution_fr,
        heb_descriptif_fr=heb_descriptif_fr,
        heb_pointfort_fr=heb_pointfort_fr)

# Updates the metadatas
context.admin_base.hebergement.zsql_maj_hebergement_metadata(heb_pk=heb_pk)

#suppression des infos de maj dans la table hebergement
context.admin_base.hebergement.zsql_maj_hebergement_delete_by_heb_maj_pk(heb_maj_pk=heb_maj_pk);
context.admin_base.hebergement.zsql_maj_hebergement_delete_metadata(heb_pk=heb_pk)

#retour sur la page qui liste les proprio en attente de confirmation
return context.REQUEST.RESPONSE.redirect('listing_maj_hebergement_info')
