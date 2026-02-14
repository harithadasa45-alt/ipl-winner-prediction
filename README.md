
# 🏏 IPL Data Analysis & Match Outcome Insights (2008–2025)

## 📌 Project Overview

This project presents a comprehensive Exploratory Data Analysis (EDA) of the Indian Premier League (IPL) dataset from 2008 to 2025 using Python.

The objective of this project is to analyze team performance, evaluate toss impact, identify match-winning patterns, and generate meaningful insights using data visualization techniques.

This project demonstrates practical skills in:

* Data Cleaning
* Data Exploration
* Statistical Insight Generation
* Visualization
* Structured Project Development

---

## 📊 Dataset Information

The dataset contains IPL match-level data from 2008 to 2025, including:

* Match Date
* Team 1
* Team 2
* Match Winner
* Toss Winner
* Player of the Match
* Win Margin
* Venue
* Over-wise scoring data (Innings 1 & 2)

Total Seasons Covered: 2008 – 2025
Dataset Type: Structured CSV format

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* VS Code

---

## 🧠 Project Workflow

### 1️⃣ Data Loading

The dataset was loaded using Pandas:

```python
df = pd.read_csv("ipl_2008_to_2025.csv")
```

---

### 2️⃣ Data Cleaning

* Removed inconsistencies in team names
* Standardized franchise names (e.g., Delhi Daredevils → Delhi Capitals)
* Checked for missing values
* Verified column integrity

---

### 3️⃣ Exploratory Data Analysis (EDA)

The following analyses were performed:

#### 🔥 Most Successful Teams

* Calculated total wins using `value_counts()`
* Identified top-performing franchises
* Visualized results using bar charts

Insight:
Mumbai Indians emerged as the most successful franchise during 2008–2025.

---

#### 🪙 Toss Impact Analysis

Calculated percentage of matches where the toss winner also won the match:

```python
toss_match_win = (df["Toss_Winner"] == df["Match_Winner"]).mean() * 100
```

Insight:
The toss winner won approximately XX% of matches, indicating moderate influence of toss outcome on match results.

(Replace XX with your actual percentage.)

---

#### 📈 Visual Storytelling

Created visualizations to represent:

* Team-wise win distribution
* Comparative performance
* Trend-based insights

Used Matplotlib for plotting and formatting.

---

## 📊 Sample Visualization

Bar chart showing most winning IPL teams from 2008–2025.

(You can upload a screenshot of your graph here.)

---

## 📂 Project Structure

```
IPL-Data-Analysis/
│
├── ipl_2008_to_2025.csv
├── analysis.py
├── README.md
└── screenshots/
```

---

## 🚀 How to Run the Project

1. Clone this repository:

```
git clone https://github.com/your-username/IPL-Data-Analysis.git
```

2. Install required libraries:

```
pip install pandas numpy matplotlib seaborn
```

3. Run the project:

```
python analysis.py
```

---

## 🎯 Key Learnings

Through this project, the following skills were strengthened:

* Real-world dataset handling
* Data inconsistency resolution
* Aggregation and grouping techniques
* Insight extraction from structured data
* Professional visualization practices

---

## 🔮 Future Improvements

* Season-wise performance trend analysis
* Player of the Match distribution analysis
* Win margin distribution study
* Predictive model for match outcome using Logistic Regression
* Streamlit dashboard deployment

---

## 💼 Resume Value

This project demonstrates end-to-end data analysis capability including:

* Data ingestion
* Cleaning
* Insight generation
* Visualization
* Structured documentation

Suitable for Data Analyst, Business Analyst, and Sports Analytics roles.

---

## 👩‍💻 Author

Haritha
MCA Final Year Student
Aspiring Data Analyst



Tell me what you want next 😌
