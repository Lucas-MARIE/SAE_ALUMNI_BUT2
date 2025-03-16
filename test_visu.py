import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le fichier CSV
df = pd.read_csv("questionnaire_sae_lp_alea.csv")

# Diagramme camembert des nationalités
plt.figure(figsize=(8, 6))
df['Nationalité'].value_counts().plot.pie(autopct="%1.1f%%", colors=sns.color_palette("pastel"))
plt.title("Répartition des nationalités")
plt.ylabel("")
plt.show()

# Histogramme des tranches de salaire
plt.figure(figsize=(8, 6))
df['Rémunération (tranche salaire)'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title("Répartition des tranches de salaire")
plt.xlabel("Tranches de salaire")
plt.ylabel("Nombre d'étudiants")
plt.xticks(rotation=45)
plt.show()

# Taux de poursuite d'études en fonction de la formation
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Formation 2023/2024', hue='Situation après Licence pro', palette='coolwarm')
plt.title("Taux de poursuite d'études selon la formation")
plt.xlabel("Formation")
plt.ylabel("Nombre d'étudiants")
plt.xticks(rotation=45)
plt.legend(title="Situation après LP")
plt.show()

# Salaire moyen en fonction de la formation
df_salaire = df[df['Rémunération (tranche salaire)'] != "vide"]
df_salaire['Salaire moyen'] = df_salaire['Rémunération (tranche salaire)'].map({
    "]1500-1700]": 1600,
    "]1700-1900]": 1800,
    "]1900-2100]": 2000,
    "]2100-2300]": 2200,
    "]2300-2500]": 2400,
    "]supérieur à 2500]": 2600
})

plt.figure(figsize=(10, 6))
sns.barplot(data=df_salaire, x='Formation 2023/2024', y='Salaire moyen', palette='viridis')
plt.title("Salaire moyen en fonction de la formation")
plt.xlabel("Formation")
plt.ylabel("Salaire moyen (€)")
plt.xticks(rotation=45)
plt.show()
