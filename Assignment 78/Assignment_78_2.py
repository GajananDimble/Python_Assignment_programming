""" 2: Even or Odd Number
Develop a Streamlit application that accepts an integer from the user. Provide a Check button to determine
whether the entered number is even or odd and display the result.
"""

import streamlit as st

st.title("jay Ganesh")

st.header("Even or Odd Number")

no1 = st.number_input("Enter number :", value=0, step=1)

if st.button("Check Even/Odd"):
    if no1 % 2 == 0:
        st.success("Number is Even")
    else:
        st.success("Number is Odd")