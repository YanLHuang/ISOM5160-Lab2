

import streamlit as st
from transformers import pipeline

# Load the text classification model
@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="Aaqib099/distilbert-phishing-detection",
        device=-1
    )

classifier = load_model()

# Streamlit application title
st.title("Text Classification for you")
st.write("Classification for whether a phishing email or not")

# Text input
text = st.text_area("Enter the text to classify", "")

# Perform text classification
if st.button("Classify"):
    if text.strip():
        results = classifier(text, top_k=None)

        # Find the highest score
        max_score = float("-inf")
        max_label = ""

        for result in results:
            if result["score"] > max_score:
                max_score = result["score"]
                max_label = result["label"]

        st.write("Text:", text)
        st.write("Label:", max_label)
        st.write("Score:", max_score)
    else:
        st.warning("Please enter some text.")

