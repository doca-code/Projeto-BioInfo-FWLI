from bio.ler_fasta import ler_fasta
from pathlib import Path

def rodar_problema_3():
    base_dir = Path(__file__).resolve().parent.parent  # volta até a raiz do projeto
    caminho_do_arquivo = base_dir / "arquivos" / "Flaviviridae-genomes.fasta"
    organismo_do_fasta = ler_fasta(caminho_do_arquivo)

    # Listas para classificar os organismos conforme o nucleotídeo presente na posição 1000 da sequência
    com_mutacao = [] 
    sem_mutacao = []
    outra_base = []
    
    # Itera por cada organismo do arquivo FASTA
    for organismo in organismo_do_fasta:
        # Verifica qual base está presente na posição 999 (posição 1000, pois o índice começa em 0)
        if organismo.sequencia[999] == "A":
            sem_mutacao.append(organismo.nome)
        elif organismo.sequencia[999] == "G":
            com_mutacao.append(organismo.nome)
        else:
            outra_base.append(organismo.nome)
   
    # Inicializa o relatório como uma string
    relatorio = "Relatório de Mutações\n\n"
    
    # Adiciona ao relatório os organismos com mutação (base G na posição 1000)
    relatorio += f"Organismos com mutação (base G na posição 1000): {len(com_mutacao)}\n"
    for nome in com_mutacao:
        relatorio += nome + "\n"
    relatorio += "\n"
    
    # Adiciona os organismos sem mutação (base A na posição 1000)
    relatorio += f"Organismos sem mutação (base A na posição 1000): {len(sem_mutacao)}\n"
    for nome in sem_mutacao:
        relatorio += nome + "\n"
    relatorio += "\n"
    
    # Adiciona os organismos com alguma outra base (nem A nem G)
    relatorio += f"Organismos com outra base na posição 1000: {len(outra_base)}\n"
    for nome in outra_base:
        relatorio += nome + "\n"
    relatorio += "\n"
    
    # Retorna a string completa com o relatório
    return (relatorio)
