import pandas as pd
import numpy as np
import streamlit as st
st.title("hi everyone I am fine")
st.write("Python requires practise")
data=pd.DataFrame({
    'c1':[10,20,30,40],
    'c2':['A','B','C','D']})
st.write("Below is the table for data")
st.write(data)                
