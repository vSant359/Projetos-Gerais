def salvar_dados_em_txt(nome_arquivo, dados):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("PRONTO PARA RECOLHER\n\n")
        for dado in dados:
            arquivo.write(f"{dado}\n\n")

dados_clientes = [
    "ANTONIO RIGOTTO\n3 Abril, 2025, 09:45 Rio de Janeiro\n\nMARIA LUIZA DE ABRANCHES RIGOTTO Recall\n\n",
    "TOMMASO ENRICO VITO PELLEGRINO\n3 Abril, 2025, 09:45 Rio de Janeiro\n\n"
]

salvar_dados_em_txt("agendamentos.txt", dados_clientes)
