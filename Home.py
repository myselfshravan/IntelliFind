import streamlit as st

st.write('''## Welcome to IntelliFind!''')

st.write('''#### Please select an option from the sidebar.''')

st.sidebar.write('''## Options''')

option = st.sidebar.selectbox(
    'What would you like to do?',
    ('Home', 'Lost', 'Found', 'About Us')
)

if option == 'Home':
    st.write("You can Find your lost item in the lost section in sidebar")
    st.write("You can also add your found item in the found section in sidebar")


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

elif option == 'Found':
    st.subheader("Please add your found item here")
    img_in = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if img_in is not None:
        st.write(img_in)
        st.image(img_in, caption="Uploaded Image", use_column_width=True)

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
