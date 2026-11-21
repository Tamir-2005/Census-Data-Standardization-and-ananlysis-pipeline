# Census Data Standardization and Analysis Pipeline: From Cleaning to Visualization

## 📌 Project Overview

The **Census Data Standardization and Analysis Pipeline** is a data engineering and analytics project that focuses on cleaning, processing, standardizing, storing, and analyzing Indian Census data.

The project uses Python, Pandas, MongoDB, SQL, and Streamlit to transform raw census datasets into structured and meaningful information for analysis and visualization.

The main objective is to improve data quality, maintain consistency across datasets, handle missing values, and generate useful insights through database queries and an interactive dashboard.

## 🎯 Project Objectives

- Clean and standardize Indian Census datasets.
- Rename columns for consistency across datasets.
- Standardize State and Union Territory names.
- Handle newly formed states such as Telangana and Ladakh.
- Identify and handle missing values.
- Calculate missing-data percentages before and after data processing.
- Store cleaned datasets in MongoDB.
- Transfer processed data from MongoDB into a relational database.
- Create primary key and foreign key constraints wherever required.
- Perform SQL-based data analysis.
- Develop an interactive Streamlit dashboard.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and pipeline development |
| Pandas | Data cleaning and manipulation |
| SQL | Database operations and analysis |
| MongoDB | NoSQL data storage |
| Streamlit | Interactive dashboard |
| MySQL / Relational Database | Structured data storage and querying |

## ⚙️ Project Workflow

The project follows these major stages:

1. Data Collection
2. Data Cleaning and Standardization
3. State and UT Name Standardization
4. New State Formation Handling
5. Missing Data Identification and Processing
6. MongoDB Data Storage
7. Relational Database Integration
8. SQL Query Execution
9. Streamlit Dashboard Development

## 📂 Data Processing

### Task 1: Column Name Standardization

Renamed inconsistent column names into standardized formats.

Examples:
- State name → State_UT
- District name → District
- Male_Literate → Literate_Male
- Female_Literate → Literate_Female
- Rural_Households → Households_Rural
- Urban_Households → Households_Urban
- Age_Group_0_29 → Young_and_Adult
- Age_Group_30_49 → Middle_Aged
- Age_Group_50 → Senior_Citizen
- Age not stated → Age_Not_Stated

### Task 2: State and UT Name Standardization

Standardized State and Union Territory names by:
- Converting names into proper title case.
- Keeping the word "and" lowercase.
- Replacing the "&" symbol with "and".
- Maintaining uniform naming conventions across datasets.

### Task 3: New State Formation

Handled the formation of two new administrative regions:

- **Telangana (2014):** Updated the State/UT name from Andhra Pradesh to Telangana for the specified districts.
- **Ladakh (2019):** Updated the State/UT name from Jammu and Kashmir to Ladakh for Leh and Kargil districts.

### Task 4: Missing Data Processing

Identified missing values and calculated missing-data percentages before and after data processing.

Used relationships between columns to fill missing values wherever possible.

Examples:

- Population = Male + Female
- Literate = Literate_Male + Literate_Female
- Population = Young_and_Adult + Middle_Aged + Senior_Citizen + Age_Not_Stated
- Households = Households_Rural + Households_Urban

## 🗄️ Database Integration

### MongoDB

- Stored the processed census datasets in MongoDB.
- Created a collection named `census`.
- Retrieved processed data from MongoDB for further database operations.

### Relational Database

- Transferred data from MongoDB into a relational database using Python.
- Created separate tables based on dataset filenames.
- Implemented primary key and foreign key constraints wherever required.
- Organized data for efficient SQL querying and analysis.

## 📊 SQL Analysis and Streamlit Dashboard

Developed analytical queries to answer 20 census-related questions.

### District-Level Analysis

1. Total population of each district.
2. Number of literate males and females.
3. Percentage of male and female workers.
4. Households using LPG or PNG as cooking fuel.
5. Religious composition of each district.
6. Households with internet access.
7. Educational attainment distribution.
8. Access to transportation and household assets.
9. Condition of occupied census houses.
10. Household size distribution.

### State-Level Analysis

11. Total number of households in each state.
12. Households with latrine facilities within the premises.
13. Average household size.
14. Owned versus rented households.
15. Distribution of different latrine facilities.
16. Access to drinking water sources near the premises.
17. Household income distribution based on purchasing power parity categories.
18. Married couples distribution across household sizes.
19. Households below the poverty line based on purchasing power parity categories.
20. Overall literacy rate of each state.

### Streamlit Dashboard

The Streamlit application provides an interactive interface to execute analytical queries and explore census information.

## 🚀 Installation and Setup

### Prerequisites

Install the following tools:

- Python 3.x
- MongoDB
- SQL database
- Visual Studio Code
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

### Step 2: Navigate to the Project Directory

```bash
cd YOUR_REPOSITORY
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install pandas pymongo sqlalchemy streamlit mysql-connector-python
```

### Step 5: Configure Database Connections

Configure your MongoDB and relational database connection details in the project configuration.

Do not upload passwords, credentials, or sensitive connection information to GitHub.

### Step 6: Execute the Data Pipeline

Run the Python pipeline script:

```bash
python main.py
```

Replace `main.py` with your actual pipeline entry-point filename if different.

### Step 7: Run the Streamlit Application

```bash
streamlit run app.py
```

Replace `app.py` with your actual Streamlit application filename if different.

## 📁 Project Structure

```text
Census-Data-Standardization-and-Analysis-Pipeline/
│
├── Data/
│   ├── Telangana.txt
│   └── census_datasets/
│
├── scripts/
│   ├── data_cleaning.py
│   ├── data_standardization.py
│   ├── missing_data.py
│   ├── mongodb_upload.py
│   └── sql_upload.py
│
├── database/
│   └── sql_queries.sql
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: This is a suggested structure. Adjust the filenames and folders to match your actual GitHub repository.*

## 💡 Key Learning Outcomes

- Practical experience in Python-based data engineering.
- Understanding data cleaning and preprocessing techniques.
- Working with missing values and data standardization.
- Understanding NoSQL and relational database integration.
- Implementing SQL queries for real-world data analysis.
- Building interactive dashboards using Streamlit.
- Developing modular and maintainable data pipelines.
- Managing project code using Git and GitHub.

## 🔮 Future Enhancements

- Automate data ingestion and processing.
- Integrate Apache Airflow for workflow orchestration.
- Implement cloud-based data storage using AWS.
- Optimize SQL queries for large datasets.
- Add advanced visualizations and reporting features.

## 👨‍💻 Author

**Tamir N**

Aspiring Data Engineer

**Skills:** Python | SQL | Pandas | MongoDB | ETL | Data Cleaning | Streamlit | Data Analytics

---

⭐ If you find this project useful, feel free to explore the repository and provide feedback.

**GitHub Repository:** [Add Your Repository Link Here]
