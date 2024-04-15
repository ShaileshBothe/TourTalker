# import streamlit as st
# import speech_recognition as sr
# import pyttsx3
# from googletrans import Translator
# import openai

# st.set_page_config(page_title="Tour Talker", page_icon=":tada:", layout="wide")

# OPENAI_KEY = "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"
# openai.api_key = OPENAI_KEY

# st.title("Voice Assistant")

# st.write("First Say HELLO")

# def SpeakText(command):
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[2])  
#     engine.setProperty('rate', 180)  
#     engine.say(command)
#     engine.runAndWait()

# def record_text():
#     r = sr.Recognizer()
#     t = Translator()
#     while True:
#         try:
#             with sr.Microphone() as source2:
#                 r.adjust_for_ambient_noise(source2, duration=0.2)
#                 st.write("I'm listening")
#                 audio2 = r.listen(source2)
#                 MyText = r.recognize_google(audio2, language='hi-IN')
#                 translated_text = t.translate(MyText, dest='en')
#                 return translated_text.text
#         except sr.RequestError as e:
#             st.error("Could not request results: {}".format(e))
#         except sr.UnknownValueError:
#             st.error("Unknown error occurred")

# def send_to_chatGBT(messages, text):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages,
#         max_tokens=100,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#     messages.append({"role": "user", "content": text})
#     messages.append({"role": "assistant", "content": response.choices[0].message.content})
#     return response.choices[0].message.content

# messages = [{"role": "user", "content": "You are an expert in traveling in India. I'd like to work as a travel assistant for me to suggest the best path to reach there and tell information about that place and give answers."}]

# while True:
#     text = record_text()
#     response = send_to_chatGBT(messages, text)
#     SpeakText(response)
#     messages.append({"role": "user", "content": text})
#     messages.append({"role": "assistant", "content": response})
#     st.write("User: ", text)
#     st.write("Assistant: ", response)


import streamlit as st
import speech_recognition as sr
import pyttsx3
from mtranslate import translate
import openai

st.set_page_config(page_title="Tour Talker", page_icon=":tada:", layout="wide")

OPENAI_KEY = "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"
openai.api_key = OPENAI_KEY

st.title("Voice Assistant")

st.write("First Say HELLO")

def SpeakText(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2])  
    engine.setProperty('rate', 180)  
    engine.say(command)
    engine.runAndWait()

def record_text():
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                st.write("I'm listening")
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2, language='hi-IN')
                translated_text = translate(MyText, 'en')
                return translated_text
        except sr.RequestError as e:
            st.error("Could not request results: {}".format(e))
        except sr.UnknownValueError:
            st.error("Unknown error occurred")

def send_to_chatGBT(messages, text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    messages.append({"role": "user", "content": text})
    messages.append({"role": "assistant", "content": response.choices[0].message.content})
    return response.choices[0].message.content

messages = [{"role": "user", "content": "You are an expert in traveling in India. I'd like to work as a travel assistant for me to suggest the best path to reach there and tell information about that place and give answers."}]

while True:
    text = record_text()
    response = send_to_chatGBT(messages, text)
    SpeakText(response)
    messages.append({"role": "user", "content": text})
    messages.append({"role": "assistant", "content": response})
    st.write("User: ", text)
    st.write("Assistant: ", response)
