import random
import csv

# Nom du fichier
csv_filename = "questionnaire_sae_lp_alea.csv"

# En-têtes du fichier CSV
headers = [
    "Mail", "Nationalité", "Date de naissance", "Genre", 
    "Bac", "Type de Bac", "Spécialités (si >= 2021)", "Série Bac (si < 2021)", "Série Bac Techno", "Spécialité Bac Pro", "Autre formation sans Bac",
    "Formation 2023/2024", "Spécialisation Licence pro (CJ, GEA)", "Formation avant Licence pro", "Si Licence 2, préciser",
    "Situation après Licence pro", "Type poursuite d'étude", "Établissement (si Master + LP Comptabilité)", "Études à l'étranger", 
    "Formation initiale/alternance", "Lien formation actuelle-LP (1-5)", "Préparation LP (1-5)", "Recommander LP (1-5)",
    "Secteur activité (si insertion)", "Temps recherche emploi (mois)", "Statut juridique", "Type contrat", 
    "Lien poste - LP (Oui/Non)", "Raison si non lié à LP", "Évolution carrière (1-5)", "Correspondance travail-attentes (1-5)",
    "Rémunération (tranche salaire)", "Satisfaction salaire (1-5)", "Nombre heures/semaine", "Satisfaction horaires (1-5)",
    "Raison année de césure", "After-work IUT (1-5)", "Intervention pédagogique (1-5)", "Collaboration étudiants IUT (1-5)", "Rester en contact IUT (1-5)"
]

# Listes de valeurs possibles pour chaque variable
nationalites = ["Française", "Marocaine", "Espagnole", "Italienne", "Chinoise"]
genres = ["Féminin", "Masculin"]
bacs = ["Oui", "Non"]
types_bac = ["Général", "Technologique", "Professionnel"]
specialites_generales = ["Maths, Physique-Chimie", "SES, HGGSP", "LCA, LLCE", "NSI, EPPCS", "Humanités, SVT"]
series_ancien_bac = ["S", "ES", "L"]
series_techno = ["STMG", "STI2D", "STAV", "ST2S", "STD2A"]
specialites_pro = ["Numérique", "Bâtiment", "Vente", "Design", "Beauté"]
formations_actuelles = ["BUT GEA", "Licence pro (CJ, GEA)", "BUT INFO", "BUT RT", "Licence pro (MRIT, GMIE)"]
specialisations_lp = ["LP banque", "LP métier du notariat", "LP GRH", "LP Comptabilité paie", "vide"]
formations_avant_lp = ["BUT2", "BTS", "Licence 2", "autre"]
situations_post_lp = ["Poursuite d’études", "Insertion professionnelle", "Année de césure"]
types_etudes = ["Master", "École privée", "Réorientation", "autre"]
etablissements = ["Université Lyon 2", "Université Paris Dauphine", "Université de Bordeaux", "vide"]
etranger = ["Non", "Oui, Canada", "Oui, Espagne", "Oui, Allemagne", "Oui, Belgique"]
statuts_juridiques = ["Salarié", "Entrepreneur", "Fonction publique", "Autre"]
contrats = ["CDI", "CDD", "Autre"]
secteurs = ["Banque", "Informatique", "Droit", "Marketing", "RH"]
raisons_non_lien_lp = ["Réorientation", "Pas d’offre d’emploi", "Autre", "vide"]
tranches_salaire = ["]1500-1700]", "]1700-1900]", "]1900-2100]", "]2100-2300]", "]2300-2500]", "]supérieur à 2500]"]
raisons_cesure = ["Je n’ai pas trouvé de travail ni de formation", "Autre", "vide"]

# Génération de 50 réponses variées
data = []
for _ in range(50):
    nationalite = random.choice(nationalites)
    genre = random.choice(genres)
    bac = random.choice(bacs)
    
    # Déterminer les détails du bac si "Oui"
    type_bac = random.choice(types_bac) if bac == "Oui" else "vide"
    specialite_generale = random.choice(specialites_generales) if type_bac == "Général" else "vide"
    serie_ancien = random.choice(series_ancien_bac) if type_bac == "Général" else "vide"
    serie_techno = random.choice(series_techno) if type_bac == "Technologique" else "vide"
    specialite_pro = random.choice(specialites_pro) if type_bac == "Professionnel" else "vide"
    
    formation_actuelle = random.choice(formations_actuelles)
    specialisation_lp = random.choice(specialisations_lp) if "Licence pro" in formation_actuelle else "vide"
    formation_avant_lp = random.choice(formations_avant_lp)
    
    situation_post_lp = random.choice(situations_post_lp)
    type_etude = random.choice(types_etudes) if situation_post_lp == "Poursuite d’études" else "vide"
    etablissement = random.choice(etablissements) if type_etude == "Master" and specialisation_lp == "LP Comptabilité paie" else "vide"
    etudes_etranger = random.choice(etranger)
    statut_juridique = random.choice(statuts_juridiques) if situation_post_lp == "Insertion professionnelle" else "vide"
    contrat = random.choice(contrats) if statut_juridique != "vide" else "vide"
    secteur_activite = random.choice(secteurs) if statut_juridique != "vide" else "vide"
    raison_non_lien_lp = random.choice(raisons_non_lien_lp) if statut_juridique != "vide" else "vide"
    
    # Scores entre 1 et 5 pour différentes évaluations
    scores = [random.randint(1, 5) for _ in range(9)]
    
    tranche_salaire = random.choice(tranches_salaire) if statut_juridique != "vide" else "vide"
    raison_cesure = random.choice(raisons_cesure) if situation_post_lp == "Année de césure" else "vide"

    data.append([
        "vide", nationalite, f"{random.randint(1,28)}/{random.randint(1,12)}/{random.randint(1999, 2005)}", genre,
        bac, type_bac, specialite_generale, serie_ancien, serie_techno, specialite_pro, "vide",
        formation_actuelle, specialisation_lp, formation_avant_lp, "vide",
        situation_post_lp, type_etude, etablissement, etudes_etranger,
        random.choice(["Alternance", "Initiale"]), *scores[:3],
        secteur_activite, random.randint(1, 12) if statut_juridique != "vide" else "vide", statut_juridique, contrat,
        "Oui" if random.random() > 0.5 else "Non", raison_non_lien_lp, *scores[3:5],
        tranche_salaire, scores[5], random.randint(30, 45) if statut_juridique != "vide" else "vide", scores[6],
        raison_cesure, *scores[7:]
    ])

# Réécriture du fichier CSV avec des données variées
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(headers)  # Écriture des en-têtes
    writer.writerows(data)  # Écriture des données

csv_filename

