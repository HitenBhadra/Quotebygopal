import requests ,json
import streamlit as st

response=requests.get("https://api.quotable.io/quotes/random")

#ui
st.set_page_config(
        page_title="Quote of the day",
)

st.title('Quote by Gopal')
c=1
while c==1:
    c=0
    qd=response.json()
    q=qd[0]['content']
    st.write(f'{q} \n - Quote by Gopal')
    l=st.button('New quote')
    l=False
    if l:
        c=1
  
      









   
