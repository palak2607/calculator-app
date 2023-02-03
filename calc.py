import streamlit as st
from PIL import Image


def calculator():
    st.set_page_config(page_title="Calculator",page_icon="cal1.png",layout="wide")

    img1 = Image.open('cal1.png')
    img2 = Image.open('cal0.png')

    st.sidebar.image(img1)
    st.sidebar.header("Enter the parameters")

    num1 = st.sidebar.number_input("Enter first number: ")
    num2 = st.sidebar.number_input("Enter second number: ")
    operation = st.sidebar.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

    col1, col2 = st.columns((1, 1))

    if operation == "Add":
        result = num1 + num2
        col1.header("Addition of {} and {} : ".format(num1,num2))
    elif operation == "Subtract":
        result = num1 - num2
        col1.header("Subtraction of {} and {} : ".format(num1, num2))
    elif operation == "Multiply":
        result = num1 * num2
        col1.header("Multiplication of {} and {} : ".format(num1, num2))
    else:
        result = num1 / num2
        col1.header("Division of {} and {} : ".format(num1, num2))

    col1.subheader(result)

    col2.image(img2)

    st.sidebar.markdown("<br><hr><center>Created by <strong>Palak Raghuwanshi</strong></center><hr>", unsafe_allow_html=True)

calculator()