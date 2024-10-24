tupla1 = ()
print(tupla1)

tupla2 =("una cadena ", 123,4.9,True)
print(tupla2)
print(tupla2[1])
print(tupla2[3])

tupla3 = (0,1,2,3)
tupla4 = ("A","B","C","D")
tupla5 =(tupla3,tupla4)

print(tupla5)
print( tupla5[1][3])
print( tupla5[0][0])

#operaciones
tupla6 = ("A","B","C","D")
tupla7 = (1,2,3,4,5)
tupla8 = tupla6 + tupla7
print(tupla8)
print(tupla8[5])


#epeticion
tupla9 = (1,2,3,4,5)
tupla10 = tupla9*3
print(tupla10)


tupla11 =("ROJAS")
tupla12 =(123)
tupla13 = ("Rosas")
tupla14 = ("rosas")

print((tupla11,tupla12) < (tupla13,tupla14))

#listas
lista = []
print(lista)
lista1 = [1,2,3,4,5,"hola",4.5]
print(lista1)

lista2 = [0,1,2,3]
lista3 = ["A","B","C"]
lista4 = [lista2,lista3]
print(lista4)
print(lista4[1][1])