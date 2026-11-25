#USO DO METODO SET{} PYTHON 
from curses import beep


lista = [1, 2, 3, 4, 5, 5, 7, 1]
lista = list(set(lista))
print(lista)

lista = [1, 2, 3, 4, 5, 5, 7, 1]

#USO DO FOR PRA COMPARAÇÃO DE INDICES
for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] == lista[j]:
            lista[j] = None

lista = list(set(lista))
lista.remove(None)

print(lista)


#O set() cria um conjunto que não permite elementos duplicados.
#Por exemplo:
conjunto = set(lista)
print(conjunto)


pessoa = {
    "nome": "Carlos",
    "idade": 25,
    "cidade": "Florianópolis"
}

for chave, valor in pessoa.items():
    print(chave, ":", valor)
  
    def keyname(chave):
      print(pessoa[chave])

keyname("idade")

