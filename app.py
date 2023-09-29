from flask import Flask, render_template, request
import openai
app = Flask(__name__)

historial = []

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        pregunta = request.form.get("pregunta")
        resultado = enviar_pregunta(pregunta)
        historial.append(("Yo", pregunta))
        historial.append(("ChatGPT", resultado))
    else:
        resultado=""
    return render_template("index.html", historial=historial)

def enviar_pregunta(pregunta):
    openai.api_key="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" #Definimos la api_key
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
             {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": pregunta}

        ],
    )#Mandamos la peticion a api

    respuesta_texto = respuesta["choices"][0]["message"]["content"]
    return respuesta_texto


if __name__ == '__main__':
    app.run(debug=True, port=5000)
