# -*- coding: utf-8 -*-
# En rajoutant la ligne ci-dessus, on pourra utiliser des caractères particuliers dans
# les commentaires. Cette ligne doit toujours être placée sur la première ligne de code
# il ne peut rien y avoir avant.

# On importe les modules nécessaires
from sqlalchemy import create_engine, and_, or_, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from gites.db.content.hebergement.hebergement import Hebergement
from gites.db.content.hebergement.typehebergement import TypeHebergement
 
Base = declarative_base()

# On se connecte à la bd
engine = create_engine('postgresql+psycopg2://aurore@/gites_wallons')
 

# On se lie données de la base de sorte que la
# la déclarative peut être accessible via une instance DBSession
Base.metadata.bind = engine

# On crée la session
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
 
# On défini la fonction run qui permettre d'afficher le résultat de la manière demandée
def run(stmt):
    rs = stmt.execute()
# J'ai rajouté cette phrase afin de séparer les différents résultats de recherche
    print "\nLe résultat de la recherche est :"
    for row in rs:
        print row


# # ------------- PARTIE QUI FONCTIONNE ---------------- # #

# # # Compte le nombre d'hébergement de type "Aucun"
# query = session.query(func.count(Hebergement.heb_typeheb_fk)).filter(and_(
#   Hebergement.heb_typeheb_fk=='0',
# ))
# for line in query.all():
#     print '\nNombre de gîtes de type "Aucun" : '
#     print line


# # # Compte le nombre d'hébergement de type "Gîte rural"
# query = session.query(func.count(Hebergement.heb_typeheb_fk)).filter(and_(
#   Hebergement.heb_typeheb_fk=='1',
# ))
# for line in query.all():
#     print '\nNombre de gîtes de type "Gîte rural" : '
#     print line

# # # Compte le nombre d'hébergement de type "Gîte à la ferme"
# query = session.query(func.count(Hebergement.heb_typeheb_fk)).filter(and_(
#   Hebergement.heb_typeheb_fk=='2',
# ))
# for line in query.all():
#     print '\nNombre de gîtes de type "Gîte à la ferme" : '
#     print line

# # # Compte le nombre d'hébergement de type "Meublé de tourisme"
# query = session.query(func.count(Hebergement.heb_typeheb_fk)).filter(and_(
#   Hebergement.heb_typeheb_fk=='3',
# ))
# for line in query.all():
#     print '\nNombre de gîtes de type "Moublé de tourisme" : '
#     print line


# # # Compte le nombre d'hébergement de type "Gîte citadin"
# query = session.query(func.count(Hebergement.heb_typeheb_fk)).filter(and_(
#   Hebergement.heb_typeheb_fk=='4',
# ))
# for line in query.all():
#     print '\nNombre de gîtes de type "Gîte citadin" : '
#     print line


# # # Compte le nombre d'hébergement de type "Maison d'Hôtes"
# query = session.query(func.count(Hebergement.heb_typeheb_fk)).filter(and_(
#   Hebergement.heb_typeheb_fk=='5',
# ))
# for line in query.all():
#     print '\nNombre de gîtes de type "Maison d Hôtes" : '
#     print line

# # # Compte le nombre d'hébergement de type "Chambre d'Hôtes"
# query = session.query(func.count(Hebergement.heb_typeheb_fk)).filter(and_(
#   Hebergement.heb_typeheb_fk=='6',
# ))
# for line in query.all():
#     print '\nNombre de gîtes de type "Chambre d Hôtes" : '
#     print line



# # # Compte le nombre d'hébergement de type "Meublé de vacances"
# query = session.query(func.count(Hebergement.heb_typeheb_fk)).filter(and_(
#   Hebergement.heb_typeheb_fk=='7',
# ))
# for line in query.all():
#     print '\nNombre de gîtes de type "Meublé de vacances" : '
#     print line



# # # Compte le nombre d'hébergement de type "Chambre"
# query = session.query(func.count(Hebergement.heb_typeheb_fk)).filter(and_(
#   Hebergement.heb_typeheb_fk=='9',
# ))
# for line in query.all():
#     print '\nNombre de gîtes de type "Chambre" : '
#     print line

# # # Compte le nombre d'hébergement de type "Logement"
# query = session.query(func.count(Hebergement.heb_typeheb_fk)).filter(and_(
#   Hebergement.heb_typeheb_fk=='10',
# ))
# for line in query.all():
#     print '\nNombre de gîtes de type "Logement" : '
#     print line




# # ------------- PARTIE QUE L'ON TESTE ---------------- # #

# # Compte le nombre d'hébergement de type "Gîtes groupés"
query = session.query(func.count(Hebergement.heb_typeheb_fk)).filter(and_(
  Hebergement.heb_typeheb_fk=='11',
))
for line in query.all():
    print '\nNombre de gîtes de type "Gîtes groupés" : \n', line



# On teste ici une autre façon d'écrire plus appropriée
# lorsque l'on ne retourne qu'un seul résultat
query = session.query(func.count(Hebergement.heb_typeheb_fk)).filter(
    Hebergement.heb_typeheb_fk=='10',).scalar()
    print query


#  J'essaye d'automatiser un peu la requête
le_type =='' # On insérera ici le numéro du type d'hébergement que l'on cherche
query = session.query(func.count(Hebergement.heb_typeheb_fk)).filter(and_(
  Hebergement.heb_typeheb_fk==le_type,
))
for line in query.all():
    print '\nNombre de gîtes' de type "Logement" : 
    print line





