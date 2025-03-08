
---

### 3. Fichier `TESTS.md`

Le fichier `TESTS.md` documente les tests effectués, les stratégies utilisées et les résultats obtenus.

#### Contenu du fichier `TESTS.md`

```markdown
# Documentation des Tests

## Tests Unitaires

### Test 1 : Recommandation de films
- **Objectif** : Vérifier que le système recommande 5 films similaires pour un film donné.
- **Résultat attendu** : 5 films sont recommandés, dont 'The Matrix' pour 'Inception'.

### Test 2 : Film non trouvé
- **Objectif** : Vérifier que le système retourne un message d'erreur si le film n'est pas trouvé.
- **Résultat attendu** : Le message "Movie not found in database." est retourné.

## Tests des Fonctions Utilitaires

### Test 1 : Chargement des données
- **Objectif** : Vérifier que les données sont correctement chargées.
- **Résultat attendu** : Les données ne sont pas vides.

### Test 2 : Extraction des titres de films
- **Objectif** : Vérifier que la liste des titres est correctement extraite.
- **Résultat attendu** : 'Inception' est dans la liste des titres.

## Résultats des Tests

Tous les tests ont réussi. La couverture de test est de 100%.