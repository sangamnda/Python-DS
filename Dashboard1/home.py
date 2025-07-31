import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns

st.title('Netflix Dashboard')
st.write('This is a dashboard for analyzing the Netflix dataset')

# df = sns.load_dataset('netflix_titles.csv')
# st.dataframe(df)
df = pd.read_csv('netflix_titles.csv')
