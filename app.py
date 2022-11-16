#import packages
import streamlit as st
import pandas as pd
import numpy as np

st.title('Hospital Inpatient Discharges 2016')

DATE_COLUMN = 'date/time'

@st.cache
def load_data(nrows):
    data = pd.read_csv('/Users/jennamui/Documents/GitHub/dashboard-streamlit/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2016.csv', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['Self-Pay','Medicare','Medicaid','Private Insurance','Blue Cross/Blue Shield'])

st.bar_chart(chart_data)