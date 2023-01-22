import streamlit as st
from streamlit_chat import message
import requests
import chat
from analysis import analyze
st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
)

st.header("Green World")
st.markdown("[Github](https://github.com/)")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text 


user_input = get_text()
if user_input=="suggest me a best suited crop":
    form = st.form("my_form",clear_on_submit=False)
    n = form.slider('Select the value of Nitrogen Level',
    0, 150)
    p = form.slider('Select the value of Phosphorus Level',
    0, 100)
    k = form.slider('Select the value of Potassium Level',
    0, 100)
    temp = form.slider('Select the value of Temperature Level',
    0.0, 50.0)
    humidity = form.slider('Select the value of Humidity Level',
    0.0, 100.0)
    ph = form.slider('Select the value of PH Level',
    0.0, 10.0)
    rainfall = form.slider('Select the value of Rainfall Level',
    0.0, 200.0)
    submit = form.form_submit_button("Submit")
    if submit:
        st.session_state.past.append("suggest me a best suited crop")
        st.session_state.generated.append("The best crop to grow with these parameters is" + analyze(n,p,k,temp,humidity,ph,rainfall))
    
if user_input:
    print(chat.initialization(user_input))
    st.session_state.past.append(user_input)
    st.session_state.generated.append(chat.initialization(user_input))

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))