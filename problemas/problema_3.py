from bio.ler_fasta import ler_fasta
from pathlib import Path

def rodar_problema_3():
    base_dir = Path(__file__).resolve().parent.parent  # volta até a raiz do projeto
    caminho_do_arquivo = base_dir / "arquivos" / "Flaviviridae-genomes.fasta"
    organismo_do_fasta = ler_fasta(caminho_do_arquivo)

    com_mutacao = []
    sem_mutacao = []
    outra_base = []
    
    for organismo in organismo_do_fasta:
        if organismo.sequencia[999] == "A":
            sem_mutacao.append(organismo.nome)
        elif organismo.sequencia[999] == "G":
            com_mutacao.append(organismo.nome)
        else:
            outra_base.append(organismo.nome)
   
    relatorio = "Relatório de Mutações\n\n"
    
    relatorio += f"Organismos com mutação (base G na posição 1000): {len(com_mutacao)}\n"
    for nome in com_mutacao:
        relatorio += nome + "\n"
    relatorio += "\n"
    
    relatorio += f"Organismos sem mutação (base A na posição 1000): {len(sem_mutacao)}\n"
    for nome in sem_mutacao:
        relatorio += nome + "\n"
    relatorio += "\n"
    
    relatorio += f"Organismos com outra base na posição 1000: {len(outra_base)}\n"
    for nome in outra_base:
        relatorio += nome + "\n"
    relatorio += "\n"
    
    return (relatorio)
