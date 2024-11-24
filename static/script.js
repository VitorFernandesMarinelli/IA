console.log("script.js carregado");
var controle = false;

function enviarLinguagem() {
    const language = document.getElementById('language').value;
    console.log("Função enviarLinguagem chamada com linguagem: " + language);
    fetch('/get_language', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({language: language})
    })
    .then(response => response.json())
    .then(data => {
        console.log("Linguagem selecionada: " + data.language);
        aviso();
    });
}

function aviso(){
    if(controle == false){
        alert("Captura iniciada");
        controle = true;
    }else{
        alert("Captura finalizada");
        controle = false;
    }
}

// Função de long polling para atualizações automáticas
function longPolling(lastTranslation, lastTranscricao) {
    fetch(`/long_polling?last_translation=${lastTranslation}&last_transcricao=${lastTranscricao}`)
    .then(response => response.json())
    .then(data => {
        console.log("Dados recebidos do servidor:", data);  // Adicionado para depuração
        atualizarTexto(data.translation, data.transcricao);
        longPolling(data.translation, data.transcricao);  // Reenvia a requisição imediatamente após receber a resposta
    })
    .catch(error => {
        console.error("Erro na requisição:", error);
        setTimeout(() => longPolling(lastTranslation, lastTranscricao), 5000);  // Tenta novamente após 5 segundos em caso de erro
    });
}

// Função para atualizar os textos no HTML
function atualizarTexto(translation, transcricao) {
    console.log("Atualizando textos:", translation, transcricao);  // Adicionado para depuração
    document.getElementById("translation").innerText = translation;
    document.getElementById("transcricao").innerText = transcricao;
}

// Inicia o long polling quando a página é carregada
window.onload = function() {
    longPolling('', '');  // Envia a primeira requisição com valores vazios
};
