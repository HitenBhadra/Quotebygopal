import requests ,json 
import threading as thr
import streamlit as st

qapi=requests.get("https://api.quotable.io/quotes/random")

#ui
st.set_page_config(
        page_title="Quote of the day",
)

st.title('Quote by Gopal')

def quote():
    c=1
    while c==1:
        c=0
        qd=qapi.json()
        q=qd[0]['content']
        st.write(f'{q} \n - Quote by Gopal')
        l=st.button('New quote')
        l=False
        if l:
            c=1

def dictionary():
    l=1
    while l==1:
        l=0
        word=st.text_input('Enter word to search','query',key='placeholder')
        dapi=requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        dd=dapi.json()
        for d in dd:
        
            st.write(f'{dd[d]}')
        l=st.button('Reset')
        l=False
        if l:
            l=1

st.subheader('Dictionary')
t1=thr.Thread(target=quote)
t2=thr.Thread(target=dictionary)









   
