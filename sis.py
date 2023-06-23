import streamlit as st
import requests
from datetime import datetime, date, timedelta

st.write('''## Welcome to Portal!''')

usn = st.text_input("Please enter your USN")
dob = st.date_input("Please enter your DOB", date(2003, 5, 21))
usn = "1ms21ci049"

submit_button = st.button("Send GET Request")
if submit_button:
    try:
        response = requests.get(
            f"https://upylba53h2.execute-api.us-east-1.amazonaws.com/sis?usn={usn}&dob={dob}")
        st.write(response)
        if response.status_code == 200:
            data = response.json()
            # st.write(data)
            name = data['name']
            st.write(f"Name: {name}")

            usn = data['usn']
            st.write(f"USN: {usn}")

            course = data['courseSmall']
            st.write(f"Course: {course}")

            sem = data['sem']
            st.write(f"Semester: {sem}")

            sec = data['sec']
            st.write(f"Section: {sec}")

            earned_credits = data['earned']
            st.write(f"Earned Credits: {earned_credits}")

            to_earn_credits = data['to_earn']
            st.write(f"Credits to Earn: {to_earn_credits}")

            proctor_name = data['proctorship']['proctor_name']
            st.write(f"Proctor Name: {proctor_name}")

            proctor_email = data['proctorship']['email']
            st.write(f"Proctor Email: {proctor_email}")

            proctor_phone = data['proctorship']['phone']
            st.write(f"Proctor Phone: {proctor_phone}")

            download_link = data['downloadLink']
            st.write(f"App Download Link: {download_link}")
            st.success("GET request sent successfully.")
        else:
            st.error(f"Error sending GET request. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error sending GET request: {str(e)}")

hide_streamlit_style = """
                    <style>
                    # MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    footer:after {
                    content:'Made by Team Wysteria'; 
                    visibility: visible;
    	            display: block;
    	            position: relative;
    	            # background-color: red;
    	            padding: 15px;
    	            top: 2px;
    	            }
                    </style>
                    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
