nome = "vik"
idade = 18
profissao = "putao"
linguagem = "xerecascript"
saldo = 45.435

dados = {"nome": "vik", "idade": 18}

print("nome: %s idade: %d % (nome,idade)")

print("nome: {} idade: {}".format(nome, idade))

print("nome: {0} idade: {1}".format(nome, idade))
print("nome: {0} {0} {0} idade: {1}".format(nome, idade))


print("Nome: {nome} idade: {idade} {idade} {idade}".format(nome=nome, idade=idade))
print("Nome: {name} idade: {age} {age} {age}".format(name=nome, age=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} idade: {idade}") #Prefiro esse, mais clean
print(f"Nome: {nome} idade: {idade} Saldo: {saldo:10.2f}") #10.2f é a quantidade de casa deciamais, depois doi ponto é 2 casas, e antes são 10 casas, por isso fica espaços em branco no lado esquerdo
print(f"Nome: {nome} idade: {idade} Saldo: {saldo:.2f}")