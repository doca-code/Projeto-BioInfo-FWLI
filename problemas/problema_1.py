from bio.ler_fasta import ler_fasta

caminho_do_arquivo = "./arquivos/Flaviviridae-genomes.fasta"
organismo_do_fasta = ler_fasta(caminho_do_arquivo)

for organismo in organismo_do_fasta:
  total_C_G = organismo.sequencia.count("C") + organismo.sequencia.count("G")
  print(organismo.nome)
  print("Percentual de A: ", round((organismo.sequencia.count("A")/organismo.sequencia.calcular_tamanho()*100),2),"%")
  print("Percentual de T: ", round((organismo.sequencia.count("T")/organismo.sequencia.calcular_tamanho()*100),2),"%")
  print("Percentual de C: ", round((organismo.sequencia.count("C")/organismo.sequencia.calcular_tamanho()*100),2),"%")
  print("Percentual de G: ", round((organismo.sequencia.count("G")/organismo.sequencia.calcular_tamanho()*100),2),"%")
  print("Percentual C+G = ", round((total_C_G/organismo.sequencia.calcular_tamanho()*100),2),"%")



