meses_validos=('enero', 'febrero', 'marzo', 'abril','mayo', 'junio', 'julio', 'agosto', 'septiembre','octubre', 'noviembre','diciembre')

mes=int(input('Ingrese un número de mes (del 1 al 12): '))
if mes in range(1,13):
    print(f'El mes seleccionado es {meses_validos[mes-1]}')
else: 
    print('Debe ingresar números de 1 a 12')