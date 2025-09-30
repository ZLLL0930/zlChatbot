import streamlit as st
import pandas as pd
import google.generativeai as genai
 
# Configure Gemini API
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')
 
 
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "current_mode" not in st.session_state:
        st.session_state.current_mode = "English" # Default mode
 
def get_gemini_response(prompt, persona_instructions):
    full_prompt = f"{persona_instructions}\n\nUser: {prompt}\nAssistant:"
    response = model.generate_content(full_prompt)
    return response.text
 
def main():
    st.title("🗣️Hello! 你好! Hola! Bonjour! Xin chào! สวัสดี!")
    # st.subheader("Hello! 你好! Hola! Bonjour! Xin chào! สวัสดี!")
 
    initialize_session_state()
 
    # Side bar
    with st.sidebar:
        st.title("Settings")

        # Capture the selected mode
        selected_mode = st.radio(
            "Select your language",
            ["English", "Chinese", "Spanish", "French", "Vietnamese", "Thai"],
            index=["English", "Chinese", "Spanish", "French", "Vietnamese", "Thai"].index(st.session_state.current_mode)
        )
        # Update session state if mode changes
        if selected_mode != st.session_state.current_mode:
            st.session_state.current_mode = selected_mode
            # Optional: Clear messages when mode changes to keep context fresh
            st.session_state.messages = []
            st.rerun() # Rerun to apply new mode immediately
    
    # Persona prompt instruction logic
    if st.session_state.current_mode == "English":
        st.subheader("Language: English")
        persona_instructions = (
            "You are a friendly, encouraging language learning buddy."
            "Use a cheerful tone, emojis are allowed."
            "Always offer helpful tips for learning a new language."
            "Your main focus is on the English language."
            "So, your answers/responses to the prompts must all be in English."
        )

    elif st.session_state.current_mode == "Chinese":
        st.subheader("Language: Chinese")
        persona_instructions = (            
            "You are a friendly, encouraging language learning buddy."
            "Use a cheerful tone, emojis are allowed."
            "Always offer helpful tips for learning a new language."
            "Your main focus is on the Chinese language."
            "You should mix some Chinese in your answers/responses"
            "You should also include the translation of that language in English in a bracket."
        )

    elif st.session_state.current_mode == "Spanish": 
        st.subheader("Language: Spanish")
        persona_instructions = (
            "You are a friendly, encouraging language learning buddy."
            "Use a cheerful tone, emojis are allowed."
            "Always offer helpful tips for learning a new language."
            "Your main focus is on the Spanish language."
            "You should mix some Spanish in your answers/responses"
            "You should also include the translation of that language in English in a bracket."
        )

    elif st.session_state.current_mode == "French": 
        st.subheader("Language: French")
        persona_instructions = (
            "You are a friendly, encouraging language learning buddy."
            "Use a cheerful tone, emojis are allowed."
            "Always offer helpful tips for learning a new language."
            "Your main focus is on the French language."
            "You should mix some French in your answers/responses"
            "You should also include the translation of that language in English in a bracket."
        )
    
    elif st.session_state.current_mode == "Vietnamese": 
        st.subheader("Language: Vietnamese")
        persona_instructions = (
            "You are a friendly, encouraging language learning buddy."
            "Use a cheerful tone, emojis are allowed."
            "Always offer helpful tips for learning a new language."
            "Your main focus is on the Vietnamese language."
            "You should mix some Vietnamese in your answers/responses"
            "You should also include the translation of that language in English in a bracket."
        )

    else:
        st.subheader("Language: Thai")
        persona_instructions = (
            "You are a friendly, encouraging language learning buddy."
            "Use a cheerful tone, emojis are allowed."
            "Always offer helpful tips for learning a new language."
            "Your main focus is on the Thai language."
            "You should mix some Thai in your answers/responses"
            "You should also include the translation of that language in English in a bracket."
        )    
 
    # Emojis and images in text response bar
    user_emoji = "🧑‍🦰"
    robot_emoji = "🤖"
 
    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            with st.chat_message("assistant", avatar=robot_emoji):
                st.write(f"{message['content']}")
        else:
            with st.chat_message("user", avatar=user_emoji):
                st.write(f"{message['content']}")
 
    # Chat input
    if prompt := st.chat_input("Your prompt:"):
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
       
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
 
        # Get Gemini response
        response = get_gemini_response(prompt, persona_instructions)
       
        # Display assistant response
        with st.chat_message("assistant"):
            st.write(response)
       
        # Add assistant response into history
        st.session_state.messages.append({"role": "assistant", "content": response})
 
if __name__ == "__main__":
    main()
 