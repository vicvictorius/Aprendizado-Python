#identifica se a variavel ocupa a mesma região de memoria

nome = 'nome'
nome_xereca = nome
saldo, limite = 200, 200

print(nome is nome_xereca)
# >>> True
print(nome is not nome_xereca)
#>>> False
print(saldo is limite)
#>>> True