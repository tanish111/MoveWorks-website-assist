
import requests
import streamlit as st
from dotenv import load_dotenv
from htmlTemplates import css, bot_template, user_template
headers_1 = {
    'x-api-key': 'sec_TsCNDtPaNF9aLh8NqWf2Kem0Pacrgwb2',
    "Content-Type": "application/json",
}
headers_2 = {
    'x-api-key': 'sec_z4jNucZC94A9AF48ppoS6Myb32BCRf2V',
    "Content-Type": "application/json",
}
responses = []
def handle_userinput_1(user_question):
    message = ""
    content=user_question
    data = {
    'sourceId': "cha_x9KRQiNKOvP7PcQayky8E",
    'messages': [
        {
            'role': 'user',
            'content': content,
        }
    ]}
    response = requests.post('https://api.chatpdf.com/v1/chats/message', headers=headers_2, json=data)
    if response.status_code == 200:
        message = response.json()['content']
        mess_arr = message.split('.')
        count = -1
        for i in mess_arr:
            count=count+1
            if("sorry" or "aplogize" in i.split().lower()):
                del mess_arr[count]
        message = " ".join(mess_arr)
    else:
        print('Status:', response.status_code)
        print('Error:', response.text)
    responses.append(message)
    if(message==""):
        message="Please provide more information"
    conversation = st.session_state.conversation or []  
    conversation.append(user_template.replace("{{MSG}}", user_question))
    st.session_state.conversation = conversation
def handle_userinput_2(user_question):
    message = ""
    content=user_question
    data = {
    'sourceId': "cha_56UP4sLyVC7EwSi7nbm6h",
    'messages': [
        {
            'role': 'user',
            'content': content,
        }
    ]}
    response = requests.post('https://api.chatpdf.com/v1/chats/message', headers=headers_1, json=data)
    if response.status_code == 200:
        message = response.json()['content']
        mess_arr = message.split('.')
        count = -1
        for i in mess_arr:
            count=count+1
            if("sorry" or "aplogize" or "cannot" in i.split().lower()):
                del mess_arr[count]
        message = " ".join(mess_arr)
    else:
        print('Status:', response.status_code)
        print('Error:', response.text)
    message = message + responses[0]
    if(message==""):
        message="Please provide more information"
    conversation = st.session_state.conversation or []  
    conversation.append(bot_template.replace("{{MSG}}", message))
    st.session_state.conversation = conversation
def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = []
    
    st.header("Chat with MoveWorks")
    user_question = st.text_input("Ask a question about your documents:")
    
    if user_question:
        handle_userinput_1(user_question)
        handle_userinput_2(user_question)
    for message in st.session_state.conversation:
        st.write(message, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
