# import required libraries

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from ibm_watson import SpeechToTextV1, LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import speech_recognition as sr

from gtts import gTTS

import os   




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




# Sampling frequency
frequency = 44400

# Recording duration in seconds
duration = 6


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

# en-AU_NarrowbandModel
#hi-IN_Telephony
with open('input1.wav', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/wav', model='en-AU_NarrowbandModel').get_result()


voicetext = res['results'][0]['alternatives'][0]['transcript']
print(voicetext)




greek = 'en-el'
chinese = 'en-zh'
hindi = 'en-pa'


translation = lt.translate(text=voicetext, model_id=hindi).get_result()
translatedtext = translation['translations'][0]['translation']
print(translatedtext)


mytext = translatedtext

language = 'hi'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")



