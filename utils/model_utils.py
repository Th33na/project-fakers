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
    "Logistic Regression": "./model/lr_pred.save",
    "Oversampled Logistic Regression": "./model/over_pred.save",
    "Random Forest": "./model/rfc.save",
    "Oversampled Random Forest": "./model/over_rfc.save",
    "Support Vector Machine": "./model/svm_pred.save",
    }

def load_models():
    models = dict()
    for key, filename in MODEL_INPUT_FILES.items():
        models[key] = joblib.load(filename) 
        
    return models

def load_scaler():
    return None
    
    
def predict(model, user_review):
    review = user_review["review"]
    
    user_review_dict={'competitor mentioned': 1, 
                  'star rating': 1, 
                  'review word count': len(user_review.split(' ')), 
                  'total votes': 5, 
                  'helpful votes': 5, 
                  'verified purchase Y': 0}
    user_review_array=list(user_review_dict.values())
    user_review_scaled=scaler.transform([user_review_array])

    model.predict(user_review_scaled)