from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from spacy.cli import download

download("en_core_web_sm")

class ENGSM:s
    ISO_639_1 = 'en_core_web_sm' 

chatbot = ChatBot("ChatClass", tagger_language=ENGSM)

treinamento = [
    "Olá, Boa noite",
    "Boa noite. Como posso te ajudar hoje?",
    "Gostaria de saber sobre as disciplinas do meu curso",
    "Me informe qual é o seu curso",
    "Sou aluno de TADS",
    "Atualmente o curso de TADS possui 30 disciplinas obrigatórias",
    "Quais são as materias do terceiro semestre?"
    "No terceiro semestre é ensinado Geometria Analítica e Álgebra Linear, Programação Orientada a Objetos I, Engenharia de Software II, Introdução a Interfaces Humano-Computador e Banco de Dados I",
    "Quais são os códigos dessas disciplinas?",
    "Preciso que você seja específico em qual disciplina quer saber",
    "Quero saber o código de Geometria Analítica e Álgebra Linear",
    "O código dessa matéria é EB102 (6 créditos)",
    "Quero saber o código de Programação Orientada a Objetos I",
    "O código dessa matéria é SI300 (4 créditos)",
    "Quero saber o código de Engenharia de Software II",
    "O código dessa matéria é SI304 (4 créditos)",
    "Quero saber o código de Introdução a Interfaces Humano-Computador",
    "O código dessa matéria é SI404 (2 créditos)",
    "Quero saber o código de Banco de Dados I",
    "O código dessa matéria é ST567 (4 créditos)",
    "Qual é o pré-requisito da disciplina EB102?",
    "Essa matéria não tem pré requsitos.",
    "Qual é o pré-requisito da disciplina SI300?",
    "Um pré requisito é a matéria Algoritmos e Programação de Computadores I (SI100)",
    "Qual é o pré-requisito da disciplina SI304?",
    "Os pré requisitos para essa matéria são Algoritmos e Programação de Computadores I (SI100) e Engenharia de Software I (ST266)",
    "Qual é o pré-requisito da disciplina SI404?",
    "Os pré requisitos para essa matéria são Algoritmos e Programação de Computadores I (SI100) e Engenharia de Software I (ST266)",
    "Qual é o pré-requisito da disciplina ST567?",
    "Um pré requisito é a matéria Algoritmos e Programação de Computadores I (SI100)",
    "O que eu faço caso pegue DP em alguma matéria?",
    "Você pode adiantar matérias que não tem como pré requisito essa matéria que você pegou DP e assim que possuivel fazer a matéria novamente para poder avançar no curso."
]

trainer = ListTrainer(chatbot)
trainer.train(treinamento)

while True:
    mensagem = input("Mande uma mensagem para o ChatBot:")
    if mensagem == "parar":
            break
    resposta = chatbot.get_response(mensagem)
    print(resposta)
