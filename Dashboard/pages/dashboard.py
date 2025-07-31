import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.title('Titatnic Dashboard')
st.write('This is a dashboard for analyzing the titanic dataset')

df = sns.load_dataset('titanic')
st.dataframe(df)

st.sidebar.header('Filter Option')

#Filter
gender  = st.sidebar.multiselect('Gender',
                                 options = df['sex'].unique(),
                                 default = df['sex'].unique())

pclass = st.sidebar.multiselect('Passenger Class',
                                options = df['class'].unique(),
                                default = df['class'].unique())

min_age, max_age = st.sidebar.slider('Age',
                                     min_value=int(df['age'].min()),
                                     max_value = int(df['age'].max()),
                                     value = (int(df['age'].min()), int(df['age'].max())))

filtered_df = df[
    (df['sex'].isin(gender)) &
    (df['class'].isin(pclass)) &
    (df['age']>=min_age) &
    (df['age']<=max_age)
]

fig = px.histogram(filtered_df, x = 'age',
                   title= 'Age distribution',
                   template= 'plotly_dark')
st.plotly_chart(fig)
st.title('highest count : 54 of age group 24')
st.markdown('This graph showsthe distribution of age of the people')