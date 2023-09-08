from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from spacy.cli import download

download("en_core_web_sm")

class ENGSM:s
    ISO_639_1 = 'en_core_web_sm' 

chatbot = ChatBot("ChatClass", tagger_language=ENGSM)

treinamento = [
    "Quais são as materias do segundo semestre?",
    "No segundo semestre é ensinado Engenharia de Software I, Resolução de Problemas I, Análise de Sistemas de Informação I, Sistemas Operacionais, Algoritmos e Programação de Computadores II e Metodologia do Trabalho Científico",
    "Quais são os códigos dessas disciplinas?",
    "Preciso que você seja específico em qual disciplina quer saber",
    "Quero saber o código de Engenharia de Software I",
    "O código dessa matéria é ST266",
    "Quantos créditos possui a disciplina ST266",
    "Possui 2 créditos",
    "Qual é o pré-requisito da disciplina ST266?",
    "O pré-requisito dessa disciplina é Algoritmos e Programação de Computadores I",
    "Quero saber o código de Resolução de Problemas I",
    "O código dessa matéria é SI202",
    "Quantos créditos possui a disciplina SI202?",
    "Possui 4 créditos",
    "Qual é o pré-requisito da disciplina SI202?",
    "O pré-requisito dessa disciplina é Algoritmos e Programação de Computadores I",
    "Quero saber o código de Análise de Sistemas de Informação I",
    "O código dessa matéria é SI305",
    "Quantos créditos possui a disciplina SI305?",
    "Possui 4 créditos",
    "Qual é o pré-requisito da disciplina SI305?",
    "O pré-requisito dessa disciplina é Algoritmos e Programação de Computadores I",
    "Quero saber o código de Sistemas Operacionais",
    "O código dessa matéria é TT304",
    "Quantos créditos possui a disciplina TT304?",
    "Possui 4 créditos",
    "Qual é o pré-requisito da disciplina TT304?",
    "O pré-requisito dessa disciplina é Organização e Arquitetura de Computadores",
    "Quero saber o código de Algoritmos e Programação de Computadores II",
    "O código dessa matéria é SI203",
    "Quantos créditos possui a disciplina SI203?",
    "Possui 2 créditos",
    "Qual é o pré-requisito da disciplina SI203?",
    "O pré-requisito dessa disciplina é Algoritmos e Programação de Computadores I",
    "Quero saber o código de Metodologia do Trabalho Científico",
    "O código dessa matéria é ST008",
    "Quantos créditos possui a disciplina ST008?",
    "Possui 2 créditos"
    "Qual é o pré-requisito da disciplina ST008?",
    "Essa matéria não possui pré-requisitos",
    
    
    
]

trainer = ListTrainer(chatbot)
trainer.train(treinamento)

while True:
    mensagem = input("Mande uma mensagem para o ChatBot:")
    if mensagem == "parar":
            break
    resposta = chatbot.get_response(mensagem)
    print(resposta)
