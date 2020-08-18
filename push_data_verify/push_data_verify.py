from sys import argv


arquivo_dos_bytes = argv[1]
with open(arquivo_dos_bytes, "r") as arquivo:
    conteudo = arquivo.readlines()
    arquivo.close()

fim_da_lista = len(conteudo) - 1
print("-=" *  15)
print(f"Temos o total de {fim_da_lista} linhas.")
print("-=" *  15)

lista_de_payloads = []
for posicao  in range(4, fim_da_lista, 5):
    linha = conteudo[posicao].split()
    lista_de_payloads.append(linha)

print(f"Lista de payloads: {lista_de_payloads}\n")

for payload in lista_de_payloads:
    tamanho_paylod = len(payload) - 1
    for indice,byte in enumerate(payload):
        if tamanho_paylod != indice:
            print(f"\\x{byte}", end="")
        else:
            print("\n")
