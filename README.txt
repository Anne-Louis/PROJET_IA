1. Pour lancer le projet, depuis un terminal aller dans le répertoir PROJET_IA/
puis rentrer la commande : python main.py    ou    python3 main.py

2. Pour lancer les tests unitaires, depuis un terminal aller dans le répertoir PROJET_IA/
puis rentrer la commande : python -m unittest discover tests   ou
                           python3 -m unittest discover tests

3. ARBORESCENCE :
📦PROJET_IA
 ┣ 📂ia : Dossier contenant tout les fichiers concernant la gestion des ia
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜evaluation.py : Fonctions d'évaluation des 3 ia
 ┃ ┣ 📜ia_difficile.py : Gestion de l'ia difficile
 ┃ ┣ 📜ia_facile.py : Gestion de l'ia facile
 ┃ ┣ 📜ia_moyenne.py : Gestion de l'ia moyenne
 ┃ ┗ 📜minimax.py : Algorithme MiniMax avec élagage alphabêta
 ┃ 
 ┣ 📂jeu : Dossier contenant tout les fichiers concernant la gestion logique du jeu
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜action.py : Permet la création et la manipulation d'actions
 ┃ ┣ 📜carte.py : Permet la création et la manipulation de cartes
 ┃ ┣ 📜etatJeu.py : Coeur du projet, s'occupe de la gestion d'une partie
 ┃ ┗ 📜joueur.py : Permet la création et la manipulation de joueurs
 ┃
 ┣ 📂tests : Dossier contenant les tests unitaires
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜test_actions.py : Tests unitaires sur les actions
 ┃ ┣ 📜test_carte.py : Tests unitaires sur les cartes
 ┃ ┣ 📜test_etat_jeu.py : Tests unitaires sur la gestion de la partie
 ┃ ┣ 📜test_evaluations.py : Tests unitaires sur les fonctions d'évaluation
 ┃ ┣ 📜test_joueur.py : Tests unitaires sur les joueurs
 ┃ ┗ 📜__init__.py : Initialisation des tests
 ┃
 ┣ 📂utils
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜cartes.json : Liste des cartes sous format JSON
 ┃ ┗ 📜decks.py : Permet la création et la manipulation de decks
 ┃
 ┣ 📜main.py : Contient la boucle principale du menu et de jeu, permet de lancer le projet
 ┣ 📜README.txt : Explication pour le lancement du projet, des tests et de l'arborescence
 ┗ 📜tournoi.py : Contient la boucle permettant de lancer le tournoi entre les ia

