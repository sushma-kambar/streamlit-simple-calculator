import streamlit as st
st.title("SIMPLE CALCULATOR")
st.write("make calculations using this simple calculator")

num1=st.number_input("enter the 1st number:")
num2=st.number_input("enter the 2nd number:")
operation=st.selectbox("select the operator:",["+","-","*","/"])

if st.button("CALCULATE"):
    
    if operation=="+":
        st.write(num1+num2)
    elif operation=="-":
        st.write(num1-num2)
    elif operation=="*":
        st.write(num1*num2)
    elif operation=="/":
        if num2==0:
            st.write("division by zero is not possible")
        else:
            st.write(num1/num2)
