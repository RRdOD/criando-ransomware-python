# Projeto Ransomware em Python

Este projeto consiste em um ransomware simples desenvolvido em Python, que criptografa e descriptografa arquivos utilizando o algoritmo AES no modo CTR. O objetivo é demonstrar o funcionamento básico de um ataque ransomware, semelhante ao famoso WannaCry.

---

## Estrutura do Projeto

- `encriptter.py` — Script responsável por criptografar o arquivo alvo.
- `decriptter.py` — Script responsável por descriptografar o arquivo criptografado.
- `teste.txt` — Arquivo de exemplo utilizado para testes.

---

## Como Funciona

1. O script de criptografia (`encriptter.py`) abre o arquivo original (`teste.txt`), lê seu conteúdo e o criptografa usando AES com uma chave de 16 caracteres.
2. Após a criptografia, o arquivo original é removido e um novo arquivo criptografado é criado (`teste.txt.wertrow`).
3. O script de descriptografia (`decriptter.py`) faz o processo inverso: abre o arquivo criptografado, usa a mesma chave para descriptografar e reconstroi o arquivo original legível.
4. Sem a chave correta, não é possível recuperar o conteúdo do arquivo.

---

## Requisitos

- Python 3.x
- Biblioteca `pycryptodome`

Você pode instalar a biblioteca necessária com:

```bash
pip install pycryptodome
