frutas = {'Platano':1.35, 'Manzana':0.80, 'Pera':0.85, 'Naranja':0.70}
fruta = input('¿Qué fruta desea comprar? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta] * kg )
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")