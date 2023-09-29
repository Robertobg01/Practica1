import openai

openai.api_key="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"
respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role":"user",
            "content": "hola quien eres"
            }
        ],
        stream =True
    )
for token in respuesta:
    print(token["choices"][0]["delta"]["content"], end="")