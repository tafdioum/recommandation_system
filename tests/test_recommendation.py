import sys
import os

# Ajouter le chemin du projet au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from src.recommendation import RecommendationSystem

@pytest.fixture
def recommendation_system():
    """Fixture pour initialiser le système de recommandation."""
    return RecommendationSystem()  # Pas besoin de passer DATA_PATH

def test_recommendation(recommendation_system):
    """Teste que le système recommande des films similaires."""
    recommendations = recommendation_system.recommend("Movie 1")
    
    # Afficher les recommandations
    print("\nRecommandations pour 'Movie 1' :")
    print(recommendations)
    
    # Vérifications
    assert len(recommendations) == 5  # Vérifie que 5 films sont recommandés
    assert len(recommendations) > 0  # Vérifie qu'au moins un film est recommandé

def test_movie_not_found(recommendation_system):
    """Teste que le système gère correctement un film non trouvé."""
    result = recommendation_system.recommend("Unknown Movie")
    
    # Afficher le résultat pour un film non trouvé
    print("\nRésultat pour un film non trouvé :")
    print(result)
    
    # Vérification
    assert result == "Movie not found in database."