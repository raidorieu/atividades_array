numeros=[0,0,0,0,0,0,0,0,0,0]
a=[numeros]

for x in range(10):
    numeros=int(input("digite um número: "))
    a.append(numeros)

for numeros in a:
    print(a%2!=0)

for numeros in a:
    print(a%2==0)

for numeros in a:
    print(a>0)

for numeros in a:
    print(a<0)

for numeros in a:
    print(a==0)