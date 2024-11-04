# Gerador de Senhas

Este script em Python gera uma senha aleatória com base em critérios especificados, como comprimento e tipos de caracteres.

## Uso

```python
senha = gerador_senhas(12, letras_maiúsculas=True, letras_minúsculas=True, inclusao_digitos=True, inclusao_especiais=True)
```


---

# Função `gerador_senhas`

A função `gerador_senhas` gera uma senha aleatória com base nos critérios especificados.

## Argumentos

- **comprimento_senha** (`int`, opcional): Comprimento da senha. Padrão é 8.
- **letras_maiúsculas** (`bool`, opcional): Incluir letras maiúsculas. Padrão é Verdadeiro.
- **letras_minúsculas** (`bool`, opcional): Incluir letras minúsculas. Padrão é Verdadeiro.
- **inclusao_digitos** (`bool`, opcional): Incluir dígitos. Padrão é Verdadeiro.
- **inclusao_especiais** (`bool`, opcional): Incluir caracteres especiais. Padrão é Verdadeiro.

## Retorno

- `str`: Senha gerada aleatoriamente com base nos critérios especificados.

## Exemplo de Uso

```python
from gerador_senhas import gerador_senhas

senha = gerador_senhas(comprimento_senha=12, letras_maiúsculas=True, letras_minúsculas=True, inclusao_digitos=True, inclusao_especiais=False)
print(senha)  # Exemplo de saída: "AaBbCc123456"
```

