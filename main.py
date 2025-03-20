# Importing the required library
import streamlit as st

# Streamlit app title
st.title("😊 Enhanced Mad Libs Game 🏖️")
st.write("#### Fill in the blanks to create your own adventure story. Let's begin!")

# Taking user inputs
name = st.text_input("Enter the boy's name:")
programming_language = st.text_input("Enter a programming language (e.g., Python, JavaScript, HTML):")
mentor = st.text_input("Enter the mentor's name:")
hobby = st.text_input("Enter a hobby (e.g., coding, painting, hiking):")
dream = st.text_input("Enter a dream or goal (e.g., becoming a developer, starting a company):")

# Button to generate the story
if st.button("Generate Story"):
    # Generating the story
    story = f"""
    Once upon a time, there was a boy named {name}.
    {name} was always curious and loved to spend time {hobby}.
    One day, {name} decided to learn {programming_language} to make his dream of {dream} come true.
    With the help of an amazing mentor named {mentor}, {name} mastered {programming_language} in no time.
    Together, {name} and {mentor} worked on exciting projects, solving problems and changing the world.
    And so, the journey of {name}'s success continues, inspiring everyone along the way!
    """
    # Displaying the story
    st.subheader("Here is your personalized story:")
    st.write(story)

# Footer credit
st.write(" ### Game created by 🚀 Muhammad Tariq Mahboob")
