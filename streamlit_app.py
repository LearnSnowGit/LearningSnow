import streamlit
import pandas


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Title
streamlit.title('Furst tust for me!')

#Header
streamlit.header('This should be header')

#Text
streamlit.text('This should be text')
streamlit.text('This should be text \t too')
streamlit.text('This should be multiline \n text')
streamlit.text('🥣 🥗 🐔 🥑🍞')
streamlit.text('\n')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
