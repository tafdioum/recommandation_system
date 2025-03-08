import sys
import os

# Ajouter le répertoire src/ au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import load_data, get_movie_titles, get_movies_by_genre

# Chemin vers le fichier de données
data_path = "C:\\Users\\Dioum7794\\OneDrive - Orange Sonatel\\Documents\\travaux EIS\\COURS\\COURS MASTER\\2ième ANNEE\\TEST LOGICIEL\\Projet_Final\\data\\movies.csv"

# Charger les données
data = load_data(data_path)

# Obtenir la liste des titres de films
titles = get_movie_titles(data)
print("Titres des films :", titles[:10])  # Affiche les 10 premiers titres

# Obtenir la liste des films d'un genre spécifique
action_movies = get_movies_by_genre(data, "Action")
print("Films d'action :", action_movies)