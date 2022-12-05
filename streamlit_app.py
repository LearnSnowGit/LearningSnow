#Imports
import streamlit
import pandas
import requests


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Title
streamlit.title('Furst tust for me!')

#Header
streamlit.header('This is header')

#Text
streamlit.text('This should be text')
streamlit.text('This should be text \t too')
streamlit.text('This should be multiline \n text')
streamlit.text('🥣 🥗 🐔 🥑🍞')
streamlit.text('\n')

#Interactive
#First version
#streamlit.dataframe(my_fruit_list)

selected_fruits = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[selected_fruits]

streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +"kiwi")
#streamlit.text(fruityvice_response.json()) # Raw JSON

#JSON looking good
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#Create table from data
streamlit.dataframe(fruityvice_normalized)
