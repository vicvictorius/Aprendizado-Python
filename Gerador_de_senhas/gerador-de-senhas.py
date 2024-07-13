import random
import string

def gerador_senhas (comprimento_senha=True, letras_maiúsculas=True, letras_minúsculas=True, inclusao_digitos=True, inclusao_especiais=True):
    caracteres = ''
    if letras_minúsculas:
        caracteres += string.ascii_uppercase
    if letras_maiúsculas:
        caracteres += string.ascii_lowercase
    if inclusao_digitos:
        caracteres += string.digits
    if inclusao_especiais:
        caracteres += string.punctuation

    senha = "".join(random.choice(caracteres) for _ in range(comprimento_senha))
    return senha

#Exemplo de uso
while True:
    try:
        comprimento_senha = int(input("Digite o comprimento da senha desejada: "))
        break  # Se a conversão for bem-sucedida, sai do loop
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

senha = gerador_senhas(comprimento_senha)
print(f'Sua senha gerada é: {senha}')