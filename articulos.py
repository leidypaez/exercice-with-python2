cesta = {}
continuar = True
while continuar:
    item = input('Introduce un artículo: ')
    precio = float(input('Introduce el precio de ' + item + ': '))
    cesta[item] = precio
    continuar = input('¿Quieres añadir este artículos a la lista (Si/No)? ') == "Si"
costo = 0
print('Lista de la compra')
for item, precio in cesta.items():
    print(item, '\t', precio)
    costo += precio
print('Costo total: ', costo)