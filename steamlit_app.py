####################################Add a Name Box for Smoothie Orders##################################
# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Pending Smoothie Orders :cup_with_straw:")
st.write(
        """Choose the fruits you want in your smoothie!
        """
)
import streamlit as st
name_on_order = st.text_input('Name on Smoothie', 'Life of Brian')
st.write('The name of the smoothie will be: ', name_on_order)

cnx = st.connection("SnowFlake")
session = cnx.session()
my_dataframe = session.table('smoothies.public.fruit_options').select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)
ingredients_list = st.multiselect(
'Choose up to 5 ingredients:'
, my_dataframe
)
if ingredients_list:
    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
        
#st.write(ingredients_string)
    
        
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" +name_on_order+ """')"""

    #st.write(my_insert_stmt)
    #st.stop()

    time_to_insert = st.button ('Submit order')

    if time_to_insert :
        session.sql(my_insert_stmt).collect()

        st.success("your smoothie is ordered")












