from django.apps import AppConfig
import pandas as pd
from joblib import load
import os

class PredictionConfig(AppConfig):
    name = 'Prediction'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CLASSIFIER_FOLDER = os.path.join(BASE_DIR, 'Prediction/classifier/')
    CLASSIFIER_FILE = os.path.join(CLASSIFIER_FOLDER, "random_forest.joblib")
    DIM_REDUCTION_FILE = os.path.join(CLASSIFIER_FOLDER, "lda_dim_reduction.joblib")
    classifier = load(CLASSIFIER_FILE)
    dim_reduction = load(DIM_REDUCTION_FILE)
