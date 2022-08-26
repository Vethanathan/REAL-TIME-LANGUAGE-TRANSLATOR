from PIL import Image, ImageTk
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from ibm_watson import SpeechToTextV1, LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import speech_recognition as sr
import datetime
from gtts import gTTS
import os  
import tkinter
import customtkinter

def change_mode(switch_2):
        if switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")


def load_image(path, image_size):
        """ load rectangular image with path relative to PATH """
        return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))
        
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
    elif a=="german":
        return "de"
    elif a=="korean":
        return "ko"
    elif a=="italian":
        return "it"
    elif a=="arabic":
        return "ar"
    elif a=="dutch":
        return "nl"
    elif a=="portuguese":
    	return "pt"
    	
     

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
    elif a=="german":
        return "de-DE_Telephony"
    elif a=="french":
        return "fr-FR_Telephony"
    elif a=="italian":
        return "it-IT_Telephony"
    elif a=="korean":
        return "ko-KR_Telephony"
    elif a=="portuguese":
        return "pt-BR_Telephony"
    elif a=="arabic":
        return "nl-NL_Telephony"
    elif a=="dutch":
    	return "nl-NL_Telephony"
    



def speech_to_text_eng(modelid,fromlang):
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
    conv = fromlang + "-" + 'en'
    # greek = 'en-el'
    # chinese = 'en-zh'
    # hindi = 'en-hi'
    translation = lt.translate(text=voicetext, model_id=conv).get_result()
    translatedtext = translation['translations'][0]['translation']
    return translatedtext
    #return voicetext




def translate(modelid,fromlang,tolang,t):
    fromlang='en'
    '''ltapikey = 'mBz9Bht8xhElBriNhiK2mfK-HPkPKHI17wU9bQVr6_mx'
    lturl = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/736c2437-d934-4cd4-ad30-e7585dc6b0fd'
    sttapikey = '_2e6jLgrZeRvtEw7MBLFRHwIvUHetcbhHRsw5m2GM-in'
    stturl = 'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/0144428a-cc93-49f8-b57a-ad802cef6d2b'
    '''
    
    #ltapikey = 'mBz9Bht8xhElBriNhiK2mfK-HPkPKHI17wU9bQVr6_mx'
    ltapikey="WP-Cu2-4bwJL0H5qC8TqGg3xs5xCv6-XCdjDn7C3bdX4"
    #lturl = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/736c2437-d934-4cd4-ad30-e7585dc6b0fd'
    lturl = "https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/6e7ddecd-dea1-43c3-abd4-79c9a77aef1b"
    sttapikey = '_2e6jLgrZeRvtEw7MBLFRHwIvUHetcbhHRsw5m2GM-in'
    stturl = 'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/0144428a-cc93-49f8-b57a-ad802cef6d2b'
    '''
    ltapikey = 'mBz9Bht8xhElBriNhiK2mfK-HPkPKHI17wU9bQVr6_mx'
    lturl = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/736c2437-d934-4cd4-ad30-e7585dc6b0fd'
    sttapikey = '_2e6jLgrZeRvtEw7MBLFRHwIvUHetcbhHRsw5m2GM-in'
    stturl = 'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/0144428a-cc93-49f8-b57a-ad802cef6d2b'
    '''



    ltauthenticator = IAMAuthenticator(ltapikey)
    lt = LanguageTranslatorV3(version='2018-05-01', authenticator=ltauthenticator)
    lt.set_service_url(lturl)


    sttauthenticator = IAMAuthenticator(sttapikey)
    stt = SpeechToTextV1(authenticator=sttauthenticator)
    stt.set_service_url(stturl)
    
    print(modelid,fromlang,tolang)
    
    conv = fromlang + "-" + tolang
    # greek = 'en-el'
    # chinese = 'en-zh'
    # hindi = 'en-hi'
    translation = lt.translate(text=t, model_id=conv).get_result()
    translatedtext = translation['translations'][0]['translation']
    #print(translatedtext)
    x = str(datetime.datetime.now())
    with open("database/"+x+"(text).txt","a") as file:file.write(translatedtext)
    
    mytext = translatedtext
    entry1.delete(0,"end")
    entry1.insert(0, mytext)    
    


def login():
	print("azhuthiten")
	u=entry_username.get()
	p=entry_password.get()
	print(u,p)
	if u=="admin" and p=="pwd":
		frame2.grid_forget()
		frame1.grid()
	


