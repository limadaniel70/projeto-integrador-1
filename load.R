df <- read.csv('ETEPLAP-quest.csv')
#====================================================================
# PERGUNTA 1
#====================================================================
# USUARIOS QUE UTILIZAM A BIBLIOTECA
total_pessoas <- nrow(df)
df <- subset(df, df[1] != "Nunca.")
total_usuarios <- nrow(df)
#====================================================================
# PERGUNTA 2
#====================================================================
# BIBLIOTECAS QUE USAM UM SISTEMA MANUAL
bibliotecas_manuais <- sum(df[2] != "Através de um sistema digital dabiblioteca.")
bibliotecas_automaticas <- total_usuarios - bibliotecas_manuais
#====================================================================
# PERGUNTA 3
#====================================================================
# USUARIOS INSATISFEITOS
insatisfeitos <- sum(df[3] == "Insatisfeito." | df[3] == "Muito insatisfeito.")
outros <- nrow(df) - insatisfeitos
#====================================================================
# PERGUNTA 4
#====================================================================
# PESSOAS QUE ENCONTRARAM UM INCONSISTENCIA NO ACERVO
acharam_inconsistencia <- sum(df[4] != "Não, nunca.")
sem_inconsistencia <- total_usuarios - acharam_inconsistencia
#====================================================================
# PERGUNTA 5
#====================================================================
# VANTAGEM DE UM SISTEMA AUTOMATIZADO

