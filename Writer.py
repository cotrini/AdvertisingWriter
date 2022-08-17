from typing import Match
import openai
import os


class writer:
    def __init__(self):
        self.name = 'cotrini'
    def gpt3( self, stext, userTemperature, userLength ):
        openai.api_key = os.getenv('API_KEY')
        response = openai.Completion.create(
            engine='text-davinci-002',
            prompt=stext,
            temperature=userTemperature,
            max_tokens=userLength,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        content = response.choices[0].text
        return content


