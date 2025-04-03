import streamlit as st

teaching_page = st.Page("teaching.py", title="Teaching")
training01_page = st.Page("training01.py", title="Training 01")

pg = st.navigation([teaching_page, training01_page])
st.set_page_config(page_title="Exercitation")
pg.run()