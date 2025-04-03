import streamlit as st
import pandas as pd
import numpy as np

# Generate Dataset of 5 Football Players
players = ["Lionel Messi", "Cristiano Ronaldo", "Neymar Jr", "Kylian Mbappe", "Kevin De Bruyne"]
goals = np.random.randint(10, 30, size=5)
assists = np.random.randint(10, 50, size=5)
matches =  np.random.randint(10, 40, size=5)
average_distance =  np.random.rand(5) * 10
pass_accuracy = np.random.rand(5) * 100

data = {
    "Player Name": players,
    "Goals Scored": goals,
    "Assists": assists,
    "Matches Played": matches,
    "Average Distance Covered [km]": average_distance,
    "Pass Accuracy [%]": pass_accuracy
}

df = pd.DataFrame(data)

# Goals
st.title("Goals")
st.bar_chart(df.set_index("Player Name")["Goals Scored"])

# Matches
st.title("Matches and Assists")
match_assist_data = df[["Player Name", "Matches Played", "Assists"]]
st.line_chart(match_assist_data.set_index("Player Name"))

# Accuracy and Distance Covered
st.title("Pass Accuracy and Distance Covered")
accuracy_distance_data = df[["Player Name", "Pass Accuracy [%]", "Average Distance Covered [km]"]]
st.area_chart(accuracy_distance_data.set_index("Player Name"))

# Interactive Element:
st.title("Select a Player to View Individual Stats")
selected_player = st.selectbox("Choose a Player", df["Player Name"])

# Display Selected Player's Stats
index_selected_player = df["Player Name"] == selected_player
player_stats = df[index_selected_player]
st.write(player_stats.set_index("Player Name").T)