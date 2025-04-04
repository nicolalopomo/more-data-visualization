import streamlit as st

# Dataset
team_name = "Barcelona United"
seasons = ["2020-21", "2021-22", "2022-23", "2023-24"]
wins = [20, 22, 18, 25]
losses = [10, 8, 12, 5]
goals_scored = [60, 65, 55, 70]

top_scorers = {"Messi": 15, "Pelè": 12, "Maradona": 10}

# Some Info
st.title("Sports Team Performance Dashboard")
st.header(team_name)

# Columns
col1, col2 = st.columns(2)
with col1:
    st.write("Sport: Soccer")
with col2:
    st.write("City: Barcelona")

# Tabs
tab1, tab2 = st.tabs(["Season Performance", "Player Stats"])

with tab1:
    st.subheader("Season Performance")
    # Create line chart for wins
    wins_data = {"Seasons": seasons, "Wins": wins}
    st.line_chart(wins_data, x="Seasons", y="Wins")

    # Create bar chart for losses
    losses_data = {"Seasons": seasons, "Losses": losses}
    st.bar_chart(losses_data, x="Seasons", y="Losses")

with tab2:
    st.subheader("Top Scorers")
    st.bar_chart(top_scorers)

# Expander
with st.expander("Goals Scored per Season"):
    st.subheader("Goals Scored")
    for i in range(len(seasons)):
        st.write(f"{seasons[i]}: {goals_scored[i]} goals")