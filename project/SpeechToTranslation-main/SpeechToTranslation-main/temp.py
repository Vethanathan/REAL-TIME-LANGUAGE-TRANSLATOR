# import required libraries

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from ibm_watson import SpeechToTextV1, LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import speech_recognition as sr

from gtts import gTTS

import os  

import tkinter
import customtkinter

def gimme_val(a):
    a=a.lower()
    if a=="hindi":
        return "hi"
    elif a=="english":
        return "en"
    elif a=="punjabi":
        return "pa"
    elif a=="tamil":
        return "ta"
    elif a=="telugu":
        return "te"
    elif a=="gujarathi":
        return "gu"
    elif a=="spanish":
        return "es"
    elif a=="chinese":
        return "zh"

def from_lang(a):
    a=a.lower()
    if a=="hindi":
        return "hi-IN_Telephony"
    elif a=="english":
        return "en-IN_Telephony"
    elif a=="chinese":
        return "zh-CN_Telephony"
    elif a=="spanish":
        return "es-LA_Telephony"






def translate(modelid,fromlang,tolang):

    print(modelid,fromlang,tolang)
    ltapikey = 'mBz9Bht8xhElBriNhiK2mfK-HPkPKHI17wU9bQVr6_mx'
    lturl = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/736c2437-d934-4cd4-ad30-e7585dc6b0fd'
    sttapikey = '_2e6jLgrZeRvtEw7MBLFRHwIvUHetcbhHRsw5m2GM-in'
    stturl = 'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/0144428a-cc93-49f8-b57a-ad802cef6d2b'


    ltauthenticator = IAMAuthenticator(ltapikey)
    lt = LanguageTranslatorV3(version='2018-05-01', authenticator=ltauthenticator)
    lt.set_service_url(lturl)


    sttauthenticator = IAMAuthenticator(sttapikey)
    stt = SpeechToTextV1(authenticator=sttauthenticator)
    stt.set_service_url(stturl)


    with open('input1.wav', 'rb') as f:
        res = stt.recognize(audio=f, content_type='audio/wav', model=modelid).get_result()


    voicetext = res['results'][0]['alternatives'][0]['transcript']
    print(voicetext)
    conv = fromlang + "-" + tolang
    # greek = 'en-el'
    # chinese = 'en-zh'
    # hindi = 'en-hi'
    translation = lt.translate(text=voicetext, model_id=conv).get_result()
    translatedtext = translation['translations'][0]['translation']
    print(translatedtext)
    mytext = translatedtext
    entry1.delete(0,"end")
    entry1.insert(0, mytext)    
    





def record():

    # Sampling frequency
    frequency = 44400

    # Recording duration in seconds
    duration = 3.5

    # to record audio from
    # sound-device into a Numpy
    print("recording .......")
    recording = sd.rec(int(duration * frequency),
                    samplerate = frequency, channels = 2)

    # Wait for the audio to complete
    sd.wait()


    write("input1.wav", frequency, recording)

    # using wavio to save the recording in .wav format
    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    wv.write("input2.wav", recording, frequency, sampwidth=4)

    print("done!!!!")
    translate(from_lang(combobox_1.get()),gimme_val(combobox_1.get()),gimme_val(combobox_2.get()))

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x400")
app.title("App")

frame1 = customtkinter.CTkFrame()
frame1.grid()


app_name = customtkinter.CTkLabel(text = "WELCCOME", master=frame1, justify=tkinter.LEFT)

app_name.grid(row=0,column=0)


from_label = customtkinter.CTkLabel(text = "FROM", master=frame1, justify=tkinter.LEFT)

from_label.grid(row=1,column=0)

combobox_1 = customtkinter.CTkComboBox(frame1, values=["english", "hindi", "chineese","spanish",])
combobox_1.grid(row=1,column=1,pady=12, padx=10)



to_label = customtkinter.CTkLabel(text = "FROM", master=frame1, justify=tkinter.LEFT)

to_label.grid(row=2,column=0)


combobox_2 = customtkinter.CTkComboBox(frame1,values=["english","hindi","tamil","telugu","spanish","chinese","gujarathi"])
combobox_2.grid(row=2,column=1,pady=12, padx=10)
# optionmenu_1.set("CTkComboBox")

button_1 = customtkinter.CTkButton(text="record and convert",master=frame1, command=record)
button_1.grid(row=3,column=1)

# button_2 = customtkinter.CTkButton(text="convert",master=frame1, command=translate)
# button_2.grid(row=4,column=1)

# label_info_1 = customtkinter.CTkLabel(master=frame1,text="",height=100,corner_radius=6,fg_color=("white", "gray38"), justify=tkinter.LEFT)
entry1 = customtkinter.CTkEntry(master = frame1)
entry1.grid(row=5,column=1)


app.mainloop()
exit()










language = 'hi'
mytext = convert()

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")



