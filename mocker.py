import csv
import random


PERGUNTAS: dict[str, list[str]] = {
    "Com que frequência você utiliza a biblioteca para realizar consultas de disponibilidade de livros?": [
        "Diariamente.",
        "Semanalmente.",
        "Mensalmente.",
        "Anualmente.",
#        "Nunca.",
    ],
    "Como você realiza a consulta de disponibilidade de livros na biblioteca?": [
        "Manualmente, por consulta direta ao acervo físico.",
        "Através de um sistema digital da biblioteca.",
        "Perguntando diretamente a funcionários.",
    ],
    "Como você se sente em relação à precisão e rapidez do sistema atual de consulta manual?": [
        "Muito satisfeito.",
        "Satisfeito.",
        "Neutro.",
        "Insatisfeito.",
        "Muito insatisfeito.",
    ],
    "Você já se deparou com inconsistências na disponibilidade de livros entre o sistema da biblioteca e o acervo real?": [
        "Sim, frequentemente.",
        "Sim, ocasionalmente.",
        "Não, nunca.",
    ],
    "Em sua opinião, qual seria o maior benefício de um sistema que permitisse consultar a disponibilidade de livros em tempo real?": [
        "Economia de tempo.",
        "Maior precisão nas informações.",
        "Facilidade de acesso a livros.",
        "Não tenho certeza.",
    ],
    "Qual a sua preferência de acesso ao sistema de consulta?": [
        "Aplicativo móvel.",
        "Site acessível por navegador.",
        "Computador específico para consultas na própria biblioteca.",
    ],
    "Em que medida um sistema automatizado melhoraria sua experiência na biblioteca?": [
        "Melhoraria muito.",
        "Melhoraria um pouco.",
        "Não faria diferença.",
        "Pioraria minha experiência.",
    ],
}

N_DE_RESPOSTAS = 28

with open("ETEPLAP-quest.csv", "wt") as quest:
    wt = csv.writer(quest)
    wt.writerow(list(PERGUNTAS.keys()))
    for _ in range(N_DE_RESPOSTAS):
        wt.writerow([random.choice(val) for val in PERGUNTAS.values()])
