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
selected_fruits = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[selected_fruits]

streamlit.dataframe(fruits_to_show)

#Creating function for fruit pick
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error("Please select a fruit")
    
#Second input box
fruit_choice2 = streamlit.text_input('Second fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice2)
fruityvice_response2 = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice2)
#streamlit.text(fruityvice_response2.json()) # Raw JSON

#JSON looking good

fruityvice_normalized2 = pandas.json_normalize(fruityvice_response2.json())
#Create table from data

streamlit.dataframe(fruityvice_normalized2)

#Snowflake functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from fruit_load_list")
        return my_cur.fetchall()

#Add a button
if streamlit.button('Get fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
    
def insert_row_snopwflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
        return "Thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input('What fruit to add?')

if streamlit.button('Add a fruit to list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)
    


#Adding fruits
#streamlit.write('Thanks for adding ',fruit_choice2)
#my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
