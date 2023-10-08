"""There are a few helper functions in this file that are used in the main.py file."""

import re

import numpy as np
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

def clean_title(title: str) -> str:
    """
    Remove alphanumeric characters and spaces from a string.

    Args:
        title (str): The string to be processed.

    Returns:
        str: The resulting string after removing the characters.
    """

    return re.sub("[^a-zA-Z0-9 ]", "", title)

def search(title: str, movies: pd.DataFrame, vectorizer, tfidf, output_size: int) -> pd.DataFrame:
    """
    Search for similarity scores between the given title and a set of titles represented as vectors.

    Args:
        title (str): The input title to compare against a set of titles.

    Returns:
        pd.DataFrame: A dataframe containing the top 5 most similar titles.
    """

    title = clean_title(title)
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(tfidf, query_vec).flatten()
    indices = np.argpartition(similarity, -output_size)[-output_size:]
    results = movies.iloc[indices][::-1]

    return results

def find_similar_movies(
        movie_title: str,
        movies: pd.DataFrame,
        ratings: pd.DataFrame,
        tfidf_vectorizer: dict,
        output_size: int
    ) -> pd.DataFrame:
    """
    Find similar movies based on the given movie ID.

    Args:
        movie_id (int): The ID of the movie to find similar movies for.

    Returns:
        pd.DataFrame: A dataframe containing the top 10 most similar movies.
    """

    search_results = search(
        movie_title, movies, tfidf_vectorizer["vectorizer"],
        tfidf_vectorizer["tfidf"], output_size
    )
    movie_id = search_results.iloc[0]["movieId"]

    similar_users = ratings[
        (ratings["movieId"] == movie_id) &
        (ratings["rating"] > 4)
    ]["userId"].unique()

    similar_user_recs = ratings[
        (ratings["userId"].isin(similar_users)) &
        (ratings["rating"] > 4)
    ]["movieId"]

    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)

    similar_user_recs = similar_user_recs[similar_user_recs > .10]

    all_users = ratings[
        (ratings["movieId"].isin(similar_user_recs.index)) &
        (ratings["rating"] > 4)
    ]

    all_user_recs = all_users["movieId"].value_counts() / len(all_users["userId"].unique())

    rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
    rec_percentages.columns = ["similar", "all"]

    rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
    rec_percentages = rec_percentages.sort_values("score", ascending=False)

    return rec_percentages.head(output_size).merge(
        movies, left_index=True, right_on="movieId"
    )[["score", "title", "genres"]]
