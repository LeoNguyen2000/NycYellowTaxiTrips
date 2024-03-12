
############################################################################################
import streamlit as st
import pandas as pd
import pyarrow.parquet as pq
import duckdb
import matplotlib.pyplot as plt
import numpy as np

st.write('NYC, Yellow Taxi Trip Data January 2023')

# Read the parquet file into a DataFrame
trips = pq.read_table('C:/Users/leong/OneDrive/Desktop/P2/data/yellow_tripdata_2023-01.parquet').to_pandas()

# Read the CSV file into a DataFrame
csv_file_path = 'C:/Users/leong/OneDrive/Desktop/P2/data/taxi_zone_lookup.csv'
data = pd.read_csv('C:/Users/leong/OneDrive/Desktop/P2/data/taxi_zone_lookup.csv')

# Display the entire DataFrame
#st.write("CSV Data:")
#st.table(data)  # or st.dataframe(data)



# Display only the first 100 rows using st.dataframe()
#st.dataframe(trips.head(100))
#trips.describe()

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

# Perform an inner join on 'DOLocationID' and 'LocationID'
merged_data2 = pd.merge(trips, data, how='inner', left_on='DOLocationID', right_on='LocationID')

# Display the merged DataFrame
#st.write("Merged Data:")
#st.table(merged_data.head(5))  # Display the first 100 rows

######################################

# Make table of Pickups by Borough
q =""" SELECT Borough, AVG(fare_amount) as Average_Cost
	FROM merged_data
	GROUP BY Borough
	ORDER BY Borough"""
test=duckdb.query(q).df()


test=test.loc[:5,:].copy()

######################################
st.title('Average Fare ($USD) for Rides Originating From Each Borough')

group_data = list(test['Average_Cost'])
group_names = list(test['Borough'])
group_mean = np.mean(group_data)

fig, ax = plt.subplots()

ax.barh(group_names, group_data)
st.pyplot(fig)

########################################



# Make table of Pickups by Borough
q =""" SELECT Borough, AVG(trip_distance) as Average_Distance
	FROM merged_data
	GROUP BY Borough
	ORDER BY Borough"""
test=duckdb.query(q).df()


test=test.loc[:5,:].copy()

######################################
st.title('Average Distance (Miles) for Rides Originating From Each Borough')

group_data = list(test['Average_Distance'])
group_names = list(test['Borough'])
group_mean = np.mean(group_data)

fig, ax = plt.subplots()

ax.barh(group_names, group_data)
st.pyplot(fig)

########################################

# Make table of Pickups by Borough
q =""" SELECT Borough, Avg(passenger_count) as Number_of_Passengers
	FROM merged_data
	GROUP BY Borough
	ORDER BY Borough"""
test=duckdb.query(q).df()


test=test.loc[:5,:].copy()

######################################
st.title('Average Number of Customers for Rides Originating From Each Borough')

group_data = list(test['Number_of_Passengers'])
group_names = list(test['Borough'])
group_mean = np.mean(group_data)

fig, ax = plt.subplots()

ax.barh(group_names, group_data)
st.pyplot(fig)

#######################################

# Make table of Pickups by Borough
q =""" SELECT Borough, Count(*) as Pick_up_Location
	FROM merged_data
	GROUP BY Borough
	ORDER BY Borough"""
test=duckdb.query(q).df()


test=test.loc[:5,:].copy()

######################################
st.title('Average number of Pick ups from Each Borough')

group_data = list(test['Pick_up_Location'])
group_names = list(test['Borough'])
group_mean = np.mean(group_data)

fig, ax = plt.subplots()

ax.barh(group_names, group_data)
st.pyplot(fig)

####################################

# Make table of Dropoffs by Borough
q =""" SELECT Borough, Count(*) as Drop_off_Location
	FROM merged_data2
	GROUP BY Borough
	ORDER BY Borough"""
test=duckdb.query(q).df()


test=test.loc[:5,:].copy()

######################################
st.title('Average number of Drop offs from Each Borough')

group_data = list(test['Drop_off_Location'])
group_names = list(test['Borough'])
group_mean = np.mean(group_data)

fig, ax = plt.subplots()

ax.barh(group_names, group_data)
st.pyplot(fig)

