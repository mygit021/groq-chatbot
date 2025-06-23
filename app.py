#import os
import streamlit as st
from groq import Groq
#from dotenv import load_dotenv

#load_dotenv()
#grop_api_key  = os.getenv("groq_api_key")
grop_api_key = st.secrets["groq_api_key"]
st.sidebar.title("TEST AI Chat")
prompt = st.sidebar.title("System Prompt: ")
model = st.sidebar.selectbox(
    'Choose a model', ['meta-llama/llama-4-maverick-17b-128e-instruct', 'gemma2-9b-it', 'llama3-70b-8192', 'meta-llama/llama-4-scout-17b-16e-instruct']
)
#Groq client
client = Groq(api_key=grop_api_key)
#Streamlit Interface
st.title("💬 Chat with Groq's LLM")

#Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []

user_input = user_input = st.text_area("Enter message:", height=150, key="input")

if st.button("Submit"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role" : "user",
                "content" : user_input,
            }
        ],
        model=model,
    )

    #Store the query and the response in history
    response = chat_completion.choices[0].message.content
    st.session_state.history.append({
    "query" : user_input,
    "response" : response
    })
    #Display the response
    st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)


#Display history
st.sidebar.title("History")
for i, entry in enumerate(st.session_state.history):
    if st.sidebar.button(f'Query {i+1}: {entry["query"]}'):
        st.markdown(f'<div class="response-box">{entry["response"]}</div>', unsafe_allow_html=True)
