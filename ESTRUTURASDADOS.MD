Em Python, existem várias estruturas de dados para armazenar, organizar e manipular informações. Vou te mostrar as principais, com exemplos e explicações de quando usar cada uma. 🐍
1. Lista (list)

Uma lista armazena vários elementos em uma única variável. Ela permite elementos duplicados e pode ser modificada depois de criada.

Exemplo:
python

numeros = [1, 2, 3, 4, 5]

print(numeros)
print(numeros[0])  # Primeiro elemento
print(numeros[2])  # Terceiro elemento

Saída:
text

[1, 2, 3, 4, 5]
1
3

Principais operações

Adicionar elementos:
python

numeros.append(6)
print(numeros)
# [1, 2, 3, 4, 5, 6]

Remover elementos:
python

numeros.remove(3)
print(numeros)
# [1, 2, 4, 5, 6]

Acessar elementos pelo índice:
python

print(numeros[0])
# 1

Quando usar: quando você precisa armazenar vários valores, alterar os elementos ou manter uma sequência ordenada.
2. Tupla (tuple)

Uma tupla é parecida com uma lista, mas não permite modificar seus elementos depois de criada.

Exemplo:
python

coordenadas = (10, 20)

print(coordenadas)
print(coordenadas[0])

Saída:
text

(10, 20)
10

Você pode ter elementos duplicados:
python

numeros = (1, 2, 2, 3, 4)

print(numeros)

Porém, não pode alterar um elemento diretamente:
python

numeros = (1, 2, 3)

numeros[0] = 10  # Gera um erro!

Quando usar?

    Para armazenar dados que não devem ser alterados.
    Para representar coordenadas.
    Para representar informações fixas, como dimensões ou datas separadas em valores.

Diferença entre lista e tupla:
python

lista = [1, 2, 3]
tupla = (1, 2, 3)

    list: mutável, ou seja, pode ser modificada.
    tuple: imutável, ou seja, seus elementos não podem ser substituídos ou removidos diretamente.

3. Conjunto (set)

O conjunto é uma estrutura de dados que não mantém elementos duplicados.

É justamente a estrutura que você estava tentando usar para remover duplicatas!

Exemplo:
python

numeros = {1, 2, 3, 4, 5}

print(numeros)

Saída:
text

{1, 2, 3, 4, 5}

Removendo duplicatas de uma lista

Imagine que você tenha:
python

lista = [1, 2, 3, 4, 5, 5, 7, 1]

lista = list(set(lista))

print(lista)

Uma saída possível é:
text

[1, 2, 3, 4, 5, 7]

O que aconteceu?

    set(lista) transformou a lista em um conjunto, eliminando os elementos duplicados.
    list(...) transformou o conjunto novamente em uma lista.

Atenção: o set não garante a ordem dos elementos.
Operações com conjuntos

Uma característica interessante do set é que você pode realizar operações matemáticas entre conjuntos.
python

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

União: reúne todos os elementos dos dois conjuntos.
python

print(a | b)
# {1, 2, 3, 4, 5, 6}

Interseção: mostra os elementos presentes nos dois conjuntos.
python

print(a & b)
# {3, 4}

Diferença: mostra os elementos que estão em a, mas não em b.
python

print(a - b)
# {1, 2}

Quando usar?

    Para eliminar duplicatas.
    Para verificar se um elemento pertence a um conjunto.
    Para comparar grupos de elementos.
    Para realizar operações de união, interseção e diferença.

4. Dicionário (dict)

O dicionário armazena informações no formato de chave e valor.

É muito útil quando você quer associar um nome a uma informação.

Exemplo:
python

pessoa = {
    "nome": "Carlos",
    "idade": 25,
    "cidade": "Florianópolis"
}

print(pessoa["nome"])
print(pessoa["idade"])

Saída:
text

Carlos
25

Nesse exemplo:

    "nome" é uma chave.
    "Carlos" é o valor associado à chave "nome".
    "idade" é outra chave.
    25 é o valor associado à chave "idade".

Adicionando informações
python

pessoa["profissao"] = "Programador"

print(pessoa)

Modificando informações
python

pessoa["idade"] = 26

print(pessoa["idade"])
# 26

Percorrendo um dicionário com for
python

pessoa = {
    "nome": "Carlos",
    "idade": 25,
    "cidade": "Florianópolis"
}

for chave, valor in pessoa.items():
    print(chave, ":", valor)

Saída:
text

nome : Carlos
idade : 25
cidade : Florianópolis

Quando usar?

    Para armazenar informações de pessoas, produtos ou usuários.
    Para representar configurações.
    Para contar a frequência de elementos.
    Para relacionar identificadores a informações.

Exemplo interessante: contando repetições

Você pode usar um dicionário para descobrir quantas vezes cada número aparece em uma lista.
python

lista = [1, 2, 3, 2, 1, 1, 4]

frequencia = {}

for numero in lista:
    if numero in frequencia:
        frequencia[numero] += 1
    else:
        frequencia[numero] = 1

print(frequencia)

Saída:
text

{1: 3, 2: 2, 3: 1, 4: 1}

Isso significa que:

    O número 1 aparece três vezes.
    O número 2 aparece duas vezes.
    O número 3 aparece uma vez.
    O número 4 aparece uma vez.

5. String (str)

A string é uma sequência de caracteres usada para representar textos.

Embora não seja normalmente agrupada com as quatro estruturas de coleção anteriores, ela é um tipo de dado sequencial muito importante em Python.

Exemplo:
python

nome = "Python"

print(nome[0])
print(nome[1])
print(len(nome))

Saída:
text

P
y
6

Você pode percorrer uma string com for:
python

palavra = "Python"

for letra in palavra:
    print(letra)

Saída:
text

P
y
t
h
o
n

Strings são imutáveis: você não pode substituir diretamente um caractere de uma string existente.
python

palavra = "Python"

palavra[0] = "J"  # Gera um erro!

Quando usar?

    Para armazenar nomes.
    Para manipular textos.
    Para processar mensagens.
    Para percorrer letras e caracteres.

6. Array (array)

Um array é uma estrutura que permite armazenar vários valores de um mesmo tipo básico, como números inteiros ou números de ponto flutuante.

Python possui um módulo chamado array para isso.

Exemplo:
python

from array import array

numeros = array('i', [1, 2, 3, 4, 5])

print(numeros)
print(numeros[0])

O 'i' indica que o array armazena números inteiros de um tipo específico.

Você pode adicionar elementos:
python

numeros.append(6)

print(numeros)

Qual é a diferença entre list e array?

Uma lista pode armazenar tipos diferentes:
python

lista = [10, "Python", 3.14, True]

Um array tradicional do módulo array é destinado a valores de um tipo numérico específico.

Quando usar? Quando você precisa armazenar muitos valores numéricos do mesmo tipo e quer uma representação mais compacta do que uma lista convencional pode oferecer.

    Observação: para cálculos numéricos e científicos, a biblioteca NumPy também oferece arrays muito utilizados.

7. frozenset

O frozenset é semelhante ao set, mas é imutável.

Isso significa que você pode realizar operações de conjuntos, mas não pode adicionar ou remover elementos depois de criá-lo.

Exemplo:
python

numeros = frozenset([1, 2, 3, 3, 4])

print(numeros)

Resultado:
text

frozenset({1, 2, 3, 4})

Observe que o número 3 aparece apenas uma vez.

Porém, isto gera um erro:
python

numeros.add(5)

Isso acontece porque o frozenset não permite alterações.
Quando usar?

    Quando você precisa de um conjunto que não possa ser alterado.
    Quando precisa utilizar um conjunto como elemento de outro conjunto ou como chave de um dicionário, desde que seus elementos sejam válidos para isso.

8. Fila (queue)

Uma fila é uma estrutura de dados que normalmente segue o princípio FIFO (First In, First Out): o primeiro elemento que entra é o primeiro que sai.

Imagine uma fila de pessoas esperando atendimento.

Você pode implementar uma fila usando o módulo queue.

Exemplo:
python

from queue import Queue

fila = Queue()

fila.put("Ana")
fila.put("Carlos")
fila.put("Maria")

print(fila.get())
print(fila.get())
print(fila.get())

Saída:
text

Ana
Carlos
Maria

O primeiro elemento inserido foi "Ana", portanto, ela foi a primeira a sair.
Quando usar?

    Para organizar tarefas que precisam ser processadas em ordem.
    Para implementar filas de atendimento.
    Para comunicação entre threads.
    Para processamento de trabalhos em segundo plano.

Observação: para filas simples em programas comuns, também é possível usar uma lista, embora collections.deque seja geralmente mais apropriado quando você precisa adicionar e remover elementos das duas extremidades com eficiência.
9. Pilha (stack)

Uma pilha normalmente segue o princípio LIFO (Last In, First Out): o último elemento que entra é o primeiro que sai.

Imagine uma pilha de pratos: você coloca um prato em cima do outro e retira primeiro o que está no topo.

Em Python, você pode implementar uma pilha usando uma lista.

Exemplo:
python

pilha = []

pilha.append(10)
pilha.append(20)
pilha.append(30)

print(pilha)

print(pilha.pop())
print(pilha.pop())
print(pilha.pop())

Saída:
text

[10, 20, 30]
30
20
10

O último elemento inserido foi 30, portanto, ele foi o primeiro a sair.
Quando usar?

    Para implementar a funcionalidade de desfazer ações.
    Para percorrer estruturas como árvores.
    Para resolver problemas que envolvem retrocesso (backtracking).
    Para controlar operações que precisam ser desfeitas na ordem inversa.

10. Resumo das principais estruturas
Estrutura	Permite duplicatas?	Pode ser modificada?	Mantém ordem?
list	Sim	Sim	Sim
tuple	Sim	Não	Sim
set	Não	Sim	Não garante ordem
dict	As chaves, não	Sim	Sim, pela ordem de inserção
str	Sim	Não	Sim
array	Sim	Sim	Sim
frozenset	Não	Não	Não garante ordem

Observação: no dicionário, os valores podem se repetir, mas as chaves são únicas. Se você inserir uma chave que já existe, o valor associado a ela será atualizado.

Filas e pilhas também são estruturas de dados, mas são classificadas pelo modo como os elementos entram e saem, e não necessariamente por um tipo específico de objeto Python.
11. Qual estrutura você deve aprender primeiro?

Se você está começando a programar em Python, recomendo esta ordem:

    Listas (list): aprenda a adicionar, remover, percorrer e modificar elementos.
    Tuplas (tuple): entenda a diferença entre dados mutáveis e imutáveis.
    Conjuntos (set): pratique a remoção de duplicatas e as operações entre conjuntos.
    Dicionários (dict): aprenda a trabalhar com chaves e valores.
    Strings (str): pratique a manipulação de textos.
    Pilhas e filas: entenda como organizar o processamento de elementos.

Depois, avance para estruturas mais complexas, como listas encadeadas, árvores, heaps e grafos.
🎯 Um desafio para praticar

Considere esta lista:
python

numeros = [1, 2, 3, 2, 4, 5, 1, 6, 3]

Tente resolver três problemas:

    Desafio 1: remova os números duplicados usando set().
    Desafio 2: conte quantas vezes cada número aparece usando um dicionário.
    Desafio 3: crie uma nova lista contendo apenas os números que aparecem uma única vez.

Esses três exercícios vão ajudar você a compreender muito bem a diferença entre list, set e dict.