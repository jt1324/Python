import calendar 
from gtts import gTTS


#Calendar
# year = int(input("Enter year: "))
# month = int(input("Enter month: "))

# print("\n", calendar.month(year,month))



#Text to Speech
text_pt = "Acertou misaravi."
text_en = "You got it right."

tts = gTTS(text=text_pt, lang='pt-br')
tts_en = gTTS(text=text_en, lang='en')

tts.save("pt_output.mp3")
tts_en.save("en_output.mp3")

print("Audio saved to pt_output.mp3")
print("Audio saved to en_output.mp3")