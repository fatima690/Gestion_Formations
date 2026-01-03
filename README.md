Moujahid Fatima G2 emsi les orangers 
# Gestion_Formations (Odoo 17) – Module de Gestion des Formations

Ce dépôt contient un projet **Odoo 17** (exécuté avec **Docker Compose**) intégrant un module personnalisé **Gestion_Form** permettant de gérer un processus complet de **gestion des formations** : catalogue de formations, planification des sessions, inscriptions des participants et reporting.

## Fonctionnalités principales

### 1) Gestion des formations
- Création et gestion d’un **catalogue de formations**.
- Informations de base : nom, responsable, dates, durée, capacité, statut, description, prix, etc.
- Accès direct aux sessions associées (onglet / relation).

### 2) Gestion des sessions
- Planification des **sessions** pour une formation (dates, capacité, formateur).
- Suivi via un **workflow** (ex. brouillon → confirmée → en cours → terminée / annulée).
- Indicateurs de suivi (inscriptions / places restantes) selon la configuration du module.
- Recherche avec filtres et regroupements (selon les vues).

### 3) Gestion des inscriptions
- Création d’**inscriptions** liant un participant (`res.partner`) à une session.
- Workflow d’inscription (brouillon / confirmée / annulée, selon la configuration).
- Champs liés (related) éventuels pour faciliter le filtrage/reporting.

### 4) Participants (Contacts filtrés)
- Menu **Participants** basé sur `res.partner` (Contacts) filtré par catégorie/tag « Participant ».

### 5) Reporting
- Vues **Pivot** et **Graph** permettant d’analyser les inscriptions (par formation, session, formateur, état, etc.).

## Stack technique
- **Odoo 17**
- **PostgreSQL 16**
- **Docker / Docker Compose**
- Développement : Python (models), XML (views/actions/menus), données (demo.xml), sécurité (access rights)

## Structure du projet

- `docker-compose.yml` : définition des services Odoo + PostgreSQL
- `config/odoo.conf` : configuration Odoo (addons_path, data-dir)
- `addons/Gestion_Form/` : module personnalisé
  - `__manifest__.py` : déclaration du module (dépendances, données, vues…)
  - `models/` : modèles Python (formation, session, inscription)
  - `views/` : vues XML (formations, sessions, inscriptions, participants, reporting)
  - `security/ir.model.access.csv` : droits d’accès
  - `data/` : données de démonstration (si activées)

## Démarrage rapide (Docker)

### Prérequis
- Docker Desktop installé et lancé.

### Lancer l’environnement
Dans un terminal (Git Bash / PowerShell) :

```bash
docker compose up -d
```

Vérifier l’état des conteneurs :

```bash
docker compose ps
```

### Accéder à Odoo
Ouvrir :
- `http://localhost:8069`

### Installer / Mettre à jour le module
Dans Odoo :
- **Apps** → rechercher **Gestion_Form** / **Gestion des Formations**
- **Install** (première fois) ou **Upgrade** (après modifications)

### Logs (en cas d’erreur)
```bash
docker compose logs --tail=200 odoo17
```

## Notes
- Si le port `8069` est déjà occupé (erreur Docker « ports are not available »), modifier le mapping dans `docker-compose.yml` (ex. `8070:8069`) ou arrêter le service/conteneur qui utilise déjà 8069.

## Auteure
- Fatima (EMSI) – Projet académique ERP / Odoo
