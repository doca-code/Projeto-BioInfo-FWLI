from bio.ler_fasta import ler_fasta
from bio.constantes import DNA_PARA_AMINOACIDO
from bio.constantes import DNA_STOP_CODONS
from pathlib import Path

def rodar_problema_2():
  base_dir = Path(__file__).resolve().parent.parent  # volta até a raiz do projeto
  caminho_do_arquivo = base_dir / "arquivos" / "Flaviviridae-genomes.fasta"
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
        aminoacido = DNA_PARA_AMINOACIDO.get(codon, "Codigo invalido")
      
      proteina.append(aminoacido)
    
    dados_problema_2 = {"nome": organismo.nome,
                        "sequencia_proteica": " ".join(proteina)}
    
    resultados_problema_2.append(dados_problema_2) 

  return resultados_problema_2
