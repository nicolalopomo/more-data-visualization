import streamlit as st

teaching_page = st.Page("teaching.py", title="Teaching")
training01_page = st.Page("training01.py", title="Training 01")
training02_page = st.Page("training02.py", title="Training 02")

pg = st.navigation([teaching_page, training01_page, training02_page])
st.set_page_config(page_title="Exercitation on Data Viz")


# Sidebar
# Object notation
st.sidebar.selectbox(
    "Select your favourite player",
    ('Messi','Ronaldo','Maradona'),
    key="FavPlayer"
    )


# With notation
with st.sidebar:
    add_radiobutton = st.radio(
    "Select your favourite team",
    ('Juve','Milan','Inter'),
    key="FavTeam"
    )


pg.run()