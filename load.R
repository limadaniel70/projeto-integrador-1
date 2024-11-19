#####################################################################
df <- read.csv('ETEPLAP-RESPOSTAS.csv')
#====================================================================
# CARREGAR FATORES
#====================================================================
# Removendo pessoas que nunca utilizaram a biblioteca
df <- subset(df, df[1] != "Nunca.")
for (i in 1:7) {
  df[[i]] <- as.factor(df[[i]])
}
#====================================================================
# PERGUNTAS
#====================================================================
# 1 -> "Com que frequência você utiliza a biblioteca para 
# realizar consultas de disponibilidade de livros?"
#====================================================================
# 2 -> "Como você realiza a consulta de 
# disponibilidade de livros na biblioteca?"
#====================================================================
# 3 -> "Como você se sente em relação à precisão e rapidez
# do sistema atual de consulta manual?"
#====================================================================
# 4 -> "Você já se deparou com inconsistências na disponibilidade
# de livros entre o sistema da biblioteca e o acervo real?"
#====================================================================
# 5 -> "Em sua opinião, qual seria o maior benefício de um sistema
# que permitisse consultar a disponibilidade de livros em tempo real?"
#====================================================================
# 6 -> "Qual a sua preferência de acesso ao sistema de consulta?"
#====================================================================
# 7 -> "Em que medida um sistema automatizado melhoraria
# sua experiência na biblioteca?"
#====================================================================
