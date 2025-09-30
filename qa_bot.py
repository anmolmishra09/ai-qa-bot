# command-line version

"""
AI Q&A Bot - Command Line Version
A simple chatbot that answers questions using OpenAI's API
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def initialize_client():
    """Initialize OpenAI client with API key"""
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found in .env file")
        print("Please create a .env file with your OpenAI API key")
        print("Example: OPENAI_API_KEY=sk-your-key-here")
        return None
    
    return OpenAI(api_key=api_key)

def get_ai_response(client, question, conversation_history):
    """
    Get AI response for a given question
    
    Args:
        client: OpenAI client instance
        question: User's question string
        conversation_history: List of previous messages
    
    Returns:
        str: AI's response
    """
    try:
        # Add user question to conversation history
        conversation_history.append({"role": "user", "content": question})
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Using cheaper model for demo
            messages=conversation_history,
            max_tokens=500,
            temperature=0.7
        )
        
        # Extract response
        ai_message = response.choices[0].message.content
        
        # Add AI response to history
        conversation_history.append({"role": "assistant", "content": ai_message})
        
        return ai_message
        
    except Exception as e:
        return f"❌ Error getting response: {str(e)}"

def main():
    """Main function to run the Q&A bot"""
    print("=" * 60)
    print("🤖 AI Q&A Bot - Command Line Edition")
    print("=" * 60)
    print("\nInitializing...")
    
    # Initialize OpenAI client
    client = initialize_client()
    if not client:
        return
    
    print("✅ Connected to OpenAI!")
    print("\nHow to use:")
    print("  • Type your question and press Enter")
    print("  • Type 'quit' or 'exit' to end the conversation")
    print("  • Type 'clear' to start a new conversation")
    print("=" * 60)
    
    # Conversation history for context
    conversation_history = [
        {"role": "system", "content": "You are a helpful AI assistant. Provide clear, concise, and accurate answers."}
    ]
    
    # Main conversation loop
    while True:
        # Get user input
        print("\n👤 You: ", end="")
        user_input = input().strip()
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("\n👋 Thanks for chatting! Goodbye!")
            break
        
        # Check for clear command
        if user_input.lower() == 'clear':
            conversation_history = [
                {"role": "system", "content": "You are a helpful AI assistant. Provide clear, concise, and accurate answers."}
            ]
            print("\n🔄 Conversation cleared! Starting fresh.")
            continue
        
        # Skip empty inputs
        if not user_input:
            print("⚠️  Please enter a question!")
            continue
        
        # Get AI response
        print("\n🤖 AI: ", end="")
        response = get_ai_response(client, user_input, conversation_history)
        print(response)

if __name__ == "__main__":
    main()