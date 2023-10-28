# CONJUNTOS EM PYTHON
# Você pode criar um conjunto usando chaves {} ou a função set():
# Em Python, os conjuntos (sets) são  estruturas de dados que representam uma coleção de elementos únicos e não ordenados.
# Eles são úteis quando você precisa armazenar elementos sem duplicatas e não se preocupa com a ordem dos elementos.

# Exemplo 01:
conjunto1 = {2,3,4,5,6,5,9}
conjunto2 = {10,7,6,979}
print(conjunto1.difference(conjunto2))

# Exemplo 02:
numeros = set([1, 2, 3, 4, 5]) #lista
frutas = {'maçã', 'banana', 'laranja'} #tupla 
dicionario =  {"key": "chave1", "key2":"chave2" } #dicionário 

# A diferença entre dois conjuntos:
x = {1, 2, 3, 4}
d = {3, 4, 5, 6}

print(x.difference(d))
print(d.difference(x))

# Adicionando elementos: Você pode adicionar elementos a um conjunto usando o método: add():
frutas.add('uva')

# Removendo elementos: Para remover elementos de um conjunto, você pode usar os métodos remove() ou discard(). 
# A diferença é que remove() gera um erro se o elemento não estiver presente, enquanto discard() não gera erro:
frutas.remove('maçã')
frutas.discard('pera')

# Verificando a existência de elementos: Você pode verificar se um elemento está em um conjunto usando o operador in:
if 'banana' in frutas:
    print('Banana está na lista de frutas.')

# Operações de conjuntos: Python suporta várias operações de conjuntos, como união, interseção, diferença, etc., que podem ser úteis ao trabalhar com conjuntos. Por exemplo:
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# União
uniao = conjunto1.union(conjunto2)  # ou conjunto1 | conjunto2

# Interseção
intersecao = conjunto1.intersection(conjunto2)  # ou conjunto1 & conjunto2

# Diferença
diferenca = conjunto1.difference(conjunto2)  # ou conjunto1 - conjunto2

# Iterando em um conjunto: Você pode iterar em um conjunto usando um loop for:
for fruta in frutas:
    print(fruta)

# Tamanho de um conjunto: Para obter o número de elementos em um conjunto, você pode usar a função de comprimento len():
tamanho = len(frutas)

# Exercício 01: Crie um conjunto chamado "frutas" com as seguintes frutas: maçã, banana, laranja, pêra e abacaxi. Em seguida, imprima o número de elementos no conjunto.
frutas = {"maçã", "banana", "laranja","pêra","abacaxi"}
print(len(frutas))

# Exercício 02: Crie dois conjuntos, "conjunto1" e "conjunto2", com alguns números inteiros. Imprima a união desses dois conjuntos
conjunto1 = {0,1,2,3,4,5,6}
conjunto2 = {7,8,9,10,11,12}
uniao = conjunto1.union(conjunto2)  # ou conjunto1 | conjunto2
print(uniao)

# Exercício 03: Dado o conjunto "cores" com cores diferentes, remova a cor "vermelho" do conjunto.
cores = {"azul","branco","verde","vermelho","cinza","branco"}
cores.remove('vermelho')
print(cores)

# Exercício 04: Crie um conjunto chamado "numeros" com os números de 1 a 10. 
numeros = {1,2,3,4,5,6,7,8,9,10}
print(numeros)

# Exercício 05: Verifique se o conjunto "alunos_aprovados" contém todos os alunos do conjunto "todos_alunos". Os conjuntos devem ser definidos com nomes apropriados.
alunos_aprovados = {"Kayh", "kaka", "Lane", "kah"}
todos_alunos =  {"Kayh", "kaka", "Carol", "Maria"}
print(todos_alunos.intersection(alunos_aprovados))
