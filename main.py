import streamlit as st
import nltk
import os

st.title("Check NLTK Data Path")

# I-print lahat ng possible paths
st.write("NLTK Data Paths:")
st.write(nltk.data.path)

# I-check kung available ang 'punkt'
try:
    punkt_path = nltk.data.find('tokenizers/punkt')
    st.success(f"'punkt' found at: {punkt_path}")
except LookupError:
    st.error("'punkt' NOT found! You might need to check the path.")

# I-check kung available ang 'stopwords'
try:
    stopwords_path = nltk.data.find('corpora/stopwords')
    st.success(f"'stopwords' found at: {stopwords_path}")
except LookupError:
    st.error("'stopwords' NOT found!")
