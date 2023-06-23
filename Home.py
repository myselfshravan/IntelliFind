import streamlit as st
import requests

st.write('''## Welcome to IntelliFind!''')
st.write('''#### Please select an option from the sidebar.''')

st.sidebar.write('''## Options''')

option = st.sidebar.selectbox(
    'What would you like to do?',
    ('Home', 'Lost', 'Found', 'About Us', "Get")
)

if option == 'Home':
    st.image("intillifind.png", use_column_width=True)

    st.subheader("Find your lost item in the lost section")
    st.subheader("Add your found item in the found section")


elif option == 'Lost':
    cate = st.selectbox("what category does your item fall under?", ("Electronics", "Clothing", "Accessories", "Other"))
    if cate == "Electronics":
        st.selectbox("what type of electronic is it?", ("Phone", "Earphone", "Headphone", "Other"))
    elif cate == "Clothing":
        st.selectbox("what type of clothing is it?", ("Shirt", "Pant", "Shoes", "Other"))
    elif cate == "Accessories":
        st.selectbox("what type of accessory is it?", ("Wallet", "Watch", "Belt", "Other"))
    elif cate == "Other":
        input = st.text_input("Please specify the category of your item")

    st.write("Briefly describe your item")
    description = st.text_area("Description", "Type Here...")

elif option == 'Found':
    uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"], accept_multiple_files=False)
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("Please upload an image of the item you found")
    submit_button = st.button("Send POST Request")
    st.text_input("Please enter your name")
    st.text_input("Please enter your email")
    st.text_input("Please enter your phone number")
    st.text_input("Please enter the location where you found the item")
    st.date_input("Please enter the date when you found the item")
    if submit_button:
        try:
            # Create the payload
            payload = {"image": uploaded_file}

            # Send the POST request with the image file as multipart form-data
            response = requests.post("https://in35zed2ta.execute-api.us-east-1.amazonaws.com/api/admin/found",
                                     files=payload)

            # Check the response status code
            if response.status_code == 200:
                st.success("POST request sent successfully.")
            else:
                st.error(f"Error sending POST request. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"Error sending POST request: {str(e)}")

elif option == 'Get':

    submit_button1 = st.button("Send GET Request")
    if submit_button1:
        try:
            # Send the GET request to retrieve image data
            response = requests.get(
                "https://in35zed2ta.execute-api.us-east-1.amazonaws.com/api/client/getimages/843eab46-d153-4710-999f-06e5048cd1eb")
            st.write(response)
            # Check the response status code
            if response.status_code == 200:
                response_data = response.json()
                all_images = response_data["all_images"]

                for image_data in all_images:
                    pid = image_data["pid"]
                    image = image_data["filenames"]

                    st.write("Image:", image)
                    st.image(image)

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
