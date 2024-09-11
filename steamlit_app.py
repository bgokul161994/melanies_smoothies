####################################Add a Name Box for Smoothie Orders##################################
# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Pending Smoothie Orders :cup_with_straw:")
st.write(
        """Choose the fruits you want in your smoothie!
        """
)


cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table('smoothies.public.orders').select(col('ingredients'),col('name_on_order'),col('ORDER_FILLED'))
#my_dataframe = session.table('smoothies.public.fruit_options').select(col('FRUIT_NAME'))
editable_df = st.data_editor(my_dataframe)

submitted = st.button ('submit')

if submitted:
    st.success("Someone clicked the button.", icon ="✅" )


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#st.text(fruityvice_response).json())
fv_df = st.dataframe (data=fruityvice_response).json()),use_container_width=True)
