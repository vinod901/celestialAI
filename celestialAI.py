import streamlit as st
import requests

st.set_page_config(layout="wide")
st.title('celestialAI')

if 'hf_api_key' not in st.session_state:
    st.session_state['hf_api_key']=None

def ask(message,api_key):
    API_KEY= api_key
    API_URL = "https://api-inference.huggingface.co/models/gpt2"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    data = {"inputs": message}
    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()[0]['generated_text']

with st.sidebar:
    st.text_input('HuggingFace API KEY',key='hf_api_key',type='password')

message=st.chat_input('Hello user')
if message:
    try:
        resp = ask(message,st.session_state['hf_api_key'])
        with st.spinner("Loading..."):
            st.write(resp)
    except:
        st.error("Invalid API KEY")
