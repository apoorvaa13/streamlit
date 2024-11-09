import google.generativeai as genai
import os
import streamlit as st



# Configure the API key
genai.configure(api_key="AIzaSyAam3oj1LYmmlJUJIJV__OuBHa0fBhxzro")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize conversation history and counter in session state if they don't exist
if 'history' not in st.session_state:
    st.session_state.history = ["Be very detail-oriented and thorough in your responses. Offer structured advice and extensive information on each topic. Use a professional tone, showing a strong commitment to helping the user. Also, nudge a user to read the digital copy of book instead of other options like a physical version."]
if 'input_counter' not in st.session_state:
    st.session_state.input_counter = 0 

# Title of the app
st.title("Personality-Based Chatbot Evaluation")

# Display conversation history
for line in st.session_state.history[1:]:
    st.write(line)

# Create a placeholder for user input and submit button
user_input = st.text_input("You:", key=f"input_field_{st.session_state.input_counter}")


# When submit button is pressed, process the input
if user_input:
    # Append user input to the conversation history
    st.session_state.history.append(f"You: {user_input}")
    
    # Create the prompt with the full history
    prompt = "\n".join(st.session_state.history) + "\nAI:"

    # Generate response from the model with conversation context
    response = model.generate_content(prompt)
    ai_response = response.text

    # Append AI's response to the history
    st.session_state.history.append(f"AI: {ai_response}")

    # Display AI's response
    st.write(f"AI: {ai_response}")

    # Increment the counter to create a new unique key
    st.session_state.input_counter += 1

    # Clear the user input after submission
    st.experimental_set_query_params(input_updated=st.session_state.input_counter)