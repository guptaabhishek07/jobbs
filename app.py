import streamlit as st
import pandas as pd
import pickle

# Load data and similarity measures
data = pickle.load(open('data.pkl3', 'rb'))
similarity3 = pickle.load(open('similarity3.pkl', 'rb'))

def recommendation(industry):
    # Check if the specified industry exists in the data
    if industry in data['Industry'].values:
        idx = data[data['Industry'] == industry].index[0]
        idx = data.index.get_loc(idx)
        distances = sorted(list(enumerate(similarity3[idx])), reverse=True, key=lambda x: x[1])[1:20]

        jobs = []
        for i in distances:
            jobs.append(data.iloc[i[0]].Industry)

        return jobs
    else:
        return None

# Create Streamlit app interface
st.sidebar.header('Job Recommendation System')
selected_industry = st.sidebar.selectbox('Select an Industry', data['Industry'])

jobs = recommendation(selected_industry)

if jobs:
    st.write('Recommended Jobs:')
    for job in jobs:
        st.write(job)
else:
    st.write("No data found for the selected industry.")
