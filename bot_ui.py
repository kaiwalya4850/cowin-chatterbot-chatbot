import streamlit as st
from chatterbot import ChatBot
import chatterbot
import spacy 
import warnings
from PIL import Image
import pandas as pd
warnings.filterwarnings('ignore')
spacy.load('en_core_web_sm')

df = pd.read_csv("India.csv")
#df = df.rename(columns={'date':'index'}).set_index('index')


def get_text():
    input_text = st.text_input("User: ","Hello, I am COWIN Bot, how may I help you?")
    return input_text
    

st.title('COWIN Bot')
st.write('This bot will help users to information on the number of vaccines available in districts across India.'
           ' It will also answer all the vaccine related FAQs')

st.write('')
image = Image.open('intro_img.jpg')

st.image(image, caption='COWIN Bot', use_column_width=True)


#st.line_chart(df["total_vaccinations"])
st.line_chart(df["people_vaccinated"])
st.line_chart(df["people_fully_vaccinated"])


bot = ChatBot(
    'Example Bot',
    logic_adapters=[
        {
            'import_path': 'adapter_cowin1.MyLogicAdapter'
        }

    ]
)

user_input = get_text()
if True:
    try:
        st.text_area("Bot:", value=bot.get_response(user_input), height=200, max_chars=None, key=None)
    except UnboundLocalError:
        print("Please enter correct response, didn't understand you")
else:
    st.text_area("Bot:", value="Please start the bot by clicking sidebar button", height=200, max_chars=None, key=None)