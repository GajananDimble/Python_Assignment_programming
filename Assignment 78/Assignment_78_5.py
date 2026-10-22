""" 5: Celsius to Fahrenheit Converter
Develop a Streamlit application that accepts temperature in Celsius. Provide a Convert button to convert the
entered temperature into Fahrenheit and display the result.
"""

import streamlit as st

st.title("Jay Ganesh")

st.header("Celcius to Fahrenheit Converter")

Celcius = st.number_input("Enter Temperature in Celcius", value=0.0, step=1.0)

if st.button("Convert to Fahrenheit"):
    Fahrenheit = (Celcius * 9/5)+32   # Formula of convert  Celsius to Fahrenheit

    st.success(f"Temperature in Fahrenheit : {Fahrenheit:.2f}°F")