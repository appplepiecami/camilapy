print('--------CAMIPY--------')

numero = int(input('Ingrese algo:'))
print(f'Ud. ingresó el número: {numero}')

frutas = ["banana", "fresa", "kiwi"]

if numero == 1:
    print('GANASTES')
else:
    print('PERDISTE')

if numero <= 100:
    for i in range(numero):
        print(f'{i+1}-Besistos')
else:
    print("no soy un loco😛")

print('-----------------')
for fruta in frutas:
    print(f'Mi fruta es: {fruta}')


print('--------FIN--------')
