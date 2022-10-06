import streamlit as st
from utils.model_utils import load_models, load_scaler, predict, validate_input_data, MODEL_INPUT_FILES, DEFAULT_MODEL

STAR_RATINGS = range(1,6)
MODELS = MODEL_INPUT_FILES.keys()
AVAILABLE_MODELS = load_models()
SCALER = load_scaler()

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",   
)


st.write("Welcome to Project Fakers")
st.write("Helping you spot a bias review")


st.text_area("Review", key="review_string", value="", height=5, max_chars=5000)
st.radio("Star Ratings", STAR_RATINGS, horizontal=True, key="star_ratings")
col1, col2 = st.columns(2)
with col1:
    st.number_input("Total Votes", key="total_votes", min_value=0)
with col2:
    st.number_input("Helpful Votes", key="helpful_votes", min_value=0)

st.checkbox("Verified Purchase", value=False, key="verified_purchase")

st.radio("Prediction Model", MODELS, horizontal=True, key="prediction_model")

if st.button("Predict", key="predict"):
    selected_model = st.session_state.prediction_model
    model_to_use = AVAILABLE_MODELS.get(selected_model, DEFAULT_MODEL)
    user_review = {
        "review": st.session_state.review_string,
        "star_ratings": st.session_state.star_ratings,
        "total_votes": st.session_state.total_votes,
        "helpful_votes": st.session_state.helpful_votes,
        "verified_purchase": st.session_state.verified_purchase
    }
    valid, message = validate_input_data(user_review)
    if valid:

        prediction = predict(model_to_use, SCALER, user_review)  

        st.write(f"Based on {selected_model}, your Review is {prediction}!")
    else:
        st.write(message)  

        


