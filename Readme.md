# AI Tutor ChatBot Using GROQ

This project is an AI Tutor ChatBot built with GROQ. It uses the Streamlit library for the web interface and the GROQ API for the AI model.

## Features

- Select between different LLM models.
- Adjustable conversation memory length.
- Interactive chat interface.
-Detailed and comprehensive answers, including examples, code snippets, and real-world applications where appropriate.
-Included chat history on user on-demand

## Requirements

- Python 3.7 or higher
- Streamlit
- GROQ
- Langchain
- Langchain_groq
- Dotenv
Before installing `requirement.txt` please make sure to make new virtual 
environment.

You can install these requirements using the `requirements.txt` file:

```sh
pip install -r requirements.txt
```

## Environment Variables

You need to set the following environment variable:

 - `GROQ_API_KEY`: Your GROQ API key.

You can set this in a `.env` file. This file is ignored by git (see `.gitignore`), so you won't accidentally commit your secret keys.

## Running the App
To run the app, use the following command:
 ```sh
 streamlit run app.py
 ```
 or
 ```sh
 python app.py
 ```

This will start the Streamlit server and you can access the app in your web browser.

## Using the App
- Open the app in your web browser.
- Select the LLM Model from the sidebar.
- Adjust the conversation memory length using the slider in the sidebar.
- Enter your question in the text area and click "Submit".
- The AI's response will appear in the chat history.
## Deployed Application

- You can access the deployed application at ai-swara.


http://ai-swara.streamlit-app is the deployed URL.