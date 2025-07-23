from problemas.problema_1 import rodar_problema_1
from problemas.problema_2 import rodar_problema_2
from problemas.problema_3 import rodar_problema_3

resultados_problema_1 = rodar_problema_1()
relatorio_problema_1 = "Relatório de Percentuais de Bases\n\n"

resultados_problema_2 = rodar_problema_2()
relatorio_problema_2 = "Relatório de Proteínas\n\n"

for item in resultados_problema_1:
    relatorio_problema_1 += (f"Organismo: {item['nome']}\n"
                             f"  A: {item['percentual_A']}%\n"
                             f"  T: {item['percentual_T']}%\n"
                             f"  C: {item['percentual_C']}%\n"
                             f"  G: {item['percentual_G']}%\n"
                             f"  CG: {item['percentual_CG']}%\n\n")
print(relatorio_problema_1)

for item in resultados_problema_2:
    relatorio_problema_2 += (f"Organismo: {item['nome']}\n"
                             f"  Proteína: {item['sequencia_proteica']}\n\n")
print(relatorio_problema_2)

resultados_problema_3 = rodar_problema_3()
print(resultados_problema_3)
