
import os
from Crypto.Cipher import AES

# Nome do arquivo criptografado
encrypted_file_name = "teste.txt.wertrow"

# Abrir o arquivo criptografado e ler dados
with open(encrypted_file_name, "rb") as f:
    # O nonce está nos primeiros 8 bytes (tamanho fixo para AES CTR no PyCryptodome)
    nonce = f.read(8)
    encrypted_data = f.read()

# Mesma chave usada para criptografia
key = b"testecom16caract"

# Inicializar AES para descriptografar usando nonce
aes = AES.new(key, AES.MODE_CTR, nonce=nonce)

# Descriptografar dados
decrypted_data = aes.decrypt(encrypted_data)

# Remover arquivo criptografado
os.remove(encrypted_file_name)

# Salvar arquivo descriptografado com nome original
original_file_name = "teste.txt"
with open(original_file_name, "wb") as f:
    f.write(decrypted_data)

print(f"Arquivo '{encrypted_file_name}' descriptografado para '{original_file_name}' com sucesso.")
