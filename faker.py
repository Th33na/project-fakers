import streamlit as st
from utils.utils import load_models()

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",   
)

st.write("Welcome to Project Fakers")

models = load_models()
scaler = load_scaler()

st.text_input("Review", key="review_string")