import streamlit as st
import pandas as pd
import seaborn as sns
df3=pd.read_csv('df.csv')

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
sns.heatmap(df3.corr(), ax=ax)
st.write(fig)