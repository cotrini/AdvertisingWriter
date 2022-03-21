import openai
import os

def gpt3( stext ):
    openai.api_key = os.getenv('API_KEY')
    response = openai.Completion.create(
        engine='davinci',
        prompt=stext,
            temperature=0.8,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
    )
    content = response.choices[0].text.split('.')
    print(content)
    return response.choices[0].text

query = 'this is a script about a personal thinks about sport and force'
response = gpt3(query)
print(response)


