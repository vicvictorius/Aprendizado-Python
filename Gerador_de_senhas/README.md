"""
Gera uma senha aleatória com base em critérios especificados.

Args:
    comprimento_senha (int, opcional): Comprimento da senha. Padrão é Verdadeiro.
    letras_maiúsculas (bool, opcional): Incluir letras maiúsculas. Padrão é Verdadeiro.
    letras_minúsculas (bool, opcional): Incluir letras minúsculas. Padrão é Verdadeiro.
    inclusao_digitos (bool, opcional): Incluir dígitos. Padrão é Verdadeiro.
    inclusao_especiais (bool, opcional): Incluir caracteres especiais. Padrão é Verdadeiro.

Returns:
    str: Senha gerada aleatoriamente com base nos critérios especificados.

Exemplos:
    senha = gerador_senhas(12, letras_maiúsculas=True, letras_minúsculas=True, inclusao_digitos=True, inclusao_especiais=True)
"""
