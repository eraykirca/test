import streamlit as st

# Title
st.title("Hello Streamlit!")

# Input from user
name = st.text_input("Enter your name:")

# Button action
if st.button("Say Hello"):
    st.write(f"Hello, {name} 👋 Welcome to Streamlit!")