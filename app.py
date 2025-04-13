import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tennis Box Scheduler", layout="centered")

st.image("logo.png", width=150)
st.title("Tennis Box Scheduler")
st.markdown("Upload or use the default player list below:")

# Load or upload players
uploaded_file = st.file_uploader("Upload player CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("players.csv")

st.dataframe(df)

if st.button("Generate Matches"):
    st.success("Match schedule generation will go here.")
