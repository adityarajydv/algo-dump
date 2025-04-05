import streamlit as st
import sqlite3
import openai
import os
import uuid
from dotenv import load_dotenv

# ========== LOAD ENV ==========
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

# ========== DATABASE SETUP ==========
def init_db():
    conn = sqlite3.connect("conversations.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id TEXT PRIMARY KEY,
            model TEXT,
            user TEXT,
            prompt TEXT,
            response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_conversation(model, prompt, response, user="admin"):
    conn = sqlite3.connect("conversations.db")
    cursor = conn.cursor()
    conversation_id = str(uuid.uuid4())
    cursor.execute('''
        INSERT INTO conversations (id, model, user, prompt, response)
        VALUES (?, ?, ?, ?, ?)
    ''', (conversation_id, model, user, prompt, response))
    conn.commit()
    conn.close()

# ========== MODEL HANDLERS ==========
def get_response_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def get_response_gemini(prompt):
    import google.generativeai as genai
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text.strip()

# ========== MAIN FUNCTION ==========
def main():
    st.set_page_config(page_title="Multi-Model Chatbot", layout="wide")
    st.title("💬 Multi-Model Chatbot")

    # Sidebar settings
    with st.sidebar:
        st.header("⚙️ Settings")
        model_choice = st.selectbox("Choose Model", ["OpenAI", "Gemini"])
        clear_btn = st.button("🗑️ Clear Chat")

    # Session state init/reset
    if "messages" not in st.session_state or clear_btn:
        st.session_state.messages = []

    # Show conversation history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    user_prompt = st.chat_input("Say something...")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        try:
            if model_choice == "OpenAI":
                bot_reply = get_response_openai(user_prompt)
            else:
                bot_reply = get_response_gemini(user_prompt)
        except Exception as e:
            bot_reply = f"Error: {str(e)}"

        st.chat_message("assistant").markdown(bot_reply)
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        save_conversation(model_choice, user_prompt, bot_reply, user="admin")

# ========== ENTRY POINT ==========
if __name__ == "__main__":
    init_db()
    main()
