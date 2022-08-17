from urllib import response
from googletrans import Translator
from Writer import writer

def textGenerator(text, userTemperature, userLength):
    translator = Translator()
    openWriter = writer()
    userText = text
    userText = translator.translate(userText, dest='en').text
    script = openWriter.gpt3( userText, userTemperature, userLength )
    translated = translator.translate(script, src='en', dest='es')
    return translated.text  