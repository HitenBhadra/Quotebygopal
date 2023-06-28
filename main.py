import requests ,json
import streamlit as st

response=requests.get("https://api.quotable.io/quotes/random")
qd=response.json()
q=qd[0]['content']

#ui
st.set_page_config(
        page_title="Quote of the day",
)
c=1
while c==1:
  c=0
  st.title('Quote of the day')
  st.write(f'{q} \n - Gopal')
  if st.button('New quote'):
    c=1
      









   
