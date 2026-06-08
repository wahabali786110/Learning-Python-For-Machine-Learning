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
# st.title('Streamlit Charts Demo')

# charts_data=pd.DataFrame(
#     np.random.randn(20,3),
#     columns=['A','B','C']
# )

# st.subheader('Area Chart')
# st.area_chart(charts_data)

# st.subheader('Bar Chart')
# st.bar_chart(charts_data)

# st.subheader('Line Chart')
# st.line_chart(charts_data)

# scatter_data=pd.DataFrame({
#     'x':np.random.randn(100),
#     'y':np.random.randn(100)
# })

# st.subheader('Scatter Chart')
# st.scatter_chart(scatter_data)

# map_data=pd.DataFrame(
#     np.random.randn(100,2) /[50,50]+[24.6061,68.0822],
#     columns=['lat','lon']
# )

# st.subheader('Map')
# st.map(map_data)


# fig, ax=plt.subplots()
# ax.plot(charts_data['A'],label='A')
# ax.plot(charts_data['B'],label='B')
# ax.plot(charts_data['C'],label='C')
# ax.set_title('Pyplot Line Chart')
# ax.legend()

# st.subheader('Pyplot Chart')
# st.pyplot(fig)

# form, text_input, number_input, selectbox, date_input, form_submit_button, warning, balloons
# from datetime import datetime

# min_date=datetime(1980,1,1)
# max_date=datetime.now()

# form_values={
#     'Name':None,
#     'Height':None,
#     'Gender':None,
#     'DOB':None
# }

# with st.form(key='user_info_form'):
#     form_values['Name']=st.text_input('Enter your name')
#     form_values['Height']=st.number_input('Enter you height')
#     form_values['Gender']=st.selectbox('Select Gender',['Male','Female'])
#     form_values['DOB']=st.date_input('Enter your birth date',min_value=min_date,max_value=max_date)

#     submit_button=st.form_submit_button(label='Submit')
#     if submit_button:
#         if not all(form_values.values()):
#             st.warning('Fill all the fields!')
#         else:
#             st.balloons()
#             st.write('### Info')
            
#             for key, values in form_values.items():
#                 st.write(f"{key}: {values}")


# st.title('User Information Form')

# from datetime import datetime

# min_date=datetime(1980,1,1)
# max_date=datetime.now()


# with st.form('user_info',clear_on_submit=True):
#     name=st.text_input('Enter you first name')
#     birth_date=st.date_input('Enter you date of birth',min_value=min_date,max_value=max_date)

#     if birth_date:
#         age=max_date.year-birth_date.year
#         if birth_date.month>max_date.month or (birth_date.month==max_date.month and birth_date.day > max_date.day):
#             age-=1

#         st.write(f"Your calculated age is: {age} years")
        


#     submit_button=st.form_submit_button()

#     if submit_button:
#         if not birth_date or not name:
#             st.warning('Please fill all the fiels')
#         else:
#             st.success(f"Thank you! {name}. Your age is {age}")
#             st.balloons()

# session_state

# if 'counter' not in st.session_state:
#     st.session_state.counter=0

# if st.button(label='Increment Counter'):
#     st.session_state.counter+=1

# if st.button(label='Reset'):
#     st.session_state.counter=0

# st.write(f"Counter Value: {st.session_state.counter}")

# callbacks

# if 'step' not in st.session_state:
#     st.session_state.step=1

# if 'info' not in st.session_state:
#     st.session_state.info={}

# def go_to_step2():
#     st.session_state.info['name']=st.session_state.name_input
#     st.session_state.step=2

# def go_to_step1():
#     st.session_state.step=1


# if st.session_state.step==1:
#     st.text_input('Name',key='name_input', value=st.session_state.info.get('name',''))
#     st.button('Next',on_click=go_to_step2)

# if st.session_state.step==2:
#     st.header('Review the Form')
#     st.subheader('Check the info')
#     st.write(f"Your name is {st.session_state.info.get('name','')}")

#     if st.button('Submit'):
#         st.success('Form submitted')
#         st.balloons()
#         st.session_state.info={}

#     st.button('Back',on_click=go_to_step1)

# layouts
# sidebar,tabs, columns, container, placeholder(empty()), expander, PopOver tooltip,
st.sidebar.title('This is a sidebar')
st.sidebar.write("You can add elements like slider, buttons and text here")    

slider_input=st.sidebar.text_input('Enter anything')

tab1,tab2,tab3=st.tabs(['Tab1','Tab2','Tab3'])
with tab1:
    st.write('You are in tab 1')

with tab2:
    st.write('You are in tab 2')

with tab3:
    st.write('You are in tab 3')

col1,col2=st.columns(2)

with col1:
    st.title('Column 1')
    st.write('This is column 1')

with col2:
    st.title('Column 2')
    st.write('This is column 2')

with st.container(border=True):
    st.write('This is written in the container')
    st.write('You can think of a container as a frouping for elements')
    st.write('Containers help manage sections of the page')

placeholder=st.empty()
placeholder.write('This is written by using the placeholder')

if st.button('Update Placeholder'):
    placeholder.write('Placeholder is updated using the button')

with st.expander('Expand for more details'):
    st.write('This is additional information that is hidden by default')
    st.write('We can use expanders to keep our interfaces clean')

st.write('Hover over this button for a tooltip')
st.button('Button with tooltip',help='This is a tooltip or popover on hover over')

if slider_input:
    st.write(f"You have written {slider_input} in the sidebar")