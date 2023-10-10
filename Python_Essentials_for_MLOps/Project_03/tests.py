"""There are a file to test cases"""

import pytest

import pandas as pd


@pytest.fixture
def fires():
    """A fixture to return a dataframe of fires."""

    return pd.read_csv("data/fires.csv")


def test_fires_shape(fires):
    """A test to check the shape of the dataframe."""

    assert fires.shape[0] > 0
    assert fires.shape[1] > 0
