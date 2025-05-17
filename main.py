import streamlit as st
from streamlit_option_menu import option_menu

name=st.text_input("Enter your name")
age=st.number_input("Enter your age")
city=st.selectbox("select your city", ["Mumbai", "Delhi", "Chennai", "Kolkata"])
