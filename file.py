from gtts import gTTS
import os

f=open('file.txt')
x=f.read()
language='en'

audio=gTTS(text=x,lang=language,slow=False)

audio.save('file.wav')
os.system('file.wav')