# IA de tradução
 
Este foi um projeto desenvolvido para a disciplina de Inteligência Artificial, onde tínhamos que criar um sistema que utilizasse alguma forma de IA. Nossa equipe decidiu desenvolver um sistema de tradução, que pegasse o áudio dito em algum idioma e o traduzisse para português e para libras.

Devido ao pouco tempo para o desenvolvimento, várias coisas poderiam ser melhoradas e não seguimos as melhores práticas, então pedimos que relevem esses fatos

# Tecnologias usadas

Optamos pelo uso da linguagem Python para a IA e para subir o servidor, HTML e CSS para o visual e JavaScript para dar funcionalidade ao HTML.

Usamos o Flask para criar um servidor local, o SpeechRecognition para capturar o áudio do microfone e gerar uma transcrição, a API do Google para a tradução para o português e a API VLibras do governo brasileiro para a tradução para LIBRAS.

# Avisos

Esse projeto foi feito com fins de demonstração do uso de IA, autorizamos o uso e alterações deste projeto por qualquer um, só pedimos que coloquem os créditos.

A tradução nunca é perfeita, por favor cheque a tradução por meios confiáveis.

O sistema de LIBRAS está parcialmente desenvolvido, sendo preciso a interação humana para gerar a tradução.

# Como funciona

O SpeechRecognition captura o áudio do microfone e gera uma transcrição no idioma original, a transcrição é passada para a API do Google, que realiza a tradução para o português. A transcrição e a tradução são enviadas para o servidor, que coloca os textos na página.

# Como utilizar

1º Após baixar os arquivos, faça a instalação dos módulos python:
    → pip install flask
    → pip install requests
    → pip install googletrans
    → pip install SpeechRecognition

2º Execute o arquivo "teste.py" para iniciar o servidor Flask;

3º Execute o "testeIdioma.py" para iniciar a IA;

4º Abra um navegador e entre no endereço: http://127.0.0.1:5000;

5º Com o site aberto, selecione o idioma que será falado e clique em iniciar para começar e fale no idioma;

6º Clique no mesmo botão para parar a captura;

7º Para ativar as libras, clique no botão com símbolo de mão, e depois clique no texto traduzido.

# Bugs localizados e ainda não corrigidos

Ao parar uma captura e tentar realizar uma nova captura sem reiniciar o servidor, pode ocorrer a geração de um texto com palavras randômicas.

# Possiveis melhorias

1º Melhor organização do código;
2º Otimização;
3º Correção de bugs;
4º Tornar mais rápido a transcrição do texto;
5º Gerar libras de forma automática;
6º Posicionar as libras na área designada.