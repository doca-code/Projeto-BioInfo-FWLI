from bio.ler_fasta import ler_fasta # Importa a função que lê arquivos no formato FASTA
from bio.constantes import DNA_PARA_AMINOACIDO # Importa o dicionário que faz a conversão de códons DNA para aminoácidos
from bio.constantes import DNA_STOP_CODONS # Importa a lista de códons que sinalizam parada da tradução
from pathlib import Path # Importa a biblioteca para lidar com caminhos de forma multiplataforma

# Função principal que executa o "problema 2"
def rodar_problema_2():
  base_dir = Path(__file__).resolve().parent.parent  # volta até a raiz do projeto
  caminho_do_arquivo = base_dir / "arquivos" / "Flaviviridae-genomes.fasta"
  organismo_do_fasta = ler_fasta(caminho_do_arquivo)
  resultados_problema_2 = [] 

  # Itera sobre cada organismo presente no arquivo FASTA
  for organismo in organismo_do_fasta:
    proteina = [] # Lista para armazenar os aminoácidos da proteína traduzida
    seq = organismo.sequencia.upper() # Garante que a sequência esteja em maiúsculas

    # Itera sobre a sequência de DNA, de 3 em 3 nucleotídeos (códons)
    for i in range(0, len(seq)-2, 3): # len(seq)-2 garante que não sobre um codon incompleto
      codon = seq[i:i+3] # Extrai o códon atual (trinca de nucleotídeos)
      # Verifica se é um stop codon
      if codon in DNA_STOP_CODONS:
        aminoacido ="Stop codon"
      else:
        # Usa o dicionário para traduzir o códon para aminoácido
        # Se o códon for inválido, retorna "Código inválido"
        aminoacido = DNA_PARA_AMINOACIDO.get(codon, "Codigo invalido")
      
      proteina.append(aminoacido) # Adiciona o aminoácido à lista da proteína
    
    # Cria um dicionário com o nome do organismo e sua sequência proteica traduzida
    dados_problema_2 = {"nome": organismo.nome,
                        "sequencia_proteica": " ".join(proteina)}
    
    resultados_problema_2.append(dados_problema_2)   # Adiciona os dados ao resultado final

  return resultados_problema_2  # Retorna todos os resultados
