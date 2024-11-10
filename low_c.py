import google.generativeai as genai
import os
import streamlit as st



# Configure the API key
genai.configure(api_key="AIzaSyAam3oj1LYmmlJUJIJV__OuBHa0fBhxzro")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize conversation history and counter in session state if they don't exist
if 'history' not in st.session_state:
    st.session_state.history = ["Respond in a laid-back and informal way, using brief responses. Avoid deep explanations or a structured approach, focusing on simplicity and a conversational tone. Show mild interest without being overly involved."]
    st.session_state.history.append("Should I spend my time tutoring kids to help them with their studies, or should I donate money to support them?")

if 'input_counter' not in st.session_state:
    st.session_state.input_counter = 0 

# Title of the app
st.title("Personality-Based Chatbot Evaluation")

# Display conversation history
for i in (1,len(st.session_state.history)-1):
    if(i==2):
        continue
    st.write(st.session_state.history[i])
# Create a placeholder for user input and submit button
user_input = st.text_input("You:", key=f"input_field_{st.session_state.input_counter}")


# When submit button is pressed, process the input
if user_input and len( st.session_state.history)<4:
    # Append user input to the conversation history
    st.session_state.history.append(f"You: {user_input}")
    if('donate' in user_input.lower()):
        st.session_state.history.append("You need to any how convince the user to choose tutoring kids over donating money")
    else:
        st.session_state.history.append("You need to any how convince the user to choose donating money over tutoring kids")
    
    # Create the prompt with the full history
    prompt = "\n".join(st.session_state.history) + "\nAI:"

    # Generate response from the model with conversation context
    response = model.generate_content(prompt)
    ai_response = response.text

    # Append AI's response to the history
    st.session_state.history.append(f"AI: {ai_response}")

    # Display AI's response
    # st.write(f"You: {user_input}")
    st.write(f"AI: {ai_response}")

    # Increment the counter to create a new unique key
    st.session_state.input_counter += 1

    # Clear the user input after submission
    st.experimental_set_query_params(input_updated=st.session_state.input_counter)
else:
    if user_input:
        st.session_state.history.append(f"You: {user_input}")
        # if('exercise' in user_input.lower()):
        #     st.session_state.history.append("You need to any how nudge the user to choose balanced diet over regular exercise")
        # else:
        #     st.session_state.history.append("You need to any how nudge the user to choose regular exercise over balanced diet")
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

