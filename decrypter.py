import os
import pyaes

## abrir o arquivo criptografado
dir_path = os.path.dirname(os.path.realpath(__file__))
file_name = dir_path + "\\alvo.txt.rsw996"
file = open(file_name, "rb")
file_data = file.read()
file.close()

arquivo_sec = "key.sec"
file_sec = open(arquivo_sec,"rb")

## chave para descriptografia
key = file_sec.readline()
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo descriptografado
new_file = "alvo.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
