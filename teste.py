from flask import Flask, render_template, request, jsonify
import time
from testeIdioma import alternar_captura_processamento

app = Flask(__name__)

# Variáveis para armazenar o texto
translation_text = "Texto de Tradução"
transcricao_text = "Texto de Transcrição"

@app.route('/')
def index():
    return render_template('index.html', translation=translation_text, transcricao=transcricao_text)

@app.route('/get_language', methods=['POST'])
def get_language():
    language = request.form['language']
    print(f"Linguagem selecionada: {language}")
    alternar_captura_processamento(language)
    return jsonify(status="success", language=language)

@app.route('/atualizar_textos', methods=['POST'])
def atualizar_textos():
    global translation_text, transcricao_text
    data = request.get_json()
    translation_text = data.get('translation')
    transcricao_text = data.get('transcricao')
    print(f"Recebido translation: {translation_text}, transcricao: {transcricao_text}")
    return jsonify(status='success')

@app.route('/long_polling')
def long_polling():
    last_translation = request.args.get('last_translation', '')
    last_transcricao = request.args.get('last_transcricao', '')

    # Checa se os textos mudaram, se não, mantém a conexão aberta por um tempo
    for _ in range(30):  # Espera por no máximo 30 segundos
        if translation_text != last_translation or transcricao_text != last_transcricao:
            return jsonify(translation=translation_text, transcricao=transcricao_text)
        time.sleep(1)
    
    return jsonify(translation=translation_text, transcricao=transcricao_text)

if __name__ == '__main__':
    app.run(debug=True)
