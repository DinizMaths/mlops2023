"""The main module for the Movie Recommender System."""

import sys
import os
import zipfile
import logging
import requests

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from tqdm import tqdm

from utils import clean_title, find_similar_movies


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

movies["clean_title"] = movies["title"].apply(clean_title)
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
tfidf = vectorizer.fit_transform(movies["clean_title"])

tfidf_vectorizer = {
    "vectorizer": vectorizer,
    "tfidf": tfidf
}

print(find_similar_movies(MOVIE_TITLE, movies, ratings, tfidf_vectorizer, SIZE))
