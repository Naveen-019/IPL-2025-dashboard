import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page configuration
st.set_page_config(
    page_title="IPL 2025 Dashboard",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1a237e;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #616161;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #1a237e 0%, #283593 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
    }
    .metric-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    matches = pd.read_csv('matches.csv')
    deliveries = pd.read_csv('deliveries.csv')
    orange_cap = pd.read_csv('orange_cap.csv')
    purple_cap = pd.read_csv('purple_cap.csv')
    return matches, deliveries, orange_cap, purple_cap

matches, deliveries, orange_cap, purple_cap = load_data()

# Header
st.markdown('<h1 class="main-header">🏏 IPL 2025 Dashboard</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Complete Cricket Statistics & Analysis</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Matches", "Orange Cap", "Purple Cap", "Team Analysis"])

st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.info("This dashboard provides comprehensive statistics from IPL 2025 season including match results, top scorers, and leading wicket-takers.")

# Overview Page
if page == "Overview":
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Matches", len(matches))
    with col2:
        # Get tournament winner (Final match winner)
        final_match = matches[matches['stage'] == 'Final']
        if not final_match.empty:
            winner = final_match.iloc[0]['match_winner']
            st.metric("Champions", winner)
    with col3:
        top_scorer = orange_cap.iloc[0]
        st.metric("Orange Cap", f"{top_scorer['Batsman']} ({top_scorer['Runs']} runs)")
    with col4:
        top_bowler = purple_cap.iloc[0]
        st.metric("Purple Cap", f"{top_bowler['Bowler']} ({top_bowler['Wickets']} wkts)")

    st.markdown("---")

    # Top Charts Row
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏏 Top 5 Run Scorers")
        top5_scorers = orange_cap.head(5)
        fig_scorers = px.bar(
            top5_scorers,
            x='Runs',
            y='Batsman',
            orientation='h',
            color='Runs',
            color_continuous_scale='Blues',
            text='Runs'
        )
        fig_scorers.update_layout(
            height=300,
            yaxis={'categoryorder': 'total ascending'},
            showlegend=False,
            margin=dict(l=20, r=20, t=20, b=20)
        )
        fig_scorers.update_traces(textposition='outside')
        st.plotly_chart(fig_scorers, use_container_width=True)

    with col2:
        st.subheader("⚡ Top 5 Wicket Takers")
        top5_bowlers = purple_cap.head(5)
        fig_bowlers = px.bar(
            top5_bowlers,
            x='Wickets',
            y='Bowler',
            orientation='h',
            color='Wickets',
            color_continuous_scale='Oranges',
            text='Wickets'
        )
        fig_bowlers.update_layout(
            height=300,
            yaxis={'categoryorder': 'total ascending'},
            showlegend=False,
            margin=dict(l=20, r=20, t=20, b=20)
        )
        fig_bowlers.update_traces(textposition='outside')
        st.plotly_chart(fig_bowlers, use_container_width=True)

    # Points Table
    st.subheader("📊 Points Table")
    
    # Calculate points table from matches data
    teams_stats = {}
    for team in matches['team1'].unique():
        teams_stats[team] = {'P': 0, 'W': 0, 'L': 0, 'T': 0, 'NR': 0, 'Pts': 0, 'For': 0, 'Against': 0}

    for _, match in matches.iterrows():
        if match['match_result'] == 'tied' or pd.isna(match['match_result']):
            continue
        
        team1, team2 = match['team1'], match['team2']
        winner = match['match_winner']
        
        if team1 in teams_stats and team2 in teams_stats:
            teams_stats[team1]['P'] += 1
            teams_stats[team2]['P'] += 1
            
            # Calculate runs for and against
            teams_stats[team1]['For'] += match['first_ings_score'] if match['team1'] == team1 else match['second_ings_score']
            teams_stats[team1]['Against'] += match['second_ings_score'] if match['team1'] == team1 else match['first_ings_score']
            teams_stats[team2]['For'] += match['second_ings_score'] if match['team1'] == team1 else match['first_ings_score']
            teams_stats[team2]['Against'] += match['first_ings_score'] if match['team1'] == team1 else match['second_ings_score']
            
            if winner == 'Draw' or pd.isna(winner):
                teams_stats[team1]['T'] += 1
                teams_stats[team2]['T'] += 1
                teams_stats[team1]['Pts'] += 1
                teams_stats[team2]['Pts'] += 1
            elif winner == team1:
                teams_stats[team1]['W'] += 1
                teams_stats[team2]['L'] += 1
                teams_stats[team1]['Pts'] += 2
            elif winner == team2:
                teams_stats[team2]['W'] += 1
                teams_stats[team1]['L'] += 1
                teams_stats[team2]['Pts'] += 2

    # Create DataFrame and calculate NRR
    points_df = pd.DataFrame(teams_stats).T
    points_df.index.name = 'Team'
    points_df['NRR'] = ((points_df['For'] / 20) - (points_df['Against'] / 20)).round(2)
    points_df = points_df.sort_values(['Pts', 'NRR'], ascending=[False, False]).reset_index()
    points_df.index = range(1, len(points_df) + 1)
    
    # Display points table
    st.dataframe(
        points_df[['Team', 'P', 'W', 'L', 'T', 'NR', 'Pts', 'NRR']],
        use_container_width=True,
        hide_index=False
    )

# Matches Page
elif page == "Matches":
    st.subheader("📋 Match Results")
    
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        stage_filter = st.selectbox("Filter by Stage", ["All", "League", "Playoffs", "Final"])
    with col2:
        team_filter = st.selectbox("Filter by Team", ["All"] + list(matches['team1'].unique()))
    
    # Apply filters
    filtered_matches = matches.copy()
    if stage_filter != "All":
        filtered_matches = filtered_matches[filtered_matches['stage'] == stage_filter]
    if team_filter != "All":
        filtered_matches = filtered_matches[
            (filtered_matches['team1'] == team_filter) | 
            (filtered_matches['team2'] == team_filter)
        ]
    
    # Display matches
    display_df = filtered_matches[['match_id', 'date', 'venue', 'team1', 'team2', 'match_winner', 'player_of_the_match']].copy()
    display_df.columns = ['Match', 'Date', 'Venue', 'Team 1', 'Team 2', 'Winner', 'Player of Match']
    
    st.dataframe(display_df, use_container_width=True)
    
    # Match statistics
    st.subheader("📈 Match Statistics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Matches", len(filtered_matches))
    col2.metric("Highest Score", f"{matches['first_ings_score'].max()}/{matches['second_ings_score'].max()}")
    col3.metric("Matches with 200+", len(matches[(matches['first_ings_score'] >= 200) | (matches['second_ings_score'] >= 200)]))

# Orange Cap Page
elif page == "Orange Cap":
    st.subheader("🏏 Orange Cap - Top Run Scorers")
    
    # Display full table
    st.dataframe(orange_cap, use_container_width=True)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Runs Comparison")
        fig = px.bar(
            orange_cap.head(10),
            x='Batsman',
            y='Runs',
            color='Runs',
            color_continuous_scale='Blues',
            text='Runs'
        )
        fig.update_layout(height=400, showlegend=False)
        fig.update_traces(textposition='outside')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Strike Rate Comparison")
        fig = px.scatter(
            orange_cap,
            x='Batsman',
            y='Strike_rate',
            size='Runs',
            color='Strike_rate',
            color_continuous_scale='Viridis',
            hover_data=['Innings', 'Average', 'Hundreds', 'Fifties']
        )
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    # Detailed stats
    st.subheader("📊 Detailed Batting Statistics")
    selected_player = st.selectbox("Select Player", orange_cap['Batsman'].tolist())
    player_data = orange_cap[orange_cap['Batsman'] == selected_player].iloc[0]
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Runs", player_data['Runs'])
    col2.metric("Average", player_data['Average'])
    col3.metric("Strike Rate", player_data['Strike_rate'])
    col4.metric("Highest Score", player_data['Highest_score'])

# Purple Cap Page
elif page == "Purple Cap":
    st.subheader("⚡ Purple Cap - Top Wicket Takers")
    
    # Display full table
    st.dataframe(purple_cap, use_container_width=True)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Wickets Comparison")
        fig = px.bar(
            purple_cap.head(10),
            x='Bowler',
            y='Wickets',
            color='Wickets',
            color_continuous_scale='Oranges',
            text='Wickets'
        )
        fig.update_layout(height=400, showlegend=False)
        fig.update_traces(textposition='outside')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Economy Rate Comparison")
        fig = px.scatter(
            purple_cap,
            x='Bowler',
            y='Economy_rate',
            size='Wickets',
            color='Economy_rate',
            color_continuous_scale='RdBu',
            hover_data=['Overs', 'Runs', 'Four_wicket_haul']
        )
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    # Detailed stats
    st.subheader("📊 Detailed Bowling Statistics")
    selected_bowler = st.selectbox("Select Bowler", purple_cap['Bowler'].tolist())
    bowler_data = purple_cap[purple_cap['Bowler'] == selected_bowler].iloc[0]
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Wickets", bowler_data['Wickets'])
    col2.metric("Economy", bowler_data['Economy_rate'])
    col3.metric("Best Figures", bowler_data['Best_bowling_figure'])
    col4.metric("4W/5W", f"{bowler_data['Four_wicket_haul']}/{bowler_data['Five_wicket_hall']}")

# Team Analysis Page
elif page == "Team Analysis":
    st.subheader("📊 Team-wise Analysis")
    
    # Calculate team statistics from deliveries
    team_stats = {}
    
    for team in matches['team1'].unique():
        team_matches = matches[(matches['team1'] == team) | (matches['team2'] == team)]
        wins = len(team_matches[team_matches['match_winner'] == team])
        
        # Get runs scored and wickets taken from deliveries
        team_deliveries = deliveries[
            (deliveries['batting_team'] == team) | (deliveries['bowling_team'] == team)
        ]
        
        runs_scored = team_deliveries[team_deliveries['batting_team'] == team]['runs_of_bat'].sum()
        wickets_taken = len(team_deliveries[
            (team_deliveries['bowling_team'] == team) & 
            (team_deliveries['wicket_type'] != '') &
            (team_deliveries['wicket_type'] != '0')
        ])
        
        team_stats[team] = {
            'Matches': len(team_matches),
            'Wins': wins,
            'Losses': len(team_matches) - wins,
            'Win %': round((wins / len(team_matches)) * 100, 1) if len(team_matches) > 0 else 0,
            'Total Runs': runs_scored,
            'Total Wickets': wickets_taken
        }
    
    teams_df = pd.DataFrame(team_stats).T
    teams_df.index.name = 'Team'
    teams_df = teams_df.sort_values('Win %', ascending=False).reset_index()
    
    # Display team stats
    st.dataframe(teams_df, use_container_width=True)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Win Percentage by Team")
        fig = px.bar(
            teams_df,
            x='Team',
            y='Win %',
            color='Win %',
            color_continuous_scale='RdYlGn',
            text='Win %'
        )
        fig.update_layout(height=400, showlegend=False)
        fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Runs vs Wickets")
        fig = px.scatter(
            teams_df,
            x='Total Runs',
            y='Total Wickets',
            size='Matches',
            color='Win %',
            color_continuous_scale='Blues',
            hover_name='Team',
            text='Team'
        )
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #616161; padding: 1rem;'>
        <p>IPL 2025 Cricket Dashboard | Built with Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)