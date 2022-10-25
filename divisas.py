Divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input('ingrese una divisa')

if divisa.title() in Divisas:
  print("el simbolo es",Divisas[divisa.title()])

else:
  print("la divisa",divisa,"no está")