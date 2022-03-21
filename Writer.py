import openai

def gpt3( stext ):
    openai.api_key = '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'
    response = openai.Completion.create(
        engine='davinci',
        prompt=stext,
            temperature=0.8,
            max_tokens=1000,
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

