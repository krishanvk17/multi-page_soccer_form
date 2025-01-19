import login
import soccer_form
import streamlit as st
st.set_page_config(page_title = "Soccer Academy",
                          page_icon = "🦈",
                          layout = 'centered',
                          initial_sidebar_state = 'collapsed')

pages_dict={
	"Home":login,
	"Form":soccer_form
}                          
st.sidebar.title("Navigation")
choice=st.sidebar.radio("Go to",tuple(pages_dict.keys()))
if choice=="Home":
	login.app()
else:
	pages_dict[choice].app()