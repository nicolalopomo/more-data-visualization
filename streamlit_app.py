import streamlit as st

# Title
st.title("Streamlit :red[Metric]")

# Display player speed with positive delta value
st.metric(label="Player **Max Speed**", value="25 km/h", delta="+5.4 km/h")

# Display with a negative delta
st.metric(label="Player **Ball Possession**", value="24 min", delta="-2 min")