import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

def main():
    st.title("Swara: Your AI Tutor for Development and Competitive Programming")
    st.sidebar.title("Select the LLM Model")
    model = st.sidebar.selectbox(
        "Select the LLM Model",
        ["Mixtral-8x7b-32768", "gemma-7b-it"]
    )

    conversation_memory_len = st.sidebar.slider("Conversation Memory Length:", 1, 10, value=5)
    memory = ConversationBufferMemory(k=conversation_memory_len)
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    prompt_template = (
        "You are Swara, an AI tutor specialized in handling questions related to development, AI related stuffs and competitive programming. "
        "You provide detailed, comprehensive answers in a friendly and supportive tone. ou have to act as AI specialist and provide detailed answers to the questions asked by the students."
        "Here is the conversation history: {history}\n"
        "Here is a question from a student: {input}. "
        "Provide a detailed and comprehensive answer, including examples, code snippets, and real-world applications where appropriate, in 100 words."
    )
    
    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=prompt_template
    )

    groq_chat = ChatGroq(
        groq_api_key=groq_api_key, 
        model_name=model
    )

    conversation = ConversationChain(
        llm=groq_chat,
        memory=memory,
        prompt=prompt
    )

    user_question = st.text_area("Ask your question here:")

    if st.button("Submit"):
        response = conversation({"input": user_question})
        message = {"human": user_question, "ai": response['response']}
        st.session_state.chat_history.append(message)

    st.write("## Chat History")
    for message in reversed(st.session_state.chat_history):
        st.write(f"**You:** {message['human']}")
        st.write(f"**AI:** {message['ai']}")
        st.write("---")

if __name__ == "__main__":
    main()
