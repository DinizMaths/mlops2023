"""The main module for the Movie Recommender System."""

import sys
import os
import re
import zipfile
import logging
import requests

import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from tqdm import tqdm


logging.basicConfig(level=logging.INFO)
logging.getLogger("urllib3").setLevel(logging.WARNING)

ZIP_URL = "https://files.grouplens.org/datasets/movielens/ml-25m.zip"
ZIP_PATH = "data/movies"
EXTRACT_DIR = "data/"


if os.path.exists("data/ml-25m/movies.csv") and os.path.exists("data/ml-25m/ratings.csv"):
    logging.info("🟩 Files already exists!")
else:
    try:
        if not os.path.exists("data"):
            os.mkdir("data")

        response = requests.get(ZIP_URL, stream=True, timeout=240)

        logging.info("🟩 Downloading...")

        with open(ZIP_PATH, "wb") as zip_file:
            with tqdm(
                total=int(response.headers.get("content-length", 0)),
                unit="B", unit_scale=True, unit_divisor=1024
            ) as pbar:
                for data in response.iter_content(chunk_size=1024):
                    pbar.update(len(data))
                    zip_file.write(data)

        logging.info("🟩 Download Success!")
        logging.info("🟩 Extracting...")

        with zipfile.ZipFile(ZIP_PATH, 'r') as zip_file:
            file_list = zip_file.namelist()
            with tqdm(total=len(file_list), unit="files") as pbar:
                for file_name in file_list:
                    zip_file.extract(file_name, EXTRACT_DIR)
                    pbar.update(1)

        logging.info("🟩 Extraction Success!")


    except requests.exceptions.RequestException as request_error:
        logging.error("🟥 Download Failed!")
        logging.error("🟥 Error: %s", request_error)

    except zipfile.BadZipFile as zip_error:
        logging.error("🟥 Failed to extract ZIP file!")
        logging.error("🟥 Error: %s", zip_error)


if "--movie-title" not in sys.argv:
    logging.error("🟥 --movie-name argument is required")

    raise SystemExit(1)

if len(sys.argv) < 3:
    logging.error("🟥 need to pass the movie name as argument for --movie-name")

    raise SystemExit(1)

MOVIE_TITLE = sys.argv[sys.argv.index("--movie-title") + 1]
SIZE = int(sys.argv[sys.argv.index("--size") + 1]) if "--size" in sys.argv else 5

movies  = pd.read_csv("./data/ml-25m/movies.csv")
ratings = pd.read_csv("./data/ml-25m/ratings.csv")

def clean_title(title: str) -> str:
    """
    Remove alphanumeric characters and spaces from a string.

    Args:
        title (str): The string to be processed.

    Returns:
        str: The resulting string after removing the characters.
    """

    return re.sub("[^a-zA-Z0-9 ]", "", title)

movies["clean_title"] = movies["title"].apply(clean_title)
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
tfidf = vectorizer.fit_transform(movies["clean_title"])

def search(title: str) -> pd.DataFrame:
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
    indices = np.argpartition(similarity, -SIZE)[-SIZE:]
    results = movies.iloc[indices][::-1]

    return results

def find_similar_movies(movie_title: str) -> pd.DataFrame:
    """
    Find similar movies based on the given movie ID.

    Args:
        movie_id (int): The ID of the movie to find similar movies for.

    Returns:
        pd.DataFrame: A dataframe containing the top 10 most similar movies.
    """

    search_results = search(movie_title)
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

    return rec_percentages.head(10).merge(
        movies, left_index=True, right_on="movieId"
    )[["score", "title", "genres"]]

print(find_similar_movies(MOVIE_TITLE))
