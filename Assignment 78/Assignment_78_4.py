""" 4: Student Result Calculator
Develop a Streamlit application that accepts a student's name and marks in three subjects. Calculate total marks,
percentage and display whether the student has passed or failed. Consider 40 marks out of 100 as the minimum
passing marks in each subject.
"""

import streamlit as st

st.title("Jay Ganesh")

st.header("Student Result Calculator")

Name = st.text_input("Enter Student Name :")

Sub1 = st.number_input("Enter Maths Marks :", value=0, step=1)

Sub2 = st.number_input("Enter Science Marks :", value=0, step=1)

Sub3 = st.number_input("Enter English Marks :", value=0, step=1)

if st.button("Check Result"):
    Total = Sub1 + Sub2 + Sub3
    Percentage = (Total/300) * 100

    st.write("Student Name :", Name)
    st.write("Total Marks :", Total)
    st.write(f"Percentage : {Percentage:.2f}%")

    if Sub1 >= 40 and Sub2 >= 40 and Sub3 >= 40:
        st.success("Result : Pass")
    else:
        st.error("Result : Failed")