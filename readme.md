# Rapport - Attrape Marceau

Ce fichier décrit la méthodologie de travail employée pour réaliser le projet technique "Attrape Marceau". 
Il explique les étapes de développement, les défis rencontrés, et les apprentissages clés issus de cette expérience.

## Méthodologie de Travail

### 1. **Planification**

- Lecture et compréhension des spécifications du projet.
- Division des tâches en modules clés (gestion des entrées utilisateur, logique de jeu, affichage des images).
- Création d'un plan à partir des classes : 
  - `Player` pour le joueur.
  - `Marceau` pour les objets à attraper.
  - `Boost` pour les bonus.
  - `main` pour la logique principale et l’interaction entre composants.

### 2. **Développement**

#### Outils et Ressources Utilisés
- **Pygame** : Bibliothèque pour la gestion des graphismes et des entrées utilisateur.
- **Documentation Pygame** : Consultation régulière pour comprendre les méthodes et classes préexistantes.

#### Étapes
1. Initialisation de la fenêtre et mise en place d'une boucle principale pour le jeu.
2. Création des classes `Player`, `Marceau` et `Boost` pour encapsuler la logique de chaque entité.
3. Mise en place des collisions pour détecter l’interaction entre les objets.
4. Ajout des niveaux de difficulté et des écrans de début/fin.

### 3. **Test et Validation**
- Test du jeu pour vérifier le bon fonctionnement des interactions.
- Debugging des problèmes de collisions et de gestion du boost (pas encore tout a fait au point).
- Validation des performances (vitesse).

## Difficultés Rencontrées

### 1. **Gestion des collisions**
- **Problème** : Comprendre et implémenter la détection des collisions entre différents types d'objets.
- **Solution** : Utilisation des rectangles (`pygame.Rect`) pour simplifier la gestion des collisions.


### 2. **Gestion des boosts**
- **Problème** : Implémenter une logique pour augmenter temporairement la vitesse du joueur et la réinitialiser après une durée précise.
- **Solution** : Introduction d'un compteur (`boost_duration`) décrémenté à chaque frame.

## Résultats et Apports Pédagogiques

### Apports Techniques
- **Maîtrise des bases de Pygame**
- **Conception Orientée Objet**

### Perspectives d’Amélioration
- Ajouter plus de niveaux et de mécanismes de jeu.
- Améliorer les graphismes pour une meilleure expérience visuelle.
- Implémenter un système de sauvegarde des scores.

🐼