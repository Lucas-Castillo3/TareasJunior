#🛠️ Problema
'''El problema a resolver consiste en encontrar la máxima cantidad de rectángulos de dimensiones “a” y “b” (paneles solares) 
que caben dentro de un rectángulo de dimensiones “x” e “y” (techo), 
según se muestra en la siguiente figura:'''

# Pedir al usuario las dimensiones del techo y de los paneles solares
height_panel = float(input("ingresa el alto del panel: "))
width_panel = float(input("ingresa el ancho del panel: "))
height_roof = float(input("ingresa el alto del techo: "))
width_roof = float(input("ingresa el ancho del techo: "))

#Función para calcular la cantidad de paneles que caben en el techo
def calculate_panels (height_panel, width_panel, height_roof, width_roof):
    # Calcular la cantidad de paneles que caben en el techo sin rotar de manera vertical
    total_panels_v = (height_roof / height_panel) * (width_roof / width_panel)
    # Calcular la cantidad de paneles que caben en el techo rotando de manera horizontal
    total_panels_h = (height_roof / width_panel) * (width_roof / height_panel)
    # Devolver el máximo entre las dos configuraciones1
    return int(max(total_panels_v, total_panels_h))

#Si un lado del techo es menor a un lado del panel entonces no caben paneles
if (height_roof >= height_panel and width_roof >= width_panel) or (height_roof >= width_panel and width_roof >= height_panel):
    total_panels = calculate_panels(height_panel, width_panel, height_roof, width_roof)
else:
    total_panels = 0
print(f'La cantidad máxima de paneles que caben en el techo es: {total_panels}')