import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Write and Button methods
# st.write('Hello World DEEER')
# "Hellow World"

# 2+5

# st.button('Press me')

# Title, Header, SubHeader, markdown, caption, code, Divider, Image
# st.title("This is a simple Title")
# st.header('This is header')
# st.subheader("This is sub header")
# st.markdown('This is **Markdown**')
# st.markdown('This is _Markdown_')
# st.caption('Small Caption')

# code_example="""
# def greet(name):
#     print('hello',name)
# """

# st.code(code_example,language='python')
# st.divider()

# st.image(os.path.join(os.getcwd(),'static','BG.png'),width=1000)

# Dataframe, DataEditor, Table, Metric, Json,Write
# df=pd.DataFrame({
#     'Name':['Wahab','Farman','Mehran','Amaar'],
#     'Age':[20,21,19,24],
#     'City':['Sujawal','Matli','Matli','Nawabshah']
# })

# st.title('Demo work on dataframes.')
# st.subheader('Dataframe')
# st.dataframe(df)

# st.subheader('Data Editor')
# edited_df=st.data_editor(df)

# st.subheader('Table')
# st.table(df)

# st.subheader('Metrices')
# st.metric(label='Total Rows',value=len(df))
# st.metric(label='Average Age',value=round(df['Age'].mean(),1))

# dict1={
#     'name':'Wahab',
#     'age':21,
#     'skills':['Python','Machine Learning','AI']
# }

# st.subheader('JSON')
# st.json(dict1)

# st.write('Dictionary View: ',dict1)

# Area_chart, bar_chart, line_chart, scatter_chart, map, pyplot
st.title('Streamlit Charts Demo')

charts_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C']
)

st.subheader('Area Chart')
st.area_chart(charts_data)

st.subheader('Bar Chart')
st.bar_chart(charts_data)

st.subheader('Line Chart')
st.line_chart(charts_data)

scatter_data=pd.DataFrame({
    'x':np.random.randn(100),
    'y':np.random.randn(100)
})

st.subheader('Scatter Chart')
st.scatter_chart(scatter_data)

map_data=pd.DataFrame(
    np.random.randn(100,2) /[50,50]+[24.6061,68.0822],
    columns=['lat','lon']
)

st.subheader('Map')
st.map(map_data)


fig, ax=plt.subplots()
ax.plot(charts_data['A'],label='A')
ax.plot(charts_data['B'],label='B')
ax.plot(charts_data['C'],label='C')
ax.set_title('Pyplot Line Chart')
ax.legend()

st.subheader('Pyplot Chart')
st.pyplot(fig)