# DICCIONARIOS EN PYTHON

 - Los diccionarios son dats estructurados, es decir, hacer referencia a una colección de datos
 - Son una colección desordenada de pares de datos de la forma **clave:valor**, conocidos como **Elementos** ó **Items**
 - Son **mutables**, una vez definido, se le puede agregar nuevos elementos, modificar o eliminar algunos de los que ya tiene
 - Tambien son conocidos cómo **arreglos asociativos**

## Representación gráfica de un diccionario
![ayo bro chill](diccionario.png 'diccionarios en python')

## Segunda representació gráfica
![XD](chill.png)

## Syntaxis
`diccionario = {clave1:valor1, clave2:valor2, ...}`

 - Cada Item o elemento tiene la forma **clave:valor**
 - En cada Item hay una clave y uno o más valores, si se desconoce el valor, se puede completar con *none*
 - Los elementos del diccionario se indexan por la clave
 - Las claves solo pueden ser **datos inmutables**
 - Los valores pueden ser datos **mutables** ó **inmutables**
 - las claves **NO** pueden repetirse dentro de un diccionario

### Ejemplo:
`frutas = {"manzana":5, "pera":20, "sandia":5000, "banana":6767}`

### Agregar elementos
`diccionario[clave] = valor`
`frutas[cereza] = 300`
 - si la clave ya se encuentra en el diccionario, se reemplaza con el nuevo valor

### Consultar ó modificar elementos
`print("el valor de pera es: " frutas[pera])`

### Eliminar elementos
`del frutas["pera"]`
 - Esto elimina el item cuya clave es "pera"

### Operador de pertenencia
```C#
if cereza in frutas:
    print("sí tenemos cereza para la cena!")
else:
    print("no tenemos cereza para la cena ૮(˶ㅠ︿ㅠ)ა")
```
## Ejersicio:
 - cree un programa en Python que utilice un diccionario para guardar los nombres de sus amigos y sus telefonos, en este caso, el diccionario representa una agenda telefónica, el programa pedirá nombres y telefonos y los irá guardado en el diccioonario (los nombres en mayuscula). además, el programa debe permitir consultar u eliminar un teléfono, incluya un menú de opciones






###### .
![:3](screen.jpg)