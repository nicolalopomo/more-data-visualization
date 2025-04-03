import streamlit as st
import pandas as pd
import numpy as np
import time as t

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


# Session state
your_name = st.text_input("Your name: ")
# Save information in the session state
st.session_state['Name'] = your_name
# Write that information
st.write(st.session_state['Name'])

# We added a key to the widget
st.number_input("Your age", min_value=18, max_value=65, value=25, step=1, key="Age")
# Write that information
st.write(st.session_state['Age'])


# Status messages
st.title("Status Messages")
# Error 
st.error("This is an error message with a custom icon.", icon="🔥")
# Warning
st.warning("This is a warning message with a custom icon.", icon="⚠️")
# Info
st.info("This is an info message with a custom icon.", icon="ℹ️")
# Success
st.success("This is a success message with a custom icon.", icon="✅")


# Progress Bar
st.title("Progress Bar")
progress_bar = st.progress(0)
status_text = st.empty()
for i in range(101):
    t.sleep(0.01)  # Simulate some work
    progress_bar.progress(i)
    status_text.write(f"Processing step {i}%")
st.success("Processing complete!")


# Progress Bar
st.title("Spinner")
with st.spinner("Wait for it...", show_time=True):
    t.sleep(2)
st.success("Done!")


# Get information from the sidebar
st.title("Info from SideBar")
st.write(st.session_state['FavPlayer'])
st.write(st.session_state['FavTeam'])


# Columns
# Object notation
st.title("Columns 1")
col1, col2 = st.columns(2)
# Col1
col1.header("A cat")
col1.image("https://static.streamlit.io/examples/cat.jpg")
# Col2
col2.header("A dog")
col2.image("https://static.streamlit.io/examples/dog.jpg")

# Columns
# With notation
st.title("Columns 2")
data2plot = np.random.rand(10, 1)
col1w, col2w = st.columns([3,1])
with col1w:
    st.header("Chart")
    st.line_chart(data2plot)
with col2w:
    st.header("Table")
    st.table(data2plot)


# Tabs
st.title("Tabs")
tab1, tab2 = st.tabs(["Cat", "Dog"])
# Tab1
tab1.subheader("A cat")
tab1.image("https://static.streamlit.io/examples/cat.jpg")
# Tab2
tab2.subheader("A dog")
tab2.image("https://static.streamlit.io/examples/dog.jpg")


# Exapanders
st.title("Expanders")
# Open
with st.expander("Chart", expanded=True):
    st.subheader("Expander with chart")
    st.line_chart(data2plot)
# Closed
with st.expander("Data", expanded=False):
    st.subheader("Expander with data")
    st.table(data2plot)
