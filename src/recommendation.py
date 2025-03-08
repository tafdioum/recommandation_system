import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationSystem:
    def __init__(self):
        """
        Initialise le système de recommandation avec les données.
        Le chemin du fichier est codé en dur dans le code.
        """
        # Chemin du fichier de données (codé en dur)
        data_path = "C:\\Users\\Dioum7794\\OneDrive - Orange Sonatel\\Documents\\travaux EIS\\COURS\\COURS MASTER\\2ième ANNEE\\TEST LOGICIEL\\Projet_Final\\data\\movies.csv"
        
        # Charger les données
        self.data = pd.read_csv(data_path)
        
        # Vectoriser les genres des films
        self.vectorizer = TfidfVectorizer()
        self.genre_matrix = self.vectorizer.fit_transform(self.data['genre'])

    def recommend(self, movie_title, top_n=5):
        """
        Recommande des films similaires à un film donné.

        :param movie_title: Titre du film pour lequel faire une recommandation.
        :param top_n: Nombre de films à recommander (par défaut 5).
        :return: DataFrame des films recommandés ou un message d'erreur.
        """
        # Vérifie si le film existe dans la base de données
        if movie_title not in self.data['title'].values:
            return "Movie not found in database."

        # Trouve l'index du film
        movie_index = self.data[self.data['title'] == movie_title].index[0]
        
        # Calcule la similarité cosinus entre ce film et les autres
        movie_vector = self.genre_matrix[movie_index]
        similarity_scores = cosine_similarity(movie_vector, self.genre_matrix).flatten()
        
        # Trie les films par similarité (du plus similaire au moins similaire)
        similar_movie_indices = similarity_scores.argsort()[-top_n-1:-1][::-1]

        # Retourne les films recommandés
        return self.data.iloc[similar_movie_indices]