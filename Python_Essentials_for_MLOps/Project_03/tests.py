"""There are a file to test cases"""

import pytest

import numpy as np
import pandas as pd

from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler

from utils import *


@pytest.fixture
def fires():
    """A fixture to return a dataframe of fires."""

    return pd.read_csv("data/fires.csv")

@pytest.fixture
def fires_imputed(fires):
    imp = KNNImputer(missing_values=np.nan, n_neighbors=3)

    fires_missing = fires[fires.columns[5:13]]
    imputed = pd.DataFrame(
        imp.fit_transform(fires_missing),
        columns=fires_missing.columns
    )

    return imputed

@pytest.fixture
def fires_scaled(fires, fires_imputed):
    scaler = StandardScaler()

    fires_scaled = scaler.fit_transform(fires_imputed)
    fires_scaled = pd.DataFrame(fires_scaled, columns=fires_imputed.columns)

    return pd.concat([fires["summer"], fires_scaled], axis=1)


def test_fires_shape(fires):
    """A test to check the shape of the dataframe."""

    assert fires.shape[0] > 0
    assert fires.shape[1] > 0

def test_is_summer_month():
    """A test to check if the function is_summer_month works as expected."""

    assert is_summer_month("jun") == 1
    assert is_summer_month("jul") == 1
    assert is_summer_month("aug") == 1
    assert is_summer_month("sep") == 0

def test_fires_imputed(fires_imputed):
    """A test to check if there are any missing values."""

    assert fires_imputed.isna().sum().sum() == 0

