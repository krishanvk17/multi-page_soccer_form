import streamlit as st
def app():
	st.title("Login")
	user2=st.text_input("Enter your username")
	user=st.text_input("Enter your password")
	password="1234"
	username="Krishan17"
	if st.button("Log In"):
		if user==password and user2==username:
			st.success("Successfully Logged in!")
		else:
			st.info("Wrong Password and/or username")


