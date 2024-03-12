import streamlit as st
import pandas as pd


st.title("Analyzing Yellow Cab Data From the Five NY Boroughs")
st.subheader("Leo Nguyen, Thomas Pentimonti, Peerapas Apichatpichien")
st.markdown("""Yellow cabs are one of the most popular transportation methods in New York City. According to NYC.gov, there are 13,587 yellow taxis in New York City.
             We analyzed yellow cab data from the five New York boroughs and EWR, also known as Newark Liberty International Airport.
             The statistics we tracked were average fare, average distance, average number of customers picked up,
             average number of pickups from each borough, and average number of dropoffs from each borough.
            """)
st.markdown("***")
st.markdown("""The purpose of putting together this data was to find any patterns between the six pickup zones. Some Questions we wanted 
            answered include which pickup and dropoff locations were most and least popular, which locations had the highest and lowest
            average fares, and which locations had the highest number of customers picked up on average. Unfortunately we were
            limited to one month, January 2023 due to file size constraints""")