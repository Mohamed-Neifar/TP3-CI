# TP 3 : Intégration Continue (CI) avec FastAPI et GitHub Actions

Ce projet implémente une API REST développée avec **FastAPI**, accompagnée d'une suite de tests unitaires, d'une mesure de couverture de code et d'une analyse statique de qualité automatisées via **GitHub Actions**.

## Fonctionnalités de l'API (`main.py`)
* `GET /` : Message de bienvenue.
* `GET /addition?a=0&b=0` : Addition de deux entiers.
* `GET /soustraction?a=0&b=0` : Soustraction de deux entiers.
* `GET /greeting?name=World` : Message de salutation personnalisé.
* `POST /multiply?a=0&b=0` : Multiplication de deux entiers.
* `POST /divide?a=0&b=1` : Division de deux nombres (avec gestion de l'erreur HTTP 400 en cas de division par zéro).

## Exécution en local
```bash
# Installer les dépendances
pip install fastapi uvicorn pytest httpx pytest-cov pylint

# Lancer le serveur
python -m uvicorn main:app --reload

# Lancer les tests unitaires et la couverture de code
pytest -v --cov=. --cov-report=term-missing --junitxml=report.xml

# Vérifier la qualité du code (objectif 10/10)
pylint main.py test_main.py