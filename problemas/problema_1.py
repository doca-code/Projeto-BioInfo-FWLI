from bio.ler_fasta import ler_fasta
from pathlib import Path

def rodar_problema_1():
  base_dir = Path(__file__).resolve().parent.parent  # volta até a raiz do projeto
  caminho_do_arquivo = base_dir / "arquivos" / "Flaviviridae-genomes.fasta"
  #caminho_do_arquivo = "./Projeto-BioInfo-FWLI/arquivos/Flaviviridae-genomes.fasta"
  organismo_do_fasta = ler_fasta(caminho_do_arquivo)
  lista_resultados_problema_1 =  [] 

  for organismo in organismo_do_fasta:
    seq = organismo.sequencia.upper()  
    total_len = len(seq)
    total_C_G = seq.count("C") + seq.count("G")
    
    dados_problema_1 = {"nome": organismo.nome,
             "percentual_A": round((seq.count("A") / total_len) * 100, 2),
             "percentual_T": round((seq.count("T") / total_len) * 100, 2),
             "percentual_C": round((seq.count("C") / total_len) * 100, 2),
             "percentual_G": round((seq.count("G") / total_len) * 100, 2),
             "percentual_CG": round((total_C_G / total_len) * 100, 2)}
    
    lista_resultados_problema_1.append(dados_problema_1)  
  
  return (lista_resultados_problema_1)
