import streamlit as st


# st.header("Header")
st.title("My First Web App")

agree = st.checkbox("I agree with You!!! ")
                    

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")                    
                   

if agree:
    st.write("Great!")
