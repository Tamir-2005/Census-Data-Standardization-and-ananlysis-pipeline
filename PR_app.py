#!/usr/bin/env python
# coding: utf-8




import pandas as pd
df = pd.read_excel(r'C:\Users\Welcome\project\census_2011.xlsx')
df.head()



# TASK 1




rename_column= {
"State name" : "State/UT",
"District name"  : "District",
"Male_Literate" : "Literate_Male",
"Female_Literate" : "Literate_Female",
"Rural_Households"  : "Households_Rural",
"Urban_Households"  : "Households_Urban",
"Age_Group_0_29" : "Young_and_Adult",
"Age_Group_30_49" : "Middle_Aged",
"Age_Group_50" : "Senior_Citizen",
"Age not stated" : "Age_Not_Stated"
}
df.rename(columns=rename_column,inplace=True)
for renamed_col in df:
  print(renamed_col)


# TASK 2




def uni_case(value):
    new = value.split()
    changed_val = []

    for word in new:
        if word.lower() == 'and':
            changed_val.append('and')
        else:
            changed_val.append(word.capitalize())

    return ' '.join(changed_val)

# Applying uni_case function to the 'State/UT' column in the DataFrame
df['State/UT'] = df['State/UT'].apply(uni_case)

#Printing the first 10 rows
print(df['State/UT'].head(10))


# TASK 3




with open(r"C:\Users\Welcome\project\Telangana.txt") as file:

    districts_tel = file.read().splitlines()

print(districts_tel)

#State name changed to Telangana for the listed district
df.loc[df['District'].isin(districts_tel), 'State/UT'] = 'Telangana'

#Changing state name to ladakh for the district Leh and Kargil
df.loc[df['District'].isin(['Leh','Kargil']), 'State/UT'] = 'Ladakh'

#Lists after the changes made
df[df["State/UT"].isin(["Telangana","Ladakh"])]


# TASK 4




# Missing column in percentage
missing_data_per = df.isnull().sum() / len(df)
for column, percentage in missing_data_per.items():
    print(f'{column} : {percentage:.2%}')

# To fill missing data

# Population = Male + Female
to_fill_Population = (df['Male'].notnull() &
                      df['Population'].isnull() &
                      df['Female'].notnull())

df.loc[to_fill_Population, 'Population'] = df['Male'] + df['Female']

to_fill_Male = (df['Female'].notnull() &
                df['Population'].notnull() &
                df['Male'].isnull())

df.loc[to_fill_Male, 'Male'] = df['Population'] - df['Female']

to_fill_Female = (df['Male'].notnull() &
                  df['Population'].notnull() &
                  df['Female'].isnull())

df.loc[to_fill_Female, 'Female'] = df['Population'] - df['Male']

# Literate = Literate_Male + Literate_Female
to_fill_Literate = (df['Literate_Male'].notnull() &
                    df['Literate'].isnull() &
                    df['Literate_Female'].notnull())

df.loc[to_fill_Literate, 'Literate'] = df['Literate_Male'] + df['Literate_Female']

to_fill_Literate_Male = (df['Literate_Female'].notnull() &
                         df['Literate'].notnull() &
                         df['Literate_Male'].isnull())

df.loc[to_fill_Literate_Male, 'Literate_Male'] = df['Literate'] - df['Literate_Female']

to_fill_Literate_Female = (df['Literate_Male'].notnull() &
                           df['Literate'].notnull() &
                           df['Literate_Female'].isnull())

df.loc[to_fill_Literate_Female, 'Literate_Female'] = df['Literate'] - df['Literate_Male']

# SC = Male_SC + Female_SC
to_fill_SC = (df['Male_SC'].notnull() &
              df['SC'].isnull() &
              df['Female_SC'].notnull())

df.loc[to_fill_SC, 'SC'] = df['Male_SC'] + df['Female_SC']

to_fill_Male_SC = (df['Female_SC'].notnull() &
                   df['SC'].notnull() &
                   df['Male_SC'].isnull())

df.loc[to_fill_Male_SC, 'Male_SC'] = df['SC'] - df['Female_SC']

to_fill_Female_SC = (df['Male_SC'].notnull() &
                     df['SC'].notnull() &
                     df['Female_SC'].isnull())

df.loc[to_fill_Female_SC, 'Female_SC'] = df['SC'] - df['Male_SC']

# ST = Male_ST + Female_ST
to_fill_ST = (df['Male_ST'].notnull() &
              df['ST'].isnull() &
              df['Female_ST'].notnull())

df.loc[to_fill_ST, 'ST'] = df['Male_ST'] + df['Female_ST']

to_fill_Male_ST = (df['Female_ST'].notnull() &
                   df['ST'].notnull() &
                   df['Male_ST'].isnull())

df.loc[to_fill_Male_ST, 'Male_ST'] = df['ST'] - df['Female_ST']

to_fill_Female_ST = (df['Male_ST'].notnull() &
                     df['ST'].notnull() &
                     df['Female_ST'].isnull())

df.loc[to_fill_Female_ST, 'Female_ST'] = df['ST'] - df['Male_ST']

# Workers = Male_Workers + Female_Workers
to_fill_Workers = (df['Male_Workers'].notnull() &
                   df['Workers'].isnull() &
                   df['Female_Workers'].notnull())

df.loc[to_fill_Workers, 'Workers'] = df['Male_Workers'] + df['Female_Workers']

to_fill_Male_Workers = (df['Female_Workers'].notnull() &
                        df['Workers'].notnull() &
                        df['Male_Workers'].isnull())

df.loc[to_fill_Male_Workers, 'Male_Workers'] = df['Workers'] - df['Female_Workers']

to_fill_Female_Workers = (df['Male_Workers'].notnull() &
                          df['Workers'].notnull() &
                          df['Female_Workers'].isnull())

df.loc[to_fill_Female_Workers, 'Female_Workers'] = df['Workers'] - df['Male_Workers']

# Population = Main_Workers + Marginal_Workers + Non_Workers
to_fill_Main_Workers = (df['Population'].notnull() &
                        df['Main_Workers'].isnull() &
                        df['Marginal_Workers'].notnull() &
                        df['Non_Workers'].notnull())

df.loc[to_fill_Main_Workers, 'Main_Workers'] = df['Population'] - df['Marginal_Workers'] - df['Non_Workers']

to_fill_Marginal_Workers = (df['Population'].notnull() & df['Marginal_Workers'].isnull() & df['Main_Workers'].notnull() & df['Non_Workers'].notnull())
df.loc[to_fill_Marginal_Workers, 'Marginal_Workers'] = df['Population'] - df['Main_Workers'] - df['Non_Workers']

to_fill_Non_Workers = (df['Population'].notnull() & df['Marginal_Workers'].notnull() & df['Non_Workers'].isnull() & df['Main_Workers'].notnull())
df.loc[to_fill_Non_Workers, 'Non_Workers'] = df['Population'] - df['Main_Workers'] - df['Marginal_Workers']

# Workers = Cultivator_Workers + Agricultural_Workers + Household_Workers + Other_Workers
to_fill_Cultivator_Workers = (df['Cultivator_Workers'].isnull() & df['Workers'].notnull() & df['Agricultural_Workers'].notnull() & df['Household_Workers'].notnull() & df['Other_Workers'].notnull())
df.loc[to_fill_Cultivator_Workers, 'Cultivator_Workers'] = df['Workers'] - df['Agricultural_Workers'] - df['Household_Workers'] - df['Other_Workers']

to_fill_Agricultural_Workers = (df['Agricultural_Workers'].isnull() & df['Workers'].notnull() & df['Cultivator_Workers'].notnull() & df['Household_Workers'].notnull() & df['Other_Workers'].notnull())
df.loc[to_fill_Agricultural_Workers, 'Agricultural_Workers'] = df['Workers'] - df['Cultivator_Workers'] - df['Household_Workers'] - df['Other_Workers']

to_fill_Household_Workers = (df['Household_Workers'].isnull() & df['Workers'].notnull() & df['Agricultural_Workers'].notnull() & df['Cultivator_Workers'].notnull() & df['Other_Workers'].notnull())
df.loc[to_fill_Household_Workers, 'Household_Workers'] = df['Workers'] - df['Agricultural_Workers'] - df['Cultivator_Workers'] - df['Other_Workers']

to_fill_Other_Workers = (df['Other_Workers'].isnull() & df['Workers'].notnull() & df['Agricultural_Workers'].notnull() & df['Household_Workers'].notnull() & df['Cultivator_Workers'].notnull())
df.loc[to_fill_Other_Workers, 'Other_Workers'] = df['Workers'] - df['Agricultural_Workers'] - df['Household_Workers'] - df['Cultivator_Workers']

# Population = Hindus + Muslims + Christians + Sikhs + Buddhists + Jains + Others_Religions + Religion_Not_Stated
to_fill_Hindus = (df['Hindus'].isnull() & df['Population'].notnull() & df['Muslims'].notnull() & df['Christians'].notnull() & df['Sikhs'].notnull() & df['Buddhists'].notnull() & df['Jains'].notnull() & df['Others_Religions'].notnull() & df['Religion_Not_Stated'].notnull())

df.loc[to_fill_Hindus, 'Hindus'] = df['Population'] - df['Muslims'] - df['Christians'] - df['Sikhs'] - df['Buddhists'] - df['Jains'] - df['Others_Religions'] - df['Religion_Not_Stated']

to_fill_Muslims = (df['Muslims'].isnull() & df['Population'].notnull() & df['Hindus'].notnull() & df['Christians'].notnull() & df['Sikhs'].notnull() & df['Buddhists'].notnull() & df['Jains'].notnull() & df['Others_Religions'].notnull() & df['Religion_Not_Stated'].notnull())
df.loc[to_fill_Muslims, 'Muslims'] = df['Population'] - df['Hindus'] - df['Christians'] - df['Sikhs'] - df['Buddhists'] - df['Jains'] - df['Others_Religions'] - df['Religion_Not_Stated']

to_fill_Christians = (df['Christians'].isnull() & df['Population'].notnull() & df['Muslims'].notnull() & df['Hindus'].notnull() & df['Sikhs'].notnull() & df['Buddhists'].notnull() & df['Jains'].notnull() & df['Others_Religions'].notnull() & df['Religion_Not_Stated'].notnull())
df.loc[to_fill_Christians, 'Christians'] = df['Population'] - df['Muslims'] - df['Hindus'] - df['Sikhs'] - df['Buddhists'] - df['Jains'] - df['Others_Religions'] - df['Religion_Not_Stated']

to_fill_Sikhs = (df['Sikhs'].isnull() & df['Population'].notnull() & df['Muslims'].notnull() & df['Christians'].notnull() & df['Hindus'].notnull() & df['Buddhists'].notnull() & df['Jains'].notnull() & df['Others_Religions'].notnull() & df['Religion_Not_Stated'].notnull())
df.loc[to_fill_Sikhs, 'Sikhs'] = df['Population'] - df['Muslims'] - df['Christians'] - df['Hindus'] - df['Buddhists'] - df['Jains'] - df['Others_Religions'] - df['Religion_Not_Stated']

to_fill_Buddhists = (df['Buddhists'].isnull() & df['Population'].notnull() & df['Muslims'].notnull() & df['Christians'].notnull() & df['Hindus'].notnull() & df['Sikhs'].notnull() & df['Jains'].notnull() & df['Others_Religions'].notnull() & df['Religion_Not_Stated'].notnull())
df.loc[to_fill_Buddhists, 'Buddhists'] = df['Population'] - df['Muslims'] - df['Christians'] - df['Hindus'] - df['Sikhs'] - df['Jains'] - df['Others_Religions'] - df['Religion_Not_Stated']

to_fill_Jains = (df['Jains'].isnull() & df['Population'].notnull() & df['Muslims'].notnull() & df['Christians'].notnull() & df['Hindus'].notnull() & df['Sikhs'].notnull() & df['Buddhists'].notnull() & df['Others_Religions'].notnull() & df['Religion_Not_Stated'].notnull())
df.loc[to_fill_Jains, 'Jains'] = df['Population'] - df['Muslims'] - df['Christians'] - df['Hindus'] - df['Sikhs'] - df['Buddhists'] - df['Others_Religions'] - df['Religion_Not_Stated']

to_fill_Others_Religions = (df['Others_Religions'].isnull() & df['Population'].notnull() & df['Muslims'].notnull() & df['Christians'].notnull() & df['Hindus'].notnull() & df['Sikhs'].notnull() & df['Buddhists'].notnull() & df['Jains'].notnull() & df['Religion_Not_Stated'].notnull())
df.loc[to_fill_Others_Religions, 'Others_Religions'] = df['Population'] - df['Muslims'] - df['Christians'] - df['Hindus'] - df['Sikhs'] - df['Buddhists'] - df['Jains'] - df['Religion_Not_Stated']

to_fill_Religion_Not_Stated = (df['Religion_Not_Stated'].isnull() & df['Population'].notnull() & df['Muslims'].notnull() & df['Christians'].notnull() & df['Hindus'].notnull() & df['Sikhs'].notnull() & df['Buddhists'].notnull() & df['Jains'].notnull() & df['Others_Religions'].notnull())
df.loc[to_fill_Religion_Not_Stated, 'Religion_Not_Stated'] = df['Population'] - df['Muslims'] - df['Christians'] - df['Hindus'] - df['Sikhs'] - df['Buddhists'] - df['Jains'] - df['Others_Religions']

# Households = Households_Rural + Households_Urban
to_fill_Households = (df['Households_Rural'].notnull() & df['Households'].isnull() & df['Households_Urban'].notnull())
df.loc[to_fill_Households, 'Households'] = df['Households_Rural'] + df['Households_Urban']

to_fill_Households_Rural = (df['Households_Urban'].notnull() & df['Households'].notnull() & df['Households_Rural'].isnull())
df.loc[to_fill_Households_Rural, 'Households_Rural'] = df['Households'] - df['Households_Urban']

to_fill_Households_Urban = (df['Households_Rural'].notnull() & df['Households'].notnull() & df['Households_Urban'].isnull())
df.loc[to_fill_Households_Urban, 'Households_Urban'] = df['Households'] - df['Households_Rural']

# Literate_Education = Below_Primary_Education + Primary_Education + Middle_Education + Secondary_Education + Higher_Education + Graduate_Education + Other_Education
to_fill_Below_Primary_Education = (df['Below_Primary_Education'].isnull() & df['Literate_Education'].notnull() & df['Primary_Education'].notnull() & df['Middle_Education'].notnull() & df['Secondary_Education'].notnull() & df['Higher_Education'].notnull() & df['Graduate_Education'].notnull() & df['Other_Education'].notnull())
df.loc[to_fill_Below_Primary_Education, 'Below_Primary_Education'] = df['Literate_Education'] - df['Primary_Education'] - df['Middle_Education'] - df['Secondary_Education'] - df['Higher_Education'] - df['Graduate_Education']

to_fill_Primary_Education = (df['Primary_Education'].isnull() & df['Literate_Education'].notnull() & df['Below_Primary_Education'].notnull() & df['Middle_Education'].notnull() & df['Secondary_Education'].notnull() & df['Higher_Education'].notnull() & df['Graduate_Education'].notnull() & df['Other_Education'].notnull())
df.loc[to_fill_Primary_Education, 'Primary_Education'] = df['Literate_Education'] - df['Below_Primary_Education'] - df['Middle_Education'] - df['Secondary_Education'] - df['Higher_Education'] - df['Graduate_Education']

to_fill_Middle_Education = (df['Middle_Education'].isnull() & df['Literate_Education'].notnull() & df['Primary_Education'].notnull() & df['Below_Primary_Education'].notnull() & df['Secondary_Education'].notnull() & df['Higher_Education'].notnull() & df['Graduate_Education'].notnull() & df['Other_Education'].notnull())
df.loc[to_fill_Middle_Education, 'Middle_Education'] = df['Literate_Education'] - df['Primary_Education'] - df['Below_Primary_Education'] - df['Secondary_Education'] - df['Higher_Education'] - df['Graduate_Education'] - df['Other_Education']

to_fill_Secondary_Education = (df['Secondary_Education'].isnull() & df['Literate_Education'].notnull() & df['Primary_Education'].notnull() & df['Middle_Education'].notnull() & df['Below_Primary_Education'].notnull() & df['Higher_Education'].notnull() & df['Graduate_Education'].notnull() & df['Other_Education'].notnull())
df.loc[to_fill_Secondary_Education, 'Secondary_Education'] = df['Literate_Education'] - df['Primary_Education'] - df['Middle_Education'] - df['Below_Primary_Education'] - df['Higher_Education'] - df['Graduate_Education'] - df['Other_Education']

to_fill_Higher_Education = (df['Higher_Education'].isnull() & df['Literate_Education'].notnull() & df['Primary_Education'].notnull() & df['Middle_Education'].notnull() & df['Below_Primary_Education'].notnull() & df['Secondary_Education'].notnull() & df['Graduate_Education'].notnull() & df['Other_Education'].notnull())
df.loc[to_fill_Higher_Education, 'Higher_Education'] = df['Literate_Education'] - df['Primary_Education'] - df['Middle_Education'] - df['Below_Primary_Education'] - df['Secondary_Education'] - df['Graduate_Education'] - df['Other_Education'] - df['Religion_Not_Stated']

to_fill_Graduate_Education = (df['Graduate_Education'].isnull() & df['Literate_Education'].notnull() & df['Primary_Education'].notnull() & df['Middle_Education'].notnull() & df['Below_Primary_Education'].notnull() & df['Secondary_Education'].notnull() & df['Higher_Education'].notnull() & df['Other_Education'].notnull())
df.loc[to_fill_Graduate_Education, 'Graduate_Education'] = df['Literate_Education'] - df['Primary_Education'] - df['Middle_Education'] - df['Below_Primary_Education'] - df['Secondary_Education'] - df['Higher_Education'] - df['Other_Education']

to_fill_Other_Education = (df['Other_Education'].isnull() & df['Literate_Education'].notnull() & df['Primary_Education'].notnull() & df['Middle_Education'].notnull() & df['Below_Primary_Education'].notnull() & df['Secondary_Education'].notnull() & df['Higher_Education'].notnull() & df['Graduate_Education'].notnull())
df.loc[to_fill_Other_Education, 'Other_Education'] = df['Literate_Education'] - df['Primary_Education'] - df['Middle_Education'] - df['Below_Primary_Education'] - df['Secondary_Education'] - df['Higher_Education'] - df['Graduate_Education']

# Total_Education = Literate_Education + Illiterate_Education
to_fill_Total_Education = (df['Literate_Education'].notnull() & df['Total_Education'].isnull() & df['Illiterate_Education'].notnull())
df.loc[to_fill_Total_Education, 'Total_Education'] = df['Literate_Education'] + df['Illiterate_Education']

to_fill_Literate_Education = (df['Illiterate_Education'].notnull() & df['Total_Education'].notnull() & df['Literate_Education'].isnull())
df.loc[to_fill_Literate_Education, 'Literate_Education'] = df['Total_Education'] - df['Illiterate_Education']

to_fill_Illiterate_Education = (df['Literate_Education'].notnull() & df['Total_Education'].notnull() & df['Illiterate_Education'].isnull())
df.loc[to_fill_Illiterate_Education, 'Illiterate_Education'] = df['Total_Education'] - df['Literate_Education']

# Population = Young_and_Adult + Middle_Aged + Senior_Citizen + Age_Not_Stated
to_fill_Young_and_Adult = (df['Young_and_Adult'].isnull() & df['Population'].notnull() & df['Middle_Aged'].notnull() & df['Senior_Citizen'].notnull() & df['Age_Not_Stated'].notnull())
df.loc[to_fill_Young_and_Adult, 'Young_and_Adult'] = df['Population'] - df['Middle_Aged'] - df['Senior_Citizen'] - df['Age_Not_Stated']

to_fill_Middle_Aged = (df['Middle_Aged'].isnull() & df['Population'].notnull() & df['Young_and_Adult'].notnull() & df['Senior_Citizen'].notnull() & df['Age_Not_Stated'].notnull())

df.loc[to_fill_Middle_Aged, 'Middle_Aged'] = df['Population'] - df['Young_and_Adult'] - df['Senior_Citizen'] - df['Age_Not_Stated']

to_fill_Senior_Citizen = (df['Senior_Citizen'].isnull() & df['Population'].notnull() & df['Middle_Aged'].notnull() & df['Young_and_Adult'].notnull() & df['Age_Not_Stated'].notnull())
df.loc[to_fill_Senior_Citizen, 'Senior_Citizen'] = df['Population'] - df['Middle_Aged'] - df['Young_and_Adult'] - df['Age_Not_Stated']

to_fill_Age_Not_Stated = (df['Age_Not_Stated'].isnull() & df['Population'].notnull() & df['Middle_Aged'].notnull() & df['Senior_Citizen'].notnull() & df['Young_and_Adult'].notnull())
df.loc[to_fill_Age_Not_Stated, 'Age_Not_Stated'] = df['Population'] - df['Middle_Aged'] - df['Senior_Citizen'] - df['Young_and_Adult']

# Calculating the missing values after filling
missing_data_after = df.isnull().sum()/len(df)
for column, percentage in missing_data_after.items():
    print(f'{column} : {percentage:.2%}')





for column in df.columns:
    percentage_before = missing_data_per[column] * 100
    percentage_after = missing_data_after[column] * 100
    print(f'{column}: Before {percentage_before:.2f}% ----> After {percentage_after:.2f}%')


# TASK 5




from pymongo import MongoClient

# Connecting to MongoDB
client = MongoClient('mongodb+srv://lovelytamir2005:UQig5oOKWTzha9l9@cluster0.sfp1awb.mongodb.net/')
db = client['testdb']
collection = db['df']

# Converting DataFrame to dictionary format 
data_dict = df.to_dict("records")

# Inserting data into MongoDB
collection.insert_many(data_dict)

# opening the collection
for data in collection.find():
    print(data)


# TASK 6




from sqlalchemy import create_engine


mongo_data = list(collection.find())

# Remove the MongoDB ObjectId
for record in mongo_data:
    record.pop('_id', None)


# Coverting MongoDB data to dataframe
df_mtos = pd.DataFrame(mongo_data)

#Defining function to list out the lengthy column names
def print_lengthy_columns(df_mtos, max_length=30):
    lengthy_columns = [col for col in df_mtos.columns if len(col) > max_length]

    if lengthy_columns:
        for col in lengthy_columns:
            print(f"- {col}")
    else:
        print("No lengthy columns found.")

print_lengthy_columns(df_mtos)


#renaming column name for the lengthy columns

rename_lengthy_column= {
"Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households" : "Households_Night_Soil_disposed_into_Open_Drain",
"Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households"  : "Households_Flush_Latrine_connect_to_Other_System",
"Not_having_bathing_facility_within_the_premises_Total_Households" : "Households_Without_Bathing_Facility",
"Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households" : "Households_Without_Latrine_facility",
"Main_source_of_drinking_water_Handpump_Tubewell_Borewell_Households"  : "Households_Handpump_Tubewell_Borewell_Water",
"Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Households"  : "Households_Natural_Water_Sources",
"Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car": "Households_Comprehensive_Electronics_Vehicles"
}

df_mtos.rename(columns=rename_lengthy_column, inplace=True)

#Listing the column of the dataframe
for col in df_mtos:
    print(col)

#MySQL Database credentials
username = 'root'
password = '2103'
host = 'localhost'
port = 3306
database = 'test'


# Creating the engine
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')


#Loading data to MySQL
df_mtos.to_sql('df_mysql', con=engine, if_exists='replace',index=False)



