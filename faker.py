import streamlit as st
from utils.model_utils import load_models, load_scaler, MODEL_INPUT_FILES

STAR_RATINGS = range(1,6)
MODELS = MODEL_INPUT_FILES.keys()

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",   
)

st.write("Welcome to Project Fakers")
st.write("Helping you spot a bias review")

models = load_models()
scaler = load_scaler()

st.text_area("Review", key="review_string", value="", height=5, max_chars=500)
st.radio("Star Ratings", STAR_RATINGS, horizontal=True, key="star_ratings")
st.number_input("Total Votes", key="total_votes", min_value=0)
st.number_input("Helpful Votes", key="helpful_votes", min_value=0)
st.checkbox("Verified Purchase", value=False, key="verified_purchase")
st.radio("Prediction Model", MODELS, horizontal=True, key="prediction_model")







