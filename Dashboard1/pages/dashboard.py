import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns

st.title('Netflix Dashboard')
st.write('This is a dashboard for analyzing the Netflix dataset')

df = pd.read_csv('netflix_titles.csv')
st.dataframe(df)

st.sidebar.header('Filter Option')

releasing_year  = st.sidebar.multiselect('releasing_year',
                                 options = df['release_year'].unique(),
                                 default = df['release_year'].unique())

names = st.sidebar.multiselect('Movies and TV shows name',
                                options = df['title'].unique(),
                                default = df['title'].unique())

filtered_df = df[
    (df['release_year'].isin(releasing_year)) &
    (df['title'].isin(names))
]

fig = px.histogram(filtered_df, x = 'release_year', y = 'title',
                   title= 'Year wise Movies and Shows',
                   template= 'plotly_dark')
st.plotly_chart(fig)