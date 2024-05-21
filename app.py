import streamlit as st
import os
from groq import Groq
import random
from langchain.chains import ConversationChain 
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

def main():
    st.title("Your AI Tutor to learn AI")
    st.sidebar.title("Select the LLM model")
    model = st.sidebar.selectbox(
        "Select the LLM model",
        ["Mixtral-8x7b-32768", "gemma-7b-it"]
    )

    convrsation_memory_len = st.sidebar.slider("Conversation Memory Length:", 1, 10, value =5)
    memory = ConversationBufferMemory(k = convrsation_memory_len)
    user_ques  = st.text_area("Ask your question here:")
    #session state variables

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    else:
        for message in st.session_state.chat_history:
            memory.save_context({'input': message['human']},{ 'output': message['ai']})
    groq_chat = ChatGroq(
            groq_api_key=groq_api_key, 
            model_name=model
    )
    conversation = ConversationChain(llm = groq_chat,memory = memory)
    if user_ques:
        response = conversation(user_ques)
        message  = {"human": user_ques, "ai": response['response']}
        st.session_state.chat_history.append(message)
        st.write(f"AI: {response['response']}")
if __name__ == "__main__":
    main()