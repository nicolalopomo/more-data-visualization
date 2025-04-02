import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Streamlit :red[Metric]")

# Display player speed with positive delta value
st.metric(label="Player **Max Speed**", value="25 km/h", delta="+5.4 km/h")

# Display with a negative delta
st.metric(label="Player **Ball Possession**", value="24 min", delta="-2 min")


# Title
st.title("Interactive :blue[Data Table]")

# Generate sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [25, 30, 35, 40, 22],
    "Salary": [50000, 60000, 70000, 80000, 45000],
    "Department": ["HR", "IT", "Finance", "IT", "Marketing"]
}

df = pd.DataFrame(data)

# Display the DataFrame as an interactive table
st.dataframe(df)

# Alternative: Display a static table (if interaction is not needed)
st.write("Static Table:")
st.table(df)
