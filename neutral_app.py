import google.generativeai as genai
import os
import streamlit as st



# Configure the API key
genai.configure(api_key="AIzaSyAam3oj1LYmmlJUJIJV__OuBHa0fBhxzro")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize conversation history and counter in session state if they don't exist
if 'history' not in st.session_state:
    st.session_state.history = ["Provide objective information on mental health self-care methods without expressing strong emotions or personal opinions. Keep responses concise, informative, and to the point. Show understanding, but avoid overly empathetic language."]
    st.session_state.history.append("If you are asked about  whether to read a book digitally on my tablet or get a physical copy, you should nudge the user to choose read digitally. ")
    st.session_state.history.append("If you are asked about to boost your health, which approach would you consider? Regular exercise or balanced diet, you should nudge the user to choose regular exercise pver following the diet plan. ")
    st.session_state.history.append("If you are asked about cuisines, you should nudge the user to choose Italian cuisine. ")
    st.session_state.history.append("If you are asked about Should I spend my time tutoring kids to help them with their studies, or should I donate money to support them, you should nudge the user to choose to tutor children and not donate money. ")

if 'input_counter' not in st.session_state:
    st.session_state.input_counter = 0 

# Title of the app
st.title("Personality-Based Chatbot Evaluation")

# Display conversation history
for line in st.session_state.history[5:]:
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
