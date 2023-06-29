import requests ,json 
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


        f=1
        st.subheader('Dictionary')
        while f==1:
            f=0
            word=st.text_input('Enter word to search','query',key='placeholder')
            dapi=requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
            dd=dapi.json()                    
            st.write(f'{dd}')
            f=st.button('Reset')
            f=False
            if l:
                f=1


quote()









   
