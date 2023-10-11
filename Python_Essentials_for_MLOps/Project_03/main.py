"""This is the main script for Project 03."""

import sys
import logging

import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoCV, RidgeCV
from sklearn.model_selection import cross_val_score

from utils import download_csv, is_summer_month

sys.dont_write_bytecode = True


DATA_URL = "https://dsserver-prod-resources-1.s3.amazonaws.com/764/fires.csv"

logging.basicConfig(filename="main.log", level=logging.INFO, format="%(asctime)s - %(message)s")
logging.getLogger("urllib3").setLevel(logging.WARNING)

download_csv(DATA_URL, "./data/fires.csv")

fires = pd.read_csv("./data/fires.csv")
fires["summer"] = [is_summer_month(m) for m in fires["month"]]
fires["log_area"] = np.log(fires["area"] + 1)
fires_reference = fires[["wind", "temp", "area"]].dropna()
reference_X = fires_reference[["wind", "temp"]]
reference = LinearRegression()
imp = KNNImputer(missing_values=np.nan, n_neighbors=3)
fires_missing = fires[fires.columns[5:13]]
fires_imputed = pd.DataFrame(
    imp.fit_transform(fires_missing),
    columns=fires_missing.columns
)
scaler = StandardScaler()
fires_scaled = scaler.fit_transform(fires_imputed)
fires_scaled = pd.DataFrame(
    fires_scaled,
    columns=fires_imputed.columns
)
fires_final = pd.concat([
    fires["summer"],
    fires_scaled
], axis=1)
y = fires["log_area"]

sfs_model = LinearRegression()
sfs_model2 = LinearRegression()
sfs_model3 = LinearRegression()

forward2 = SequentialFeatureSelector(
    estimator=sfs_model,
    n_features_to_select=2,
    direction="forward"
)

forward4 = SequentialFeatureSelector(
    estimator=sfs_model2,
    n_features_to_select=4,
    direction="forward"
)

forward6 = SequentialFeatureSelector(
    estimator=sfs_model3,
    n_features_to_select=6,
    direction="forward"
)

forward2.fit(fires_final, y)
forward4.fit(fires_final, y)
forward6.fit(fires_final, y)

print("=== FORWARD SELECTION ===")
print("Features selected in 2 feature model:", forward2.get_feature_names_out())
print("Features selected in 4 feature model:", forward4.get_feature_names_out())
print("Features selected in 6 feature model:", forward6.get_feature_names_out())
print('\n')

backward2 = SequentialFeatureSelector(
    estimator=sfs_model,
    n_features_to_select=2,
    direction="backward"
)

backward4 = SequentialFeatureSelector(
    estimator=sfs_model,
    n_features_to_select=4,
    direction="backward"
)

backward6 = SequentialFeatureSelector(
    estimator=sfs_model,
    n_features_to_select=6,
    direction="backward"
)

backward2.fit(fires_final, y)
backward4.fit(fires_final, y)
backward6.fit(fires_final, y)

print("=== BACKWARD SELECTION ===")
print("Features selected in 2 feature model:", backward2.get_feature_names_out())
print("Features selected in 4 feature model:", backward4.get_feature_names_out())
print("Features selected in 6 feature model:", backward6.get_feature_names_out())
print('\n')

fw2_model = LinearRegression().fit(fires_final[forward2.get_feature_names_out()], y)
fw4_model = LinearRegression().fit(fires_final[forward4.get_feature_names_out()], y)
fw6_model = LinearRegression().fit(fires_final[forward6.get_feature_names_out()], y)

bw2_model = LinearRegression().fit(fires_final[backward2.get_feature_names_out()], y)
bw4_model = LinearRegression().fit(fires_final[backward4.get_feature_names_out()], y)
bw6_model = LinearRegression().fit(fires_final[backward6.get_feature_names_out()], y)


ridge = RidgeCV(alphas = np.linspace(1, 10000, num=1000))
lasso = LassoCV(alphas = np.linspace(1, 10000, num=1000))

ridge.fit(fires_final, y)
lasso.fit(fires_final, y)

print("Ridge tuning parameter: ", ridge.alpha_)
print("LASSO tuning parameter: ", lasso.alpha_)
print("Ridge coefficients: ", ridge.coef_)
print("LASSO coefficients: ", lasso.coef_)
print('\n')

reference_cv = cross_val_score(
    reference,
    fires_final[["wind", "temp"]],
    y,
    cv = 5,
    scoring = "neg_mean_squared_error"
)
fw2_cv = cross_val_score(
    fw2_model,
    fires_final[forward2.get_feature_names_out()],
    y,
    cv = 5,
    scoring = "neg_mean_squared_error"
)
fw4_cv = cross_val_score(
    fw4_model,
    fires_final[forward4.get_feature_names_out()],
    y,
    cv = 5,
    scoring = "neg_mean_squared_error"
)
fw6_cv = cross_val_score(
    fw6_model,
    fires_final[forward6.get_feature_names_out()],
    y,
    cv = 5,
    scoring = "neg_mean_squared_error"
)
bw2_cv = cross_val_score(
    bw2_model,
    fires_final[backward2.get_feature_names_out()],
    y,
    cv = 5,
    scoring = "neg_mean_squared_error"
)
bw4_cv = cross_val_score(
    bw4_model,
    fires_final[backward4.get_feature_names_out()],
    y,
    cv = 5,
    scoring = "neg_mean_squared_error"
)
bw6_cv = cross_val_score(
    bw6_model,
    fires_final[backward6.get_feature_names_out()],
    y,
    cv = 5,
    scoring = "neg_mean_squared_error"
)
ridge_cv = cross_val_score(
    ridge,
    fires_final,
    y,
    cv = 5,
    scoring = "neg_mean_squared_error"
)

print("=== CROSS VALIDATION ===")
print("Reference Model, Avg Test MSE: ", np.mean(reference_cv), " SD: ", np.std(reference_cv))
print("Forward-2 Model, Avg Test MSE: ", np.mean(fw2_cv), " SD: ", np.std(fw2_cv))
print("Forward-4 Model, Avg Test MSE: ", np.mean(fw4_cv), " SD: ", np.std(fw4_cv))
print("Forward-6 Model, Avg Test MSE: ", np.mean(fw6_cv), " SD: ", np.std(fw6_cv))
print("Backward-2 Model, Avg Test MSE: ", np.mean(bw2_cv), " SD: ", np.std(bw2_cv))
print("Backward-4 Model, Avg Test MSE: ", np.mean(bw4_cv), " SD: ", np.std(bw4_cv))
print("Backward-6 Model, Avg Test MSE: ", np.mean(bw6_cv), " SD: ", np.std(bw6_cv))
print("Ridge Model, Avg Test MSE: ", np.mean(bw6_cv), " SD: ", np.std(bw6_cv))
