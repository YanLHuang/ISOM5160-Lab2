


import streamlit as st
from transformers import pipeline

# Load phishing email detection model
@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="Aaqib099/distilbert-phishing-detection",
        device=-1
    )

classifier = load_model()

st.title("Phishing Email Detection")
st.write("Classify whether an email is phishing or safe.")

text = st.text_area("Enter email text:", "")

if st.button("Classify"):
    if text.strip():
        result = classifier(
            text,
            truncation=True,
            max_length=256
        )[0]

        label_map = {
            "LABEL_0": "Safe Email",
            "LABEL_1": "Phishing Email"
        }

        label = label_map.get(result["label"], result["label"])

        st.write("Text:", text)
        st.write("Label:", label)
        st.write("Score:", result["score"])
    else:
        st.warning("Please enter some text.")


