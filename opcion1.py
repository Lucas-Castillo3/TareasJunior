#(EL EJERCICIO PRINCIPAL NO ME PARECIÓ FÁCIL PERO FUE ENTRETENIDO)
#Repetir el ejercicio base, considerando un techo triangular, isóceles.

altura_panel = float(input("Ingrese la altura del panel: "))
ancho_panel = float(input("Ingrese el ancho del panel: "))
altura_techo = float(input("Ingrese la altura del techo: "))
ancho_techo = float(input("Ingrese el ancho del techo: "))

def calcular_paneles(altura_panel, ancho_panel, altura_techo, ancho_techo):
    #cuantos paneles caen considerando la altura del techo
    filas_maximas = int(altura_techo // altura_panel)
    total_paneles = 0
    for i in range( filas_maximas):
        #ancho disponible en la fila i considerando que cada vez es más estrecho de manera lineal
        ancho_disponible = ancho_techo * ((altura_techo - (i * altura_panel)) / altura_techo)
        rectangulos_en_fila = int(ancho_disponible // ancho_panel)
        total_paneles += rectangulos_en_fila
    return int (total_paneles)
if altura_techo >= altura_panel and ancho_techo >= ancho_panel:
    total_paneles = calcular_paneles(altura_panel, ancho_panel, altura_techo, ancho_techo)
else:
    total_paneles = 0
print(f'La cantidad máxima de paneles que caben en el techo es: {total_paneles}')

#para este ejercicio me tarde cerca de 1 hora, fue mucho más complejo que el original, pero me gustó.
