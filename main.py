import streamlit as st
from extract_image import get_image, get_title



st.write("")
st.image("image.jpg")

st.write(get_image())

