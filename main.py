from problemas.problema_1 import rodar_problema_1 # Importa a função que executa o problema 1 (cálculo de percentuais de bases nitrogenadas)
from problemas.problema_2 import rodar_problema_2 # Importa a função que executa o problema 2 (tradução da sequência de DNA para proteínas)
from problemas.problema_3 import rodar_problema_3 # Importa a função que executa o problema 3 (análise de mutação na posição 1000)

resultados_problema_1 = rodar_problema_1() # Executa o problema 1 e armazena o resultado em uma lista de dicionários
relatorio_problema_1 = "Relatório de Percentuais de Bases\n\n" # Inicializa uma string para armazenar o relatório do problema 1

resultados_problema_2 = rodar_problema_2() # Executa o problema 2 e armazena o resultado em uma lista de dicionários
relatorio_problema_2 = "Relatório de Proteínas\n\n" # Inicializa uma string para armazenar o relatório do problema 2

# Gera o relatório com os percentuais de bases para cada organismo
for item in resultados_problema_1:
    relatorio_problema_1 += (f"Organismo: {item['nome']}\n"
                             f"  A: {item['percentual_A']}%\n"
                             f"  T: {item['percentual_T']}%\n"
                             f"  C: {item['percentual_C']}%\n"
                             f"  G: {item['percentual_G']}%\n"
                             f"  CG: {item['percentual_CG']}%\n\n")
print(relatorio_problema_1) # Problema 1: Análise de Composição de Nucleotídeos

# Gera o relatório com a sequência proteica traduzida para cada organismo
for item in resultados_problema_2:
    relatorio_problema_2 += (f"Organismo: {item['nome']}\n"
                             f"  Proteína: {item['sequencia_proteica']}\n\n")
# exibe o relatório de proteínas no terminal
print(relatorio_problema_2)

# exibe o relatório de mutações no terminal
resultados_problema_3 = rodar_problema_3() # Executa o problema 3 (detecção de mutação na posição 1000)
print(resultados_problema_3)
