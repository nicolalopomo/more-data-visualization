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
    "Age": [25, 30, 35, 20, 22],
    "Goal": [5, 6, 7, 8, 4],
    "Team": ["HR", "IT", "FR", "GR", "UK"]
}

df = pd.DataFrame(data)

# Display the DataFrame as an interactive table
st.dataframe(df)

# Alternative: Display a static table (if interaction is not needed)
st.write("Static Table:")
st.table(df)


# Title
st.title(":green[Line] Chart")

# Generate sample data
goals_season = np.random.randint(15, size=(40, 3)) 
players = ['Mario', 'Victor', 'Sandro']

# Create a DataFrame
df = pd.DataFrame(goals_season, columns= players)

# Display the line chart
st.line_chart(df)


# Title
st.title(":green[Area] Chart")

# Generate sample data
goals_season = np.random.randint(15, size=(40, 3)) 
players = ['Mario', 'Victor', 'Sandro']

# Create a DataFrame
df = pd.DataFrame(goals_season, columns= players)

# Display the area chart
st.area_chart(df)


# Title
st.title(":green[Bar] Chart")

# Generate sample data
goals_season = np.random.randint(15, size=(40, 3)) 
players = ['Mario', 'Victor', 'Sandro']

# Create a DataFrame
df = pd.DataFrame(goals_season, columns= players)

# Display the area chart
st.bar_chart(df)


# Title
st.title(":red[Scatter] Chart")

# Generate sample data
num_points = 50

x_coord = np.random.rand(num_points) * 100 # Random values for X-axis
y_coord = np.random.rand(num_points) * 100 # Random values for Y-axis
marker_size = np.random.rand(num_points) * 100 # Size of the points
marker_color = np.random.rand(num_points, 3) #RGB colors
color_tuples = [tuple(color) for color in marker_color]

marker_data = {
    "X Value": x_coord,
    "Y Value": y_coord,  
    "Size": marker_size,
    "Color": color_tuples
}

data = pd.DataFrame(marker_data)

# Display the scatter chart
st.scatter_chart(data, x="X Value", y="Y Value", color="Color", size="Size")



# Title
st.title(":blue[Interactive] Map")

# Generate sample data with random latitude & longitude points
num_points = 10
latitude = np.random.uniform(45.8, 45.9, num_points)  # Latitude (Lecco)
longitude = np.random.uniform(9.35, 9.45, num_points)  # Longitude
gps = {"lat": latitude, "lon": longitude}
data = pd.DataFrame(gps)

# Display the map
st.map(data)