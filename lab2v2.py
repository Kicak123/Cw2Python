'''
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


value = input("Enter your name:")
print(value)'''

'''iks = int(input("podaj x:"))
igrek = int(input("podaj y:"))
if iks < igrek:
     print("X<Y")
elif iks > igrek:
     print("X>Y")
else: print("X=Y")'''

#dlugosc wyrazu
'''
a = ['kot' , 'okno', 'kic']
for x in a:
    print( x, len(x))

for seq in range(10):
    print(seq)

list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
d=len(list(range(10)))
print(d) #to ta 10 na koncu bo ma 10 elementóW
'''
'''
a = ['Pierwszy wyraz', 'Drugi wyraz', 'Trzeci wyraz', 'Czwarty wyraz']
for i in range(len(a)):
    print (i, a[i])
    '''
'''    
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print (n, 'równe', x, '*', n/x)
            break
    else:
        print (n, 'jest liczba pierwsza')

months = ['January', 'February', 'March']
months.append('April')
print(months)

def hello():
    imie = str(input("Enter your name: "))
    if imie:
        print ("Hello " + str(imie))
    else:
        print("Hello World") 
        return 
  
hello()

a = [66.6, 333, 333, 1, 1234.5]
print (a.count(333), a.count(66.6), a.count('x'))
a.insert(2, -1)
a.append(333)
print(a)
a.sort()
print(a)

kolejka = ["Eric", "John", "Michael"]
kolejka.append("Terry") # przybywa Terry
kolejka.append("Graham") # przybywa Graham

print(kolejka.pop(0))

print(kolejka.pop(0))

print(kolejka)

t = [12345, 54321, 'hello!']
print(t[0])

print(t)


u = [t, (1, 2, 3, 4, 5)]
print(u)

tel = {'jack': 4098,'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)

print(tel.keys())
'''