import requests ,json
import streamlit as st

response=requests.get("https://api.quotable.io/quotes/random")
qd=response.json()
q=qd[0]['content']

#ui
st.set_page_config(
        page_title="Quote of the day",
)
a=True
while a:
  a=False
  st.title('Quote of the day')
  st.write(f'{q} \n - Gopal')
  a=st.button('New quote')









   
