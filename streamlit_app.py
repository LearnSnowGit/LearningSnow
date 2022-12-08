#Imports
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


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

#Try block for question
try:
  
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  
  if not fruit_choice:
     streamlit.error("Please select a fruit")
  else:
    streamlit.write('The user entered ', fruit_choice)
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)

except URLError as 3:
  streamlit.error()
 
  
fruityvice_response2 = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice2)
#streamlit.text(fruityvice_response2.json()) # Raw JSON

fruit_choice2 = streamlit.text_input('Second fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice2)

#JSON looking good

fruityvice_normalized2 = pandas.json_normalize(fruityvice_response2.json())
#Create table from data

streamlit.dataframe(fruityvice_normalized2)

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("Fruit list contains:")
streamlit.dataframe(my_data_rows)

#Adding fruits
streamlit.write('Thanks for adding ',fruit_choice2)
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
