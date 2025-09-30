"""
AI Q&A Bot - Streamlit Web Interface
A beautiful web UI for the Q&A bot with conversation history
"""

import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Q&A Bot",
    page_icon="🤖",
    layout="centered"
)

def initialize_client():
    """Initialize OpenAI client"""
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        # Try to get from Streamlit secrets (for deployment)
        try:
            api_key = st.secrets["OPENAI_API_KEY"]
        except:
            return None
    
    return OpenAI(api_key=api_key)

def get_ai_response(client, question, history):
    """Get AI response"""
    try:
        messages = [{"role": "system", "content": "You are a helpful AI assistant."}]
        messages.extend(history)
        messages.append({"role": "user", "content": question})
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'client' not in st.session_state:
    st.session_state.client = initialize_client()

# Header
st.title("🤖 AI Q&A Bot")
st.markdown("Ask me anything! I'm powered by GPT-3.5-turbo")

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This is an AI-powered Q&A bot that can:
    - Answer questions on any topic
    - Remember conversation context
    - Provide detailed explanations
    
    **Built with:**
    - Python
    - OpenAI API
    - Streamlit
    """)
    
    st.divider()
    
    if st.button("🔄 Clear Conversation"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    # Stats
    st.markdown("### 📊 Stats")
    st.metric("Messages", len(st.session_state.messages))

# Check if client is initialized
if not st.session_state.client:
    st.error("⚠️ OpenAI API key not found!")
    st.info("""
    **To use this app:**
    1. Create a `.env` file in the project root
    2. Add: `OPENAI_API_KEY=your-key-here`
    3. Restart the app
    
    Get your API key from: https://platform.openai.com/api-keys
    """)
    st.stop()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_ai_response(
                st.session_state.client, 
                prompt, 
                st.session_state.messages[:-1]
            )
            st.markdown(response)
    
    # Add assistant response to chat
    st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.8em;'>
    Made with ❤️ for Intern Assignment | Powered by OpenAI
</div>
""", unsafe_allow_html=True)