import os
import re
import joblib
from utils.utils import get_word_count, get_mentions

MODEL_INPUT_FILES = {
    "Logistic Regression": "./model/lr_model.save",
    "Oversampled Logistic Regression": "./model/over_lr_model.save",
    "Support Vector Machine": "./model/svm_model.save",
    "Random Forest": "./model/rfc_model.save",
    "Oversampled Random Forest": "./model/over_rfc_model.save",

    }

DEFAULT_MODEL = "Logistic Regression"

SCALER_FILENAME = "./model/scaler.save"

def load_models():
    # loads the available trained models
    models = dict()
    for key, filename in MODEL_INPUT_FILES.items():
        models[key] = joblib.load(filename) 
        
    return models

def load_scaler():
    # loads the scaler for the models
    return joblib.load(SCALER_FILENAME) 
    
    
def predict(model, scaler, user_review):
    # predicts the whether a review is bias or not, depending on the model selected
    
    review = user_review.get("review", "")
    verified_purchase = 1 if user_review.get("verified_purchase", False) else 0

    user_review_dict={'competitor mentioned': get_mentions(review), 
                  'star rating': user_review.get("star_ratings", 1),
                  'review word count': get_word_count(review), 
                  'total votes': user_review.get("total_votes", 0), 
                  'helpful votes': user_review.get("helpful_votes", 0), 
                  'verified purchase': verified_purchase}

    user_review_array = list(user_review_dict.values())

    user_review_scaled = scaler.transform([user_review_array])

    prediction = model.predict(user_review_scaled)
    
    return "Not Bias" if prediction else "Bias"