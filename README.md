El problema nos habla de paneles de dimensiones "a" y "b" que deben colocarse en un techo de dimensiones "x" e "y"

Lo primero que se hace es pedir las dimensiones al Usuario.
Luego comprobar que estas dimensiones tengan sentido, es decir que el ancho y alto del techo sean mayores o igual al alto y ancho de los paneles,
es decir que si tengo paneles de 2x2 y el techo es de 1x10, no debe caer ningún panel, porque si bien el área es mayor, el alto del techo es menor que ambos lados del panel.
Es por esto que puse una condición if.
De cumplirse la condición se hace la llamada a la funcion "calculate_panels" (todo mi codigo está en inglés por esta función xd) en esta función primero calculo cuantos paneles
caen considerando los lados como float, en caso de que me de 7.5 por ejemplo.

Luego retorno y muestro solo el valor entero.


Hice la opción 1 y me constó bastante más, cerca de una hora, me demoré en el papel y luego los resultados del codigo eran distintos a los que calculé en papel,
finalmente encontré mi error y fue en la linea de codigo en la que calculo el ancho disponible, ya que olvidé que i comienza en 0 y que las divisiones no se aproximan.
Ahora, está bien o mi logica y codigos están equivocados.
