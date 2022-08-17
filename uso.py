from funciones_matematicas import sumar, restar
from estadistica.funciones_estadistica import combinar

resultado = sumar (20, 30)
print(resultado)
combinar(5)

from collections import namedtuple
algo = namedtuple("club", ["color_1","color_2"])
river_plate = algo ("rojo","blanco")
print (river_plate)
print (type (river_plate))