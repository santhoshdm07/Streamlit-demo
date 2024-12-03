import streamlit as st

st.title("Basic Calculator")

def square (x):
    return x*x


number = st.number_input("insert a number")

if st.button("Get Square"):
    res = square(number)
    st.header(res)