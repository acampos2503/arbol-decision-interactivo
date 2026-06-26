# diseno orientado a objetos

## proyecto

**arbol de decision interactivo**

## descripcion general

Este proyecto consiste en una aplicacion grafica desarrollada en Python con Tkinter. La aplicacion funciona como un juego de preguntas y respuestas llamado **adivina en que estoy pensando**.

El programa utiliza un arbol binario de decision para hacer preguntas de **si** o **no**. Segun las respuestas del usuario, el programa recorre el arbol hasta llegar a una posible respuesta final.

El tema principal del proyecto es **paises**, pero tambien se incluyen otros archivos json con diferentes categorias, como animales, comidas, deportes y personajes.

Si el programa falla al adivinar, el usuario puede agregar una nueva respuesta y una nueva pregunta. Con eso, el arbol se actualiza y guarda automaticamente el nuevo conocimiento.

## archivos principales

El proyecto se organiza en tres archivos principales:

- `main.py`
- `arbol_decision.py`
- `interfaz.py`

Tambien se usa la carpeta `data`, donde se guardan los archivos json del arbol.

## main.py

El archivo `main.py` es el archivo principal del programa.

Su responsabilidad es importar la interfaz grafica, crear el objeto principal de la aplicacion e iniciar el programa.

Este archivo no contiene la logica del arbol ni la logica de la interfaz. Solo se usa como punto de entrada del proyecto.

## arbol_decision.py

El archivo `arbol_decision.py` contiene la parte logica del proyecto.

En este archivo se manejan los nodos, el recorrido del arbol, el aprendizaje, la carga de archivos json y el guardado automatico.

## clase Nodo

La clase `Nodo` representa cada elemento del arbol de decision.

Un nodo puede ser una pregunta o una respuesta final.

Por ejemplo, un nodo de pregunta puede ser:

```text
¿Esta en America?
```

Un nodo de respuesta puede ser:

```text
Costa Rica
```

### atributos principales

- `tipo`: indica si el nodo es una pregunta o una respuesta.
- `texto`: guarda el texto del nodo.
- `si`: guarda la rama que se sigue cuando el usuario responde si.
- `no`: guarda la rama que se sigue cuando el usuario responde no.

### metodos principales

- `es_respuesta()`: revisa si el nodo actual es una respuesta final.
- `convertir_a_diccionario()`: convierte el nodo en un diccionario para poder guardarlo en json.

### responsabilidad de la clase

La responsabilidad de la clase `Nodo` es guardar la informacion de cada parte del arbol.

Esta clase permite representar preguntas, respuestas y las conexiones entre los nodos.

## funcion crear_nodo_desde_diccionario

La funcion `crear_nodo_desde_diccionario()` permite reconstruir el arbol a partir de un archivo json.

Esta funcion lee los datos del archivo y va creando objetos de la clase `Nodo`.

Si el nodo es una respuesta, crea un nodo sin ramas.

Si el nodo es una pregunta, crea el nodo y tambien crea sus ramas de si y no.

Esta funcion tambien ayuda a validar que el archivo tenga el formato correcto.

## clase ArbolDecision

La clase `ArbolDecision` controla el funcionamiento principal del arbol.

Esta clase se encarga de cargar el arbol, recorrerlo, reiniciar la partida, aprender nuevas respuestas y guardar los cambios.

### atributos principales

- `archivo`: guarda la ruta del archivo json que se esta usando.
- `raiz`: representa el primer nodo del arbol.
- `actual`: representa el nodo donde esta ubicada la partida en ese momento.
- `ultimo_error`: guarda el ultimo mensaje de error relacionado con archivos.

### metodos principales

- `crear_arbol_por_defecto()`: crea un arbol basico si no se puede cargar un archivo.
- `reiniciar()`: vuelve al inicio del arbol.
- `obtener_texto_actual()`: devuelve la pregunta o respuesta actual.
- `nodo_actual_es_respuesta()`: revisa si el nodo actual es una respuesta final.
- `responder(respuesta)`: avanza por la rama si o no.
- `aprender(respuesta_correcta, nueva_pregunta, respuesta_correcta_es_si)`: agrega una nueva pregunta y respuesta al arbol.
- `guardar_arbol()`: guarda el arbol actualizado en un archivo json.
- `cargar_arbol()`: carga el arbol desde un archivo json.
- `cambiar_archivo(nuevo_archivo)`: cambia el archivo json usado por el programa.

### responsabilidad de la clase

La responsabilidad de la clase `ArbolDecision` es manejar toda la logica del arbol.

Esta clase no se encarga de mostrar ventanas ni botones. Solo se encarga de controlar como funciona el arbol internamente.

## interfaz.py

El archivo `interfaz.py` contiene la interfaz grafica del programa.

Esta interfaz fue creada usando Tkinter.

## clase InterfazJuego

La clase `InterfazJuego` controla todo lo que el usuario ve en pantalla.

Esta clase se encarga de mostrar la ventana principal, los botones, las preguntas, los mensajes y el formulario que aparece cuando el programa debe aprender una nueva respuesta.

### atributos principales

- `ventana`: representa la ventana principal de Tkinter.
- `arbol`: representa el objeto de la clase `ArbolDecision` que se usa para jugar.

### metodos principales

- `iniciar()`: muestra la pantalla inicial y mantiene abierta la ventana.
- `limpiar_ventana()`: borra los elementos actuales de la pantalla.
- `mostrar_inicio()`: muestra el menu principal.
- `cargar_archivo()`: permite seleccionar un archivo json.
- `iniciar_partida()`: inicia una nueva partida desde la raiz del arbol.
- `mostrar_nodo_actual()`: muestra la pregunta o respuesta actual.
- `responder(respuesta)`: envia la respuesta del usuario al arbol.
- `mostrar_gano()`: muestra el mensaje cuando el programa adivina correctamente.
- `mostrar_aprendizaje()`: muestra el formulario para agregar nueva informacion.
- `guardar_aprendizaje()`: valida los datos y manda la informacion al arbol.
- `mostrar_aprendido()`: muestra el mensaje cuando el arbol se actualiza.

### responsabilidad de la clase

La responsabilidad de la clase `InterfazJuego` es manejar la interaccion con el usuario.

La interfaz no contiene toda la logica del arbol. Para avanzar, aprender, guardar o cargar, utiliza los metodos de la clase `ArbolDecision`.

## relacion entre clases

El programa usa una relacion sencilla entre clases.

La clase `InterfazJuego` tiene un objeto de la clase `ArbolDecision`.

La clase `ArbolDecision` usa objetos de la clase `Nodo`.

La relacion se puede representar asi:

```text
InterfazJuego
      usa
ArbolDecision
      usa
Nodo
```

Esto permite separar responsabilidades.

La interfaz se encarga de mostrar la parte visual.

El arbol se encarga de manejar la logica.

Los nodos guardan las preguntas y respuestas.

## representacion del arbol

El arbol se representa con objetos de la clase `Nodo`.

Cada nodo tiene un texto y un tipo.

Si el nodo es de tipo `pregunta`, tiene dos ramas:

- `si`
- `no`

Si el nodo es de tipo `respuesta`, no tiene ramas y funciona como una hoja del arbol.

Ejemplo:

```text
¿Esta en America?
si -> Costa Rica
no -> España
```

En los archivos json, el arbol se guarda con la misma idea.

Cada nodo tiene:

- `tipo`
- `texto`

Y si es pregunta, tambien tiene:

- `si`
- `no`

## recorrido del arbol

El recorrido inicia en la raiz del arbol.

Cuando el usuario responde **si**, el programa avanza por la rama `si`.

Cuando el usuario responde **no**, el programa avanza por la rama `no`.

Este proceso se repite hasta llegar a un nodo de tipo respuesta.

Cuando se llega a una respuesta final, el programa pregunta si esa era la respuesta pensada por el usuario.

## aprendizaje del arbol

El aprendizaje ocurre cuando el programa falla al adivinar.

En ese caso, el programa pide tres datos:

- la respuesta correcta
- una pregunta que diferencie la respuesta correcta de la incorrecta
- si para la respuesta correcta la contestacion seria si o no

Luego, el programa reemplaza la respuesta incorrecta por una nueva pregunta.

Esa nueva pregunta queda con dos ramas:

- una rama hacia la nueva respuesta correcta
- una rama hacia la respuesta incorrecta anterior

La posicion de cada respuesta depende de si para la nueva respuesta la contestacion era si o no.

## guardado del arbol

El arbol se guarda en archivos json dentro de la carpeta `data`.

Para guardar el arbol, cada nodo se convierte en un diccionario.

Luego, el programa usa `json.dump()` para escribir la informacion en el archivo.

El guardado se realiza automaticamente despues de que el programa aprende una nueva respuesta.

Esto permite que el conocimiento nuevo no se pierda cuando el programa se cierra.

## carga del arbol

El programa puede cargar un arbol desde un archivo json.

Para cargarlo, el programa abre el archivo, lee los datos y reconstruye el arbol creando objetos de la clase `Nodo`.

Si el archivo no existe, esta vacio o tiene errores, el programa crea un arbol basico por defecto.

Tambien se muestra un mensaje para indicar que hubo un problema al cargar el archivo.

## validaciones

El programa valida que el usuario no deje campos vacios cuando se agrega informacion nueva.

Tambien valida que el usuario seleccione si o no antes de guardar el aprendizaje.

En el manejo de archivos, el programa valida que el archivo pueda leerse y que tenga una estructura correcta para reconstruir el arbol.

## archivos json incluidos

El proyecto incluye cinco archivos json de ejemplo:

- `paises.json`
- `animales.json`
- `comidas.json`
- `deportes.json`
- `personajes.json`

El archivo principal del programa es `paises.json`.

Los otros archivos se pueden cargar desde la interfaz grafica.

## conclusion

El proyecto utiliza programacion orientada a objetos de forma sencilla.

Se usan pocas clases, pero cada una tiene una responsabilidad clara.

La clase `Nodo` representa los elementos del arbol.

La clase `ArbolDecision` controla la logica del juego.

La clase `InterfazJuego` controla la interfaz grafica.

Esta organizacion permite cumplir con el uso de arbol binario, interfaz grafica, manejo de archivos y separacion de responsabilidades.