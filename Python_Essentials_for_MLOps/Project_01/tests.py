"""There are a file to test cases"""

import pytest

import pandas as pd

from utils import clean_title


@pytest.fixture
def movie_titles():
    """A fixture to return a movie title."""
    return [
        "Toy Story",
        "Toy Story (1995)",
    ]

@pytest.fixture
def movies():
    """A fixture to return a dataframe of movies."""
    return pd.read_csv("data/ml-25m/movies.csv")

@pytest.fixture
def ratings():
    """A fixture to return a dataframe of ratings."""
    return pd.read_csv("data/ml-25m/ratings.csv")

def test_clean_title(movie_titles):
    """A test to check the clean_title function."""

    assert clean_title(movie_titles[0]) == "Toy Story"
    assert clean_title(movie_titles[1]) == "Toy Story 1995"

def test_movies_columns(movies):
    """A test to check the columns of the movies dataframe."""

    assert "movieId" in movies.columns
    assert "title" in movies.columns
    assert "genres" in movies.columns

def test_ratings_columns(ratings):
    """A test to check the columns of the ratings dataframe."""

    assert "userId" in ratings.columns
    assert "movieId" in ratings.columns
    assert "rating" in ratings.columns
    assert "timestamp" in ratings.columns

def test_movies_size(movies):
    """A test to check the size of the movies dataframe."""

    assert movies.shape[0] > 0
    assert movies.shape[1] > 0

def test_ratings_size(ratings):
    """A test to check the size of the ratings dataframe."""

    assert ratings.shape[0] > 0
    assert ratings.shape[1] > 0
