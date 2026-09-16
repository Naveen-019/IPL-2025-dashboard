# 🏏 IPL 2025 Cricket Analytics Dashboard

## 📌 Project Overview

The **IPL 2025 Cricket Analytics Dashboard** is an interactive data visualization project designed to analyze and explore Indian Premier League (IPL) 2025 cricket statistics.

The project provides insights into match results, team performance, player statistics, top run-scorers, and leading wicket-takers through an easy-to-use dashboard.

It uses Python, Pandas, and Plotly for data analysis and visualization, along with HTML and CSS for a web-based dashboard interface.

---

## 🎯 Project Objectives

- Analyze IPL 2025 match results and team performance.
- Identify the leading run-scorers and wicket-takers.
- Display tournament statistics through interactive visualizations.
- Explore team performance using points tables and statistics.
- Build a user-friendly cricket analytics dashboard.
- Gain practical experience in data analysis and data visualization.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Data processing and dashboard development |
| Pandas | Data loading, cleaning, and analysis |
| Plotly | Interactive charts and data visualization |
| Streamlit | Building the interactive Python dashboard |
| HTML5 | Creating the web dashboard structure |
| CSS3 | Styling and designing the dashboard |
| CSV | Storing IPL match and player statistics |
| Git/GitHub | Version control and project sharing |
| VS Code | Project development and coding |

---

## 📂 Project Structure

```text
IPL-2025-dashboard-main/
│
├── app.py
├── index.html
├── style.css
│
├── matches.csv
├── deliveries.csv
├── orange_cap.csv
├── purple_cap.csv
│
└── requirements.txt
```

---

## 📊 Dataset Description

The project uses CSV files containing IPL 2025 cricket statistics.

### 1. matches.csv

Contains match-level information, including:

- Match ID
- Match date
- Venue
- Teams
- Match stage
- Match winner
- First-innings score
- Second-innings score
- Player of the Match

### 2. deliveries.csv

Contains ball-by-ball match data, which can be used to analyze:

- Runs scored
- Batting performance
- Bowling performance
- Team scoring patterns
- Ball-by-ball match statistics

### 3. orange_cap.csv

Contains batting statistics of IPL 2025 players, including:

- Player name
- Team
- Matches played
- Innings
- Total runs
- Batting average
- Strike rate
- Highest score
- Number of boundaries
- Centuries and fifties

### 4. purple_cap.csv

Contains bowling statistics of IPL 2025 players, including:

- Player name
- Team
- Matches played
- Innings
- Overs bowled
- Runs conceded
- Wickets
- Economy rate
- Best bowling figures
- Four-wicket and five-wicket hauls

---

## 🚀 Dashboard Features

### 🏠 1. Tournament Overview

Displays the major IPL 2025 tournament statistics.

Key features:

- Total number of matches
- Tournament champions
- Orange Cap winner
- Purple Cap winner
- Top 5 run-scorers
- Top 5 wicket-takers
- Team points table

---

### 🏏 2. Match Results

Provides an overview of IPL 2025 match results.

Features:

- View match details.
- Filter matches by stage.
- Filter matches by team.
- View match winners.
- View venues and match dates.
- Display player-of-the-match information.
- Analyze match statistics.

---

### 🟠 3. Orange Cap Analysis

Displays the batting performance of IPL 2025 players.

Features:

- Top run-scorers.
- Player-wise batting statistics.
- Runs comparison charts.
- Batting average and strike rate.
- Highest individual scores.
- Boundaries and milestone statistics.

---

### 🟣 4. Purple Cap Analysis

Displays the bowling performance of IPL 2025 players.

Features:

- Top wicket-takers.
- Player-wise bowling statistics.
- Wickets comparison charts.
- Economy rate analysis.
- Best bowling figures.
- Four-wicket and five-wicket haul statistics.

---

### 📈 5. Team Analysis

Provides team-level performance insights.

Features:

- Team-wise statistics.
- Matches played.
- Wins and losses.
- Team performance comparison.
- Team scoring analysis.
- Points table visualization.

---

## 🔄 Project Workflow

The project follows a data analytics workflow consisting of the following stages:

### Step 1: Data Collection

IPL 2025 match data, ball-by-ball data, and player statistics are collected and stored in CSV files.

⬇️

### Step 2: Data Storage

The collected datasets are organized and stored in the project directory.

Datasets include:

- Match data
- Delivery data
- Orange Cap statistics
- Purple Cap statistics

⬇️

### Step 3: Data Loading

Python and Pandas are used to load the CSV files into DataFrames.

```python
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")
orange_cap = pd.read_csv("orange_cap.csv")
purple_cap = pd.read_csv("purple_cap.csv")
```

⬇️

### Step 4: Data Processing

The data is processed to calculate useful statistics, such as:

- Total matches
- Team wins and losses
- Total runs
- Total wickets
- Top-performing players
- Team points
- Run-rate-related metrics

⬇️

### Step 5: Data Analysis

The processed data is analyzed to identify trends and patterns in:

- Batting performance
- Bowling performance
- Team performance
- Match results
- Player statistics

⬇️

### Step 6: Data Visualization

Plotly is used to create interactive charts and graphs.

Examples:

- Top run-scorers chart
- Top wicket-takers chart
- Team performance charts
- Player comparison charts

⬇️

### Step 7: Dashboard Development

The processed data and visualizations are integrated into an interactive dashboard using Streamlit.

HTML and CSS are also used to create a separate web-based dashboard interface.

⬇️

### Step 8: User Interaction

Users can explore the dashboard by:

- Navigating between sections.
- Filtering match data.
- Comparing players.
- Viewing team statistics.
- Exploring tournament insights.

⬇️

### Step 9: Insights and Interpretation

The dashboard helps users understand IPL 2025 team and player performance through data-driven insights.

---

## 🧠 Data Analytics Concepts Used

This project demonstrates the practical application of:

- Data collection
- Data cleaning
- Exploratory Data Analysis (EDA)
- Data transformation
- Aggregation and grouping
- Statistical analysis
- Data visualization
- Dashboard development
- Interactive filtering
- Performance comparison

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the Project Folder

```bash
cd IPL-2025-dashboard-main
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

## 🖥️ Dashboard Technologies

### Python Dashboard

The Python-based dashboard is developed using:

- Streamlit
- Pandas
- Plotly

The main application file is:

```text
app.py
```

### Web Dashboard

The project also includes a web-based interface built using:

- HTML
- CSS
- JavaScript

The main files are:

```text
index.html
style.css
```

> **Note:** The project contains both a Streamlit dashboard and a separate HTML/CSS-based dashboard interface.

---

## 📌 Expected Outcomes

By completing this project, users can:

- Understand IPL 2025 match statistics.
- Analyze team and player performance.
- Identify leading batsmen and bowlers.
- Explore cricket data using interactive dashboards.
- Apply Python and Pandas to real-world datasets.
- Develop practical data analytics and visualization skills.

---

## 🔮 Future Enhancements

- Add live IPL match data integration.
- Add advanced player comparison features.
- Include ball-by-ball visualizations.
- Add predictive analysis for match outcomes.
- Implement machine learning-based player performance predictions.
- Add interactive team performance filters.
- Deploy the dashboard using Streamlit Community Cloud.
- Improve mobile responsiveness.
- Add advanced statistical metrics such as Net Run Rate and player consistency analysis.

---

## 👨‍💻 Author

**Naveen Yadav**

Data Analytics & Data Science Student

---

## 📄 License

This project is intended for educational and learning purposes.
