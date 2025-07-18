# app.py

import streamlit as st
from extractor import extract_attributes

# App Title
st.set_page_config(page_title="Fashion Attribute Extractor", page_icon="👗")
st.title("👗 Fashion Attribute Extractor")

# Text input area
description = st.text_area(
    "Enter Product Description:", 
    "A-line red cotton mini dress with short sleeves"
)

# Button to trigger extraction
if st.button("Extract Attributes"):
    attributes = extract_attributes(description)
    st.subheader("🧾 Extracted Attributes")
    st.json(attributes)

# Footer
st.markdown("---")
st.caption("Developed by Karthik | Streamlit App for Fashion Attribute Extraction")
