#import packages
import streamlit as st
import pandas as pd
import numpy as np


st.title('Hospital Inpatient Discharge Dataframes')

st.write('These are 2 dataframes with patient discharge information.')

st.header('This dataframe 1')

@st.cache
def load_data(nrows):
    data = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA-507-2022/main/autoML/datasets/data_sparcs.csv', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Dataframe 1')
    st.write(data)


st.subheader('Bar Graph')
chart_data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=['0-17','18-29','30-49','50-69','70+'])

st.bar_chart(chart_data)


st.header('This is dataframe 2')

@st.cache
def load_data(nrows):
    data2 = pd.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv', nrows=nrows)
    lowercase2 = lambda x: str(x).lower()
    data2.rename(lowercase2, axis='columns', inplace=True)
    return data2

# Create a text element and let the reader know the data is loading.
data2_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data2 = load_data(10000)
# Notify the reader that the data was successfully loaded.
data2_load_state.text("Done! (using st.cache)")

if st.checkbox('Show dataframe'):
    st.subheader('Dataframe 2')
    st.write(data2)

st.subheader('Line Graph')
chart_data2 = pd.DataFrame(
    np.random.randn(20, 4),
    columns=['Emergency', 'Elective', 'Newborn','Urgent'])

st.line_chart(chart_data2)
