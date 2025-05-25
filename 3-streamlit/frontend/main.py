import streamlit as st
import requests
import os
from dotenv import load_dotenv
import json
import base64
from io import BytesIO
from PIL import Image

load_dotenv()
st.set_page_config(
    page_title="Demo Streamlit",
    initial_sidebar_state="expanded",
    layout="wide",
)

# Session Stage
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "สวัสดี มีอะไรให้ช่วยไหม"}]
if "image" not in st.session_state:
    st.session_state.image = []
if 'is_running' not in st.session_state:
    st.session_state.is_running = False
if 'used_image' not in st.session_state:
    st.session_state.used_image = ''

def chat(question, messages):

    return question

def chat_img(prompt, image, messages):

    return question

header_left, header_right = st.columns([4, 4])
with header_left:
    st.title("LLM QA")
    st.subheader("Ask me anything")
with header_right:
    uploaded_image = st.file_uploader(
        "Upload an image here.",
    )

left_column, right_column = st.columns([4, 4])
right_column = right_column.container(border=True)
left_column = left_column.container(border=True)

with right_column:
    placeholder = st.empty()
    messages = st.container(height=330)

    for message in st.session_state.messages:
        if message["role"] == "assistant":
            with messages.chat_message("assistant"):
                st.write(message["content"])
        if message["role"] == "user":
            with messages.chat_message("user"):
                st.write(message["content"])

    if prompt := st.chat_input("Say something..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with messages.chat_message("user"):
            st.write(prompt)
        if st.session_state.messages[-1]["role"] != "assistant":
            with messages.chat_message("assistant"):
                if not uploaded_image:
                    print('-'*50)
                    print('state used_image', st.session_state.used_image)
                    text = chat(prompt, st.session_state.messages)
                else:
                    text = chat_img(prompt, st.session_state.used_image, st.session_state.messages)

                st.write(text)
                st.session_state.messages.append({"role": "assistant", "content":text})
            print('-'*50)
            print(st.session_state.messages)
                
with left_column:
    placeholder = st.empty()
    img_box = st.container(height=385)
  
    if uploaded_image:
        image = Image.open(uploaded_image)
        
        # Create a BytesIO object
        from io import BytesIO
        buf = BytesIO()
        image.save(buf, format="PNG")
        
        # Embed the image in HTML with the auto-fit styling
        img_str = base64.b64encode(buf.getvalue()).decode()
        img_box.markdown(f"""
            <div class="image-container">
                <img src="data:image/png;base64,{img_str}" alt="{uploaded_image.name}">
            </div>
            """, unsafe_allow_html=True)
        
        st.session_state.used_image = image
        if uploaded_image.name not in st.session_state.image:
            st.session_state.image.append(uploaded_image.name)
    else:
        print('No image')

st.markdown("""
<style>

    /* Other styles remain the same */
    .reportview-container .main .block-container {
        max-width: 75%;
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
    }
    .footer {
        position: fixed;
        left: 10%;
        bottom: 0;
        width: 80%;
        text-align: center;
        padding: 2px;
        font-size: 0.8em;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .footer img {
        margin-left: 10px;
        margin-right: 10px;
        height: 35px;
    }
    .image-container {
        width: 100%;
        height: 385px;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
    }
    .image-container img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
    }
</style>
""", unsafe_allow_html=True)

# Footer section
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
