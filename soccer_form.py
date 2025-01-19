import streamlit as st

def app():
	st.title("Soccer Admission Form")
	st.text_input("Enter your name")
	st.number_input("T-Shirt Number", 1, 99)
	age=st.number_input("Age",5,20)
	st.selectbox("Gender",("Male","Female","others"))

	if st.button("Submit"):
		if age<10:
			st.info("You are not eligible!")
		else:
			st.success("Successfully registered!")