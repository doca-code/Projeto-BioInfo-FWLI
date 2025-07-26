# Importa a função 'ler_fasta' do módulo 'bio.ler_fasta'
# Essa função é responsável por ler arquivos no formato FASTA
from bio.ler_fasta import ler_fasta
# Importa a classe 'Path' da biblioteca 'pathlib' para manipulação de caminhos de arquivos de forma multiplataforma
from pathlib import Path 

# Define a função principal que executa o "problema 1"
def rodar_problema_1():
  # Define o diretório base como sendo dois níveis acima do arquivo atual (__file__).
  # Isso é útil para garantir que o caminho funcione mesmo que o script seja executado de outro lugar.
  base_dir = Path(__file__).resolve().parent.parent  # volta até a raiz do projeto
  caminho_do_arquivo = base_dir / "arquivos" / "Flaviviridae-genomes.fasta"# Define o caminho do arquivo FASTA, assumindo que está na pasta "arquivos" no diretório base
  organismo_do_fasta = ler_fasta(caminho_do_arquivo) # Lê o conteúdo do arquivo FASTA, retornando uma lista de objetos
  lista_resultados_problema_1 =  [] # Inicia uma lista para armazenar os resultados do problema 1
  # Itera sobre cada organismo presente no arquivo FASTA
  for organismo in organismo_do_fasta:
    seq = organismo.sequencia.upper() # Converte a sequência genética para letras maiúsculas (por segurança, caso existam letras minúsculas) 
    total_len = len(seq) # Calcula o tamanho total da sequência
    total_C_G = seq.count("C") + seq.count("G") # Soma a quantidade de bases C (citosina) e G (guanina)
    
    # Cria um dicionário com os percentuais de cada base (A, T, C, G) e da soma de C+G
    dados_problema_1 = {"nome": organismo.nome,
             "percentual_A": round((seq.count("A") / total_len) * 100, 2),
             "percentual_T": round((seq.count("T") / total_len) * 100, 2),
             "percentual_C": round((seq.count("C") / total_len) * 100, 2),
             "percentual_G": round((seq.count("G") / total_len) * 100, 2),
             "percentual_CG": round((total_C_G / total_len) * 100, 2)}
    
    lista_resultados_problema_1.append(dados_problema_1)  # Adiciona o dicionário de resultados na lista final
  
  return (lista_resultados_problema_1) # Função retorna a lista com os resultados para todos os organismos analisados
