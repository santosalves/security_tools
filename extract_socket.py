# Info
mensagem = "Ferramenta para analisar bytes de rede e extrair informacoes como SOCKET(IP + PORTA) e FLAGS ativas na comunicacao"
print("-+" * len(mensagem))

# Pegando o nome do arquivo
caminho_do_arquivo = str(input("Digite o caminho do arquivo (ex: /ubuntu/hexa_bytes.txt): ")).strip()
print(caminho_do_arquivo)

# Variaveis de controle
bytes = []
contador = 0
ip_origem = ""
ip_destino = ""
porta_origem = ""
porta_destino = ""
elementos = 0

with open(caminho_do_arquivo, "r" ) as arquivo:
    # Transformando cada linha do arquivo em uma lista
    conteudo = arquivo.readlines()
    
    arquivo.close()

# Pegando cada lista que forma uma string e transformando cada elemento em um item da nova lista
for qtd_itens in range(len(conteudo)):
    bytes += conteudo[qtd_itens].split()
print(f"Numero de bytes: {len(bytes)}") 

# Separando corretamente os IPs/Portas
for byte in bytes:
    contador += 1
    if (contador >= 27) and (contador < 31):
        if contador != 30:
            ip_origem += str(int(byte, 16)) + "."
        else:
            ip_origem += str(int(byte, 16))
    
    elif (contador >= 31) and (contador < 35):
        if contador != 34:
            ip_destino += str(int(byte, 16)) + "."
        else:
            ip_destino += str(int(byte, 16))
   
    elif (contador >= 35) and (contador < 37):
        porta_origem += str(byte)
        if contador == 36:
            porta_origem = str(int(porta_origem, 16))

    elif (contador >= 37) and (contador < 39):
        porta_destino += str(byte)
        if contador == 38:    
            porta_destino = str(int(porta_destino, 16))
            elementos += contador
           
            # Apresentacao do Socket
            print("-=" * 20)
            print(f"Socket de origem: {ip_origem}:{porta_origem}")
            print(f"Socket de destino: {ip_destino}:{porta_destino}")

            # Resetando os valores para comecar o proximo bloco
            contador = 0
            ip_origem = ""
            ip_destino = ""
            porta_origem = ""
            porta_destino = ""

            
    elif elementos == len(bytes):
        break
