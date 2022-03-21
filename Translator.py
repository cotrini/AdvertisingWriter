from urllib import response
from googletrans import Translator
from Writer import writer

translator = Translator()
openWriter = writer()
userText = input("Describe tu texto lo mejor posible: ")
userText = translator.translate(userText, dest='en').text
script = openWriter.gpt3( userText )
translated = translator.translate(script, src='en', dest='es')
print(translated.text)  