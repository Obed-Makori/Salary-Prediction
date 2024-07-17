import streamlit as st
with st.sidebar:
  st.image("mkenzo-logo.png", width=250)
  st.markdown("<style> margin-top:0; </style>",unsafe_allow_html=True)
  st.multiselect('Select Age', [1,2,3,4,5,6,7,8,9,'Skip'])
  st.button('Button 1')
import random
import numpy as np
s=np.random.rand()
st.button('Test')
# st.markdown("<h4 style=color:red; text-color:red;>TOP PLAYER</h2>", unsafe_allow_html=True) 

