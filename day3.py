import pandas as pd
import numpy as np
import streamlit as st

st.title('Welcome to Python website')
st.write('This is a simple website to show how to use Python with Streamlit')

data=pd.DataFrame({'c1':[1,2,3,4,5],'c2':["A","B",30,40,50]})
st.write(data)
chart_data = np.random.randn(20, 3)
st.bar_chart(chart_data)