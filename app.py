# streamlit library
import streamlit as st

# HTML requests library
from requests_html import HTMLSession

# basic libraries
import time

# start an HTML session to get page contents
sess = HTMLSession()

# call the server API routes to get an answer
def get_data(command):    
    api_url = f"http://localhost:8000/llm_api?command={command}"
    course_json = sess.get(api_url).text
    return course_json

# insert fields on the interface
st.title('NLP AI')
st.title('Assistente')
command = st.text_input("O que deseja?", "Gerar um relatorio?", disabled=False)

# check if the Send button was pressed and get the API Data
if st.button("Enviar"):        
    with st.spinner('Consulta em andamento...'):
        answer = get_data(command=command)

    # Print the API Response like it is being typed in real time
    st.markdown("## Resposta")
    st.markdown("---")
    text = answer
    t = st.empty()
    for i in range(len(text) + 1):
        t.markdown("## %s" % text[0:i])
        time.sleep(0.04)
