from bio.ler_fasta import ler_fasta
from bio.constantes import DNA_PARA_AMINOACIDO

caminho_do_arquivo = "./arquivos/Flaviviridae-genomes.fasta"
organismo_do_fasta = ler_fasta(caminho_do_arquivo)

for organismo in organismo_do_fasta:
  print(organismo.nome)
  for i in range(0, len(organismo.sequencia), 3):
    codon = organismo.sequencia[i:i+3]

    proteina = DNA_PARA_AMINOACIDO.get(codon, "Codigo invalido ou Stop codon")
    print(codon, ": ", proteina)