def record():

    frequency = 44400

    duration = 10

    print("recording .......")
    recording = sd.rec(int(duration * frequency),
                    samplerate = frequency, channels = 2)

    sd.wait()

    x = str(datetime.datetime.now())
    write("input1.wav", frequency, recording)

    wv.write("database/"+x+"(voice).wav", recording, frequency, sampwidth=4)

    print("done!!!!")
    print(from_lang(combobox_1.get()),gimme_val(combobox_1.get()))
    t = speech_to_text_eng(from_lang(combobox_1.get()),gimme_val(combobox_1.get()))
    if gimme_val(combobox_2.get()) == 'en':
        print(t)
        f1 = open("database/"+x+"(text).txt","a")
        f1.write(t)
        f1.close()
        mytext = t
        entry1.delete(0,"end")
        entry1.insert(0, mytext)
    else:
        print("en-IN_Telephony",'en',gimme_val(combobox_2.get()))
        print(t)
        translate("en-IN_Telephony",'en',gimme_val(combobox_2.get()),t)

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue")  
PATH = os.path.dirname(os.path.realpath(__file__))



app = customtkinter.CTk()

app.geometry("304x280")
app.title("App")

frame1 = customtkinter.CTkFrame(width=100,height=100)
#frame1.grid()
frame2 = customtkinter.CTkFrame(width=100,height=100)
switch_2 = customtkinter.CTkSwitch(master=frame2,text="Dark Mode",command=lambda :change_mode(switch_2))
switch_2.grid(row=10,column=0)
frame2.grid()
login_name = customtkinter.CTkLabel(text = "LOGIN", master=frame2, justify=tkinter.LEFT)
user_name = customtkinter.CTkLabel(text = "USERNAME", master=frame2, justify=tkinter.LEFT)
password = customtkinter.CTkLabel(text = "PASSWORD", master=frame2, justify=tkinter.LEFT)
entry_username = customtkinter.CTkEntry(master = frame2)
entry_password = customtkinter.CTkEntry(master = frame2)

login_name.grid(row=0,column=1)
user_name.grid(row=1,column=0)
password.grid(row=2,column=0)
entry_username.grid(row=1,column=1)
entry_password.grid(row=2,column=1)
button_9 = customtkinter.CTkButton(master=frame2, text="LOGIN", width=130, height=60, border_width=2,
corner_radius=10, compound="bottom", border_color="#D35B58", fg_color=("gray84", "gray25"),hover_color="#C77C78", command=login)
button_9.grid(row=3,column=1)

app_name = customtkinter.CTkLabel(text = "WELCOME", master=frame1, justify=tkinter.LEFT)

app_name.grid(row=0,column=0)


from_label = customtkinter.CTkLabel(text = "FROM", master=frame1, justify=tkinter.LEFT)

from_label.grid(row=1,column=0)



combobox_1 = customtkinter.CTkComboBox(frame1, values=["english", "hindi", "chinese","spanish","german","french","italian","korean","portuguese","dutch","arabic"])
combobox_1.grid(row=1,column=1,pady=12, padx=10)



to_label = customtkinter.CTkLabel(text = "TO", master=frame1, justify=tkinter.LEFT)

to_label.grid(row=2,column=0)


combobox_2=customtkinter.CTkComboBox(frame1,values=["english","hindi","tamil","telugu","spanish","chinese","gujarathi","portuguese","arabic","german","korean","french","italian"])
combobox_2.grid(row=2,column=1,pady=12, padx=10)
# optionmenu_1.set("CTkComboBox")
add_user_image = load_image("/test_images/mike.png", 50)

to_label = customtkinter.CTkLabel(text = "CLICK HERE TO RECORD", master=frame1, justify=tkinter.LEFT)
to_label.grid(row=5,column=0)

button_1 = customtkinter.CTkButton(master=frame1, image=add_user_image, text="", width=130, height=60, border_width=2,
corner_radius=10, compound="bottom", border_color="#D35B58", fg_color=("gray84", "gray25"),hover_color="#C77C78", command=record)
#button_1 = customtkinter.CTkButton(text="record and convert",master=frame1, command=record)

to_label = customtkinter.CTkLabel(text = "", master=frame1, justify=tkinter.LEFT)
to_label.grid(row=3,column=1)
to_label.grid(row=4,column=1)

button_1.grid(row=5,column=1)

# button_2 = customtkinter.CTkButton(text="convert",master=frame1, command=translate)
# button_2.grid(row=4,column=1)
to_label = customtkinter.CTkLabel(text = "", master=frame1, justify=tkinter.LEFT)
to_label.grid(row=6,column=1)
# label_info_1 = customtkinter.CTkLabel(master=frame1,text="",height=100,corner_radius=6,fg_color=("white", "gray38"), justify=tkinter.LEFT)
entry1 = customtkinter.CTkEntry(master = frame1)
entry1.grid(row=7,column=1)

language = gimme_val(combobox_2.get())
mytext = entry1.get()


myobj = gTTS(text=mytext, lang=gimme_val(combobox_2.get(), slow=False)

myobj.save("welcome.mp3")
app.mainloop()
#exit()














