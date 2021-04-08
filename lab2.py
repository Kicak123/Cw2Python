# pierwszy poradnik 
print ("Hello World")
paliwo = 8.5 * (67*0.1 + 124*0.15 + 11.7*0.2)
autostrada = 124*0.17
prom = 50
koszt = paliwo + autostrada + prom
print (koszt)
print (koszt / 5)

lista = [1,2,3,4,"napis", True, False, 8.5, 11]

slownik = {"jablecznik" : "ciasto z jablek", "czy lubisz jablecznik" : True}

d=[10, 8, 10, 12, 6, 8, 7, 12, 10, 16, 16, 9, 14, 9, 11, 17, 18, 9]

print (d[0])

print (d[4:75])

#drugi poradnik z oficjalnej strony

a=1.5+0.5j
print(a)
print(a.real)
abs(a)
print(abs(a))

slowo = 'Pomoc' + 'ABC'
print(slowo)
print(slowo[2:5])
print('123' + slowo[0:])

lista1 = ['ser','jajka','maslo','pomidor']
print(lista1)
print(lista1[1:3])
print(len(lista1))

q= [2,3]
p=[1,2,q]
print(p,len(p))
lista2=['bułka','laptop','maslo',lista1]
print(lista2)


#value = input("Enter your name:")

#print(value)

iks = int(input("podaj x:"))
igrek = int(input("podaj y:"))
if iks < igrek:
     print("X<Y")
elif iks > igrek:
     print("X>Y")
else: print("X=Y")
