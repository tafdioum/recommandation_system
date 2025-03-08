import pandas as pd

def load_data(data_path):
    """
    Charge les données à partir d'un fichier CSV.

    :param data_path: Chemin vers le fichier CSV.
    :return: DataFrame contenant les données.
    """
    return pd.read_csv(data_path)

def get_movie_titles(data):
    """
    Retourne la liste des titres de films.

    :param data: DataFrame contenant les données.
    :return: Liste des titres de films.
    """
    return data['title'].tolist()

def get_movie_genres(data):
    """
    Retourne la liste des genres de films.

    :param data: DataFrame contenant les données.
    :return: Liste des genres de films.
    """
    return data['genre'].tolist()

def get_movie_by_id(data, movie_id):
    """
    Retourne les informations d'un film spécifique par son ID.

    :param data: DataFrame contenant les données.
    :param movie_id: ID du film à rechercher.
    :return: DataFrame contenant les informations du film.
    """
    return data[data['movie_id'] == movie_id]

def get_movies_by_genre(data, genre):
    """
    Retourne la liste des films d'un genre spécifique.

    :param data: DataFrame contenant les données.
    :param genre: Genre des films à rechercher.
    :return: DataFrame contenant les films du genre spécifié.
    """
    return data[data['genre'] == genre]