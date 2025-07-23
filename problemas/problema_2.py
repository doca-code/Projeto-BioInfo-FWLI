from bio.ler_fasta import ler_fasta
from bio.constantes import DNA_PARA_AMINOACIDO
from bio.constantes import DNA_STOP_CODONS

def rodar_problema_2():
  caminho_do_arquivo = "./Projeto-BioInfo-FWLI/arquivos/Flaviviridae-genomes.fasta"
  organismo_do_fasta = ler_fasta(caminho_do_arquivo)
  resultados_problema_2 = [] 

  for organismo in organismo_do_fasta:
    proteina = []
    seq = organismo.sequencia.upper()

    for i in range(0, len(seq)-2, 3):
      codon = seq[i:i+3]
      if codon in DNA_STOP_CODONS:
        aminoacido ="Stop codon"
      else:
        aminoacido = DNA_PARA_AMINOACIDO.get(codon, "Codigo invalido ou Stop codon")
      
      proteina.append(aminoacido)
    
    dados_problema_2 = {"nome": organismo.nome,
                        "sequencia_proteica": " ".join(proteina)}
    
    resultados_problema_2.append(dados_problema_2) 

  return resultados_problema_2
