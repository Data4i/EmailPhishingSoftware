import streamlit as st
import pickle

st.set_page_config(page_title='Email Verifier', layout = 'wide', page_icon=':name_badge:')
left_col, center_col, right_col = st.columns((1,2,1))

model_filepath = 'phising_rf_classifier.pkl'

@st.cache_resource
def get_model(filepath):
    with open(filepath, 'rb') as f:
        model = pickle.load(f)
    return model

model = get_model(model_filepath)

with center_col:
    
    st.title("Email Verifier")
    st.text("Input Your Email here")
    email = st.text_input(label= 'email',label_visibility="hidden" ,placeholder='Get $20 Free')
    check_email = st.button("Check")
    
    if check_email:
        prediction = model.predict([email])
        if prediction == 'Phishing Email':
            st.success("Beware Spam", icon="🚨")
        elif prediction == 'Safe Email':
            st.success("Verified", icon="🔥")