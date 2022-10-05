import os
import json
import re
from urllib import request
import shutil
import gzip
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import joblib

MODEL_INPUT_FILES = {
    "logistic_regression": "./model/lr_pred.save",
    "oversampled_lr": "./model/over_pred.save",
    "random_forest": "./model/rfc.save",
    "oversampled_rfc": "./model/over_rfc.save",
    "support_vector_machine": "./model/svm_pred.save",
    }

def load_models():
    models = dict()
    for key, filename in MODEL_INPUT_FILES.items():
        models[key] = joblib.load(filename) 
    