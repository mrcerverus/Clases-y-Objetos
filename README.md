# Clases-y-Objetos
Desafío - Creación de clases y objetos
En este desafío validaremos nuestros conocimientos de clases, atributos, objetos y métodos.
Lee todo el documento antes de comenzar el desarrollo individual o grupal, para asegurarte
de tener el máximo de puntaje y enfocar bien los esfuerzos.
Descripción
En un emprendimiento dedicado a venta de té de hoja artesanal, se puede comprar té de
distintos sabores (té negro, té verde, e infusión de hierbas) y en 2 formatos (300 gr y 500 gr).
Cada tipo de té tiene, además, un tiempo de preparación (en minutos) y una recomendación
de consumo (se explica en un pequeño texto). Todos los té tienen un tiempo de duración de
1 año o 365 días.
Los 3 sabores de té se pueden comprar en cualquiera de los 2 formatos, teniendo el formato
de 300gr un valor de $3.000 y el de 500gr un valor de $5.000. El té negro tiene un tiempo de
preparación de 3 minutos, el té verde de 5 minutos y el agua de hierbas de 6 minutos. El té
negro se recomienda consumir al desayuno, mientras que el té verde al medio día, y el agua
de hierbas al atardecer.
Utilizando Python y las características de la Programación Orientada a Objetos, se solicita en
primera instancia generar un programa que permita obtener el tiempo de preparación,
recomendación y precio, según el sabor y el formato entregado por el usuario, para así obtener
los datos necesarios para generar un pedido.
_ 2
www.desafiolatam.com
Requerimientos
1. Crear en un archivo llamado te.py una clase que permita instanciar objetos de tipo
“Te”. Para ello, debe considerar un nombre adecuado para la clase, y el o los atributos
de clase. Recuerde que un atributo de clase es aquel que se define a nivel de clase, y
que todas las instancias tendrán el mismo valor.
(1 Punto)
2. En el archivo te.py y en la clase del requerimiento anterior, agregue un método
estático que retorne el tiempo de preparación y la recomendación correspondiente,
según el sabor ingresado por parámetro. Debe retornar el tiempo y recomendación
correspondiente, según la descripción del problema.
(2 Puntos)
Considere el parámetro sabor como un número entero, con los siguientes 3 posibles
valores:
a. 1: Corresponde a Té negro
b. 2: Corresponde a Té verde
c. 3: Corresponde a Agua de hierbas.
3. En el archivo te.py y en la clase del primer requerimiento, agregue un método estático
que retorne el precio según el formato ingresado por parámetro (número entero). Debe
retornar el precio adecuado según la descripción del problema.
(2 Puntos)
4. En un archivo llamado instancias.py, importe la clase del primer requerimiento.
(2 Puntos)
A partir de esta clase:
a. Cree dos instancias
b. Almacene el tipo de dato de cada instancia creada en una variable (Tip: Use la
función type()).
c. Muestre por pantalla, usando print(), el valor de cada tipo de dato
almacenado.
d. En caso de que ambos tipos almacenados sean iguales, muestre por pantalla,
usando print(), el mensaje “Ambos objetos son del mismo tipo”. En caso
contrario, mostrar mensaje “Los objetos no son del mismo tipo”.
_ 3
www.desafiolatam.com
5. En un archivo llamado pedido.py, escriba un programa que al ser ejecutado permita
al usuario ingresar los datos para generar un pedido de té. Para ello, el programa debe
pedir al usuario ingresar el valor que desea para cada atributo requerido para
especificar su pedido. Los valores entregados por el usuario deben almacenarse en
variables, y luego estas variables se deben utilizar en los métodos de la clase del
requerimiento 1 (debe importarla en este script), para obtener el resto de valores
necesarios para un pedido. Una vez ingresada la información requerida, se debe
mostrar en pantalla, mediante print, el detalle de toda la información del té ordenado,
a partir de los valores ingresados por el usuario, y los obtenidos a partir de los métodos
de la clase del requerimiento 1.
(3 Puntos)
Por tanto, debe mostrar en pantalla los valores de:
a. Sabor del tipo de té (como texto)
b. Formato (como número)
c. Precio (como número)
d. Tiempo (como número)
e. Recomendación (como texto)

¡Mucho éxito!
Consideraciones y recomendaciones
● NOTA 1: Considerar que no todos los valores de los atributos son “definidos por el
usuario”; Debe considerar qué se le debe consultar al usuario, y qué se debe asignar
desde el lado del programa, considerando la información entregada en la
descripción (considere que la recomendación de uso está predefinida).
● NOTA 2: Asuma que el usuario ingresará siempre un valor dentro de los permitidos
(no es necesario hacer validaciones).
● Tip: Puede asignar un número a cada sabor en la información mostrada al usuario,
y pedir al usuario ingresar el número correspondiente al sabor que desea. Y luego
en su programa hacer la transformación al sabor correspondiente.