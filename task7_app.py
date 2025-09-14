import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# ===============================
# MySQL Connection
# ===============================
username = "root"
password = "2103"   # <-- change if needed
host = "localhost"
port = 3306
database = "test"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")
# Use engine with pandas
query = "SELECT * FROM df_mysql"  # replace with your actual query
df = pd.read_sql(query, engine)

# ===============================
# Streamlit Title
# ===============================
st.title("Census Data Analysis Dashboard - Task 7")

# ===============================
# Query Dictionary (20 queries)
# ===============================
queries = {
    "1. Total population of each district":
        "SELECT `District`, SUM(Population) AS total_population FROM df_mysql GROUP BY `District`;",

    "2. Literate males and females in each district":
        "SELECT `District`, SUM(Literate_Male) AS Literate_Male, SUM(Literate_Female) AS Literate_Female FROM df_mysql GROUP BY `District`;",

    "3. Percentage of workers (male + female) in each district":
        """SELECT `District`,
                  (SUM(Male_Workers) + SUM(Female_Workers)) * 100.0 / SUM(Population) AS worker_percentage
           FROM df_mysql GROUP BY `District`;""",

    "4. Households with access to LPG/PNG as cooking fuel":
        "SELECT `District`, SUM(LPG_or_PNG_Households) AS households_with_gas FROM df_mysql GROUP BY `District`;",

    "5. Religious composition in each district":
        "SELECT `District`, SUM(Hindus) AS Hindus, SUM(Muslims) AS Muslims, SUM(Christians) AS Christians, SUM(Sikhs) AS Sikhs, SUM(Buddhists) AS Buddhists, SUM(Jains) AS Jains FROM df_mysql GROUP BY `District`;",

    "6. Households with internet access in each district":
        "SELECT `District`, SUM(Households_with_Internet) AS internet_households FROM df_mysql GROUP BY `District`;",

    "7. Educational attainment distribution":
        "SELECT `District`, SUM(Below_Primary_Education) AS below_primary, SUM(Primary_Education) AS primary_edu, SUM(Middle_Education) AS middle, SUM(Secondary_Education) AS secondary, SUM(Higher_Education) AS higher, SUM(Graduate_Education) AS graduate FROM df_mysql GROUP BY `District`;",

    "8. Access to transportation and communication assets":
        "SELECT `District`, SUM(Households_with_Bicycle) AS bicycle, SUM(Households_with_Car_Jeep_Van) AS car, SUM(Households_with_Radio_Transistor) AS radio, SUM(Households_with_Television) AS television FROM df_mysql GROUP BY `District`;",

    "9. Condition of occupied census houses":
        "SELECT `District`, SUM(Condition_of_occupied_census_houses_Dilapidated_Households) AS dilapidated, SUM(Households_with_separate_kitchen_Cooking_inside_house) AS with_kitchen, SUM(Having_bathing_facility_Total_Households) AS with_bath, SUM(Having_latrine_facility_within_the_premises_Total_Households) AS with_latrine FROM df_mysql GROUP BY `District`;",

    "10. Household size distribution":
        "SELECT `District`, SUM(Household_size_1_person_Households) AS size1, SUM(Household_size_2_persons_Households) AS size2, SUM(Household_size_3_to_5_persons_Households) AS size3_5 FROM df_mysql GROUP BY `District`;",

    "11. Total households in each state":
        "SELECT `State/UT`, SUM(Households) AS total_households FROM df_mysql GROUP BY `State/UT`;",

    "12. Households with latrine facility within premises in each state":
        "SELECT `State/UT`, SUM(Having_latrine_facility_within_the_premises_Total_Households) AS latrine_households FROM df_mysql GROUP BY `State/UT`;",

    "13. Male vs Female ratio in each district":
        "SELECT `District`, SUM(Male) AS total_males, SUM(Female) AS total_females, (SUM(Male)/SUM(Female)) AS sex_ratio FROM df_mysql GROUP BY `District`;",

    "14. Literacy rate (total literates / population) in each district":
        "SELECT `District`, SUM(Literate) * 100.0 / SUM(Population) AS literacy_rate FROM df_mysql GROUP BY `District`;",

    "15. Workers vs Non-Workers in each district":
        "SELECT `District`, SUM(Main_Workers) AS main_workers, SUM(Marginal_Workers) AS marginal_workers, SUM(Non_Workers) AS non_workers FROM df_mysql GROUP BY `District`;",

    "16. Access to banking facilities (proxy: households with computer + internet)":
        "SELECT `District`, SUM(Households_with_Computer) AS computer_households, SUM(Households_with_Internet) AS internet_households FROM df_mysql GROUP BY `District`;",

    "17. Access to electricity in each district":
        "SELECT `District`, SUM(Housholds_with_Electric_Lighting) AS electricity_households FROM df_mysql GROUP BY `District`;",

    "18. Availability of drinking water within premises":
        "SELECT `District`, SUM(Location_of_drinking_water_source_Within_the_premises_Households) AS water_within_premises FROM df_mysql GROUP BY `District`;",

    "19. Availability of tap water (treated/untreated combined as Tapwater)":
        "SELECT `District`, SUM(Main_source_of_drinking_water_Tapwater_Households) AS tapwater_households FROM df_mysql GROUP BY `District`;",

    "20. Availability of mobile phone in households":
        "SELECT `District`, SUM(Households_with_Telephone_Mobile_Phone) AS mobile_households FROM df_mysql GROUP BY `District`;"
}


# ===============================
# Streamlit UI
# ===============================
option = st.selectbox("Select a query to run:", list(queries.keys()))

if st.button("Run Query"):
    try:
        query = queries[option]
        df = pd.read_sql(query, engine)
        st.write(f"### Result for: {option}")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error: {e}")
