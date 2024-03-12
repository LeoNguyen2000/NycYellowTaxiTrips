import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import duckdb
import pyarrow.parquet as pq

# Load data (replace this with your actual data loading code)
trips = pq.read_table('C:/Users/leong/OneDrive/Desktop/P2/data/yellow_tripdata_2023-01.parquet').to_pandas()
data = pd.read_csv('C:/Users/leong/OneDrive/Desktop/P2/data/taxi_zone_lookup.csv')

# Perform an inner join on 'PULocationID' and 'LocationID'
merged_data = pd.merge(trips, data, how='inner', left_on='PULocationID', right_on='LocationID')
# Perform an inner join on 'DOLocationID' and 'LocationID'
merged_data2 = pd.merge(trips, data, how='inner', left_on='DOLocationID', right_on='LocationID')

st.title("Charts")
st.sidebar.markdown("""# Charts
""")

# Radio button for selecting the type of chart
genre = st.radio(
    "What summarized data would you like to see?",
    [":green[Average Fair Price]", ":red[Distance]", ":rainbow[Number of Customers] :man:", ":blue[Number of Pickups]:taxi:", ":orange[Number of Dropoffs]:taxi:"],
    captions=["($USD).", "Average Miles.", "Average # of people.", "Average number of pickups", "Average number of dropoffs"])

# Section for 'Average Fair Price'
if genre == ':green[Average Fair Price]':
    st.title('Average Fare ($USD) for Rides Originating From Each Borough')

    # Your existing code for fetching and plotting the 'Average_Cost' data
    q = """ SELECT Borough, AVG(fare_amount) as Average_Cost
            FROM merged_data
            GROUP BY Borough
            ORDER BY Borough"""
    test = duckdb.query(q).df()
    test = test.loc[:5, :].copy()

    group_data = list(test['Average_Cost'])
    group_names = list(test['Borough'])
    group_mean = np.mean(group_data)

    fig, ax = plt.subplots()
    ax.barh(group_names, group_data)
    st.pyplot(fig)
##############################################################

# Section for 'Average Distance'
elif genre == ':red[Distance]':
    # Make table of Pickups by Borough
    q = """ SELECT Borough, AVG(trip_distance) as Average_Distance
            FROM merged_data
            GROUP BY Borough
            ORDER BY Borough"""
    test = duckdb.query(q).df()

    test = test.loc[:5, :].copy()

    st.title('Average Distance (Miles) for Rides Originating From Each Borough')

    group_data = list(test['Average_Distance'])
    group_names = list(test['Borough'])
    group_mean = np.mean(group_data)

    fig, ax = plt.subplots()
    ax.barh(group_names, group_data)
    st.pyplot(fig)
####################################################################

# Section for 'Average Distance'
elif genre == ':rainbow[Number of Customers] :man:':
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

########################################################################

# Section for 'Average Distance'
elif genre == ':blue[Number of Pickups]:taxi:':
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

##################################################################3
elif genre == ':orange[Number of Dropoffs]:taxi:':
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




# Add more sections for other radio button options if needed
# elif genre == 'OtherOption':
#    st.title('Other Option Title')
#    # Other Option Code

else:
    st.write("You didn't select any option.")