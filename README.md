# Détection de fraude bancaire

Projet de data science pour détecter des transactions frauduleuses à partir
du dataset "Credit Card Fraud Detection" (Kaggle).

## Structure du projet

```
fraude-bancaire-detection/
├── README.md              <- ce fichier
├── requirements.txt       <- dépendances Python
├── .gitignore
├── data/
│   ├── raw/               <- données brutes (creditcard.csv à placer ici)
│   └── processed/         <- données nettoyées / transformées
├── notebooks/
│   └── 01_exploration.ipynb  <- EDA (étapes 0 à 3 du guide)
├── src/
│   ├── __init__.py
│   ├── data_loader.py     <- chargement des données (étape 1)
│   ├── preprocessing.py   <- nettoyage + split train/test (étapes 3 et 5)
│   ├── features.py        <- feature engineering + rééquilibrage (étapes 4 et 6)
│   ├── train.py           <- entraînement des modèles (étape 7)
│   ├── evaluate.py        <- évaluation (étape 8)
│   └── utils.py           <- fonctions utilitaires partagées
├── models/                <- modèles entraînés sauvegardés (.pkl)
├── reports/
│   └── figures/           <- graphiques générés
└── tests/                 <- tests unitaires
```

## Installation

```bash
python -m venv venv
source venv/bin/activate      # Windows : venv\Scripts\activate
pip install -r requirements.txt
```

## Récupérer les données

1. Télécharge le dataset ici : https://www.kaggle.com/mlg-ulb/creditcardfraud
2. Place le fichier `creditcard.csv` dans `data/raw/`

## Utilisation

### 1. Exploration (à faire en premier)
Ouvre `notebooks/01_exploration.ipynb` et suis les cellules dans l'ordre.

### 2. Pipeline complet en ligne de commande
```bash
python src/train.py
python src/evaluate.py
```

## Suivi d'avancement

- [ ] Étape 0 — Définition du problème
- [ ] Étape 1 — Chargement des données (`data_loader.py`)
- [ ] Étape 2 — Exploration (`notebooks/01_exploration.ipynb`)
- [ ] Étape 3 — Nettoyage (`preprocessing.py`)
- [ ] Étape 4 — Feature engineering (`features.py`)
- [ ] Étape 5 — Split train/test (`preprocessing.py`)
- [ ] Étape 6 — Rééquilibrage des classes (`features.py`)
- [ ] Étape 7 — Entraînement des modèles (`train.py`)
- [ ] Étape 8 — Évaluation (`evaluate.py`)
- [ ] Étape 9 — Optimisation des hyperparamètres
- [ ] Étape 10 — Interprétation (feature importance / SHAP)
- [ ] Étape 11 — Conclusion et rapport
- [ ] Étape 12 — Déploiement (bonus)
