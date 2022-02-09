# .append("") --> para agregar un elemento al final de la lista
# .extend("", "")--> para agregar varios elementos al final de la lista
# .insert(posición, "nuevo elemento")
import array as arr
array_example = arr.array("i", [1, 3, 4, 8, 9])
array_example_one = arr.array('i', [7, 5, 0, 1, 6, 7])
# -----
print(array_example)
print(type(array_example))

print('primer valor', array_example[0])

array_example.insert(2, 10)
print(array_example)

array_example[0] = 12
print(array_example)
# Concatenar arreglos
print(array_example_one + array_example)
# Eliminar .pop()--> eliminar el último valor, pop(i) -->posicion
print("valor eliminado", array_example.pop())
print('despues del pop', array_example)
