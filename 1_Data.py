import streamlit as st
import pandas as pd


st.title("Data")
st.sidebar.markdown("""# Data

Now, let's talk about dataframes!""")

st.markdown("""## 
The following data is from TLC Trip Record Data. https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page 

""")


import streamlit as st
import pandas as pd
import pyarrow.parquet as pq
import duckdb
import matplotlib.pyplot as plt
import numpy as np


# Read the parquet file into a DataFrame
trips = pq.read_table('C:/Users/leong/OneDrive/Desktop/P2/data/yellow_tripdata_2023-01.parquet').to_pandas()

# Read the CSV file into a DataFrame
csv_file_path = 'C:/Users/leong/OneDrive/Desktop/P2/data/taxi_zone_lookup.csv'
data = pd.read_csv('C:/Users/leong/OneDrive/Desktop/P2/data/taxi_zone_lookup.csv')

# Display the entire DataFrame
st.write("Taxi Zone Lookup Table:")
st.table(data)  # or st.dataframe(data)



# Display only the first 100 rows using st.dataframe()
st.write("January 2023 Data:")
st.dataframe(trips.head(100))
trips.describe()

# trips['hour']=trips['tpep_pickup_datetime']

#q ="""SELECT PULocationID, SUM(passenger_count)
#	FROM trips
#	GROUP BY PULocationID"""
#duckdb.query(q).df()

# Extract and display repeating values in the 'PULocationID' column
column_to_check = 'PULocationID'
repeating_value_counts = trips[column_to_check][trips.duplicated(subset=column_to_check, keep=False)].value_counts()

# Sort the values by count in descending order
sorted_values = repeating_value_counts.reset_index().rename(columns={column_to_check: 'Count', 'index': 'Unique Values'})

# Manually set the header for 'PULocationID'
sorted_values = sorted_values.rename(columns={'PULocationID': 'Unique Values'})

#st.write(f"'{column_to_check}' column (sorted by count):")
#st.table(sorted_values)

# Perform an inner join on 'PULocationID' and 'LocationID'
merged_data = pd.merge(trips, data, how='inner', left_on='PULocationID', right_on='LocationID')

# Display the merged DataFrame
st.write("Merged Data:")
st.table(merged_data.head(5))  # Display the first 100 rows

######################################


# Make table of Pickups by Borough
st.write("Specified Drop off Tables: ")
q =""" SELECT Borough, Avg(DOLocationID) as Drop_off_Location
	FROM merged_data
	GROUP BY Borough
	ORDER BY Borough"""
test=duckdb.query(q).df()
test

test=test.loc[:5,:].copy()
test
######################################

# Make table of Pickups by Borough
st.write("Specified Pick up Tables: ")
q =""" SELECT Borough, Avg(PULocationID) as Pick_up_Location
	FROM merged_data
	GROUP BY Borough
	ORDER BY Borough"""
test=duckdb.query(q).df()
test


test=test.loc[:5,:].copy()
test

######################################
# Make table of Pickups by Borough
st.write("Specified Average Number of Passengers Tables:")
q =""" SELECT Borough, Avg(passenger_count) as Number_of_Passengers
	FROM merged_data
	GROUP BY Borough
	ORDER BY Borough"""
test=duckdb.query(q).df()
test


test=test.loc[:5,:].copy()
test


#######################################

# Make table of Pickups by Borough
st.write("Specified Average Trip Distance Tables:")
q =""" SELECT Borough, AVG(trip_distance) as Average_Distance
	FROM merged_data
	GROUP BY Borough
	ORDER BY Borough"""
test=duckdb.query(q).df()
test


test=test.loc[:5,:].copy()
test

#####################################
st.write("Specified Average Fair Price Tables:")
# Make table of Pickups by Borough
q =""" SELECT Borough, AVG(fare_amount) as Average_Cost
	FROM merged_data
	GROUP BY Borough
	ORDER BY Borough"""
test=duckdb.query(q).df()


test=test.loc[:5,:].copy()