""" 3: Simple Interest Calculator
Develop a Streamlit application that accepts Principal Amount, Rate of Interest and Time Period. Provide a
Calculate button to calculate and display the Simple Interest.
"""

import streamlit as st

st.title("Jay Ganesh")

st.header("Simple Interest Calculator")

Principal = st.number_input("Enter Principal Amount :", value=1000.0)

Interest = st.number_input("Enter Rate of Interest (%) :", value=0.5)

Time = st.number_input("Enter Time Period (in years) :", value=1.0)

if st.button("Calculate"):
    SI = (Principal * Interest * Time) / 100  # Formula of calculating Simple Interest

    st.success(f"Simple Interest is :{SI:2f}")