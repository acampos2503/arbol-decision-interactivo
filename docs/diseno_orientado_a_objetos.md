# Diseño orientado a objetos

## Descripción general

Este proyecto consiste en una aplicación gráfica desarrollada en Python. El programa utiliza un árbol binario de decisión para intentar adivinar un país pensado por el usuario.

El usuario responde preguntas de Sí o No. Según cada respuesta, el programa avanza por el árbol hasta llegar a una posible respuesta final. Si el programa falla, el usuario puede enseñarle una nueva pregunta y una nueva respuesta.

## Archivos principales del proyecto

El proyecto se organiza en tres archivos principales:

* `main.py`
* `arbol_decision.py`
* `interfaz.py`

También se utiliza la carpeta `data` para guardar los archivos JSON con los árboles de decisión.

## Clase Nodo

La clase `Nodo` representa cada elemento del árbol de decisión.

Un nodo puede representar una pregunta o una respuesta final.

### Atributos principales

* `texto`: guarda la pregunta o la respuesta del nodo.
* `si`: representa el camino que se sigue cuando el usuario responde Sí.
* `no`: representa el camino que se sigue cuando el usuario responde No.

### Responsabilidad

La responsabilidad de esta clase es guardar la información de cada nodo del árbol.

## Clase ArbolDecision

La clase `ArbolDecision` controla la lógica principal del juego.

### Atributos principales

* `raiz`: representa el primer nodo del árbol.
* `actual`: representa el nodo en el que se encuentra la partida actual.
* `archivo`: guarda la ruta del archivo que se está utilizando.

### Métodos principales

* `reiniciar()`: vuelve al inicio del árbol.
* `obtener_texto_actual()`: devuelve la pregunta o respuesta actual.
* `es_respuesta()`: indica si el nodo actual es una respuesta final.
* `responder_si()`: avanza por la rama Sí.
* `responder_no()`: avanza por la rama No.
* `aprender()`: agrega una nueva pregunta y una nueva respuesta cuando el programa falla.
* `guardar()`: guarda el árbol en un archivo.
* `cargar()`: carga el árbol desde un archivo.

### Responsabilidad

La responsabilidad de esta clase es manejar el árbol de decisión, recorrerlo según las respuestas del usuario y actualizarlo cuando aprende una nueva respuesta.

## Clase InterfazJuego

La clase `InterfazJuego` controla la interfaz gráfica del programa.

### Responsabilidad

Esta clase se encarga de mostrar la ventana del juego, las preguntas, los botones de Sí y No, los mensajes y los campos necesarios cuando el programa debe aprender una nueva respuesta.

La interfaz no contiene toda la lógica del árbol. En su lugar, utiliza la clase `ArbolDecision` para manejar el funcionamiento del juego.

## Representación del árbol

El árbol se representa mediante nodos conectados entre sí.

Cada nodo de pregunta puede tener dos caminos:

* Rama Sí
* Rama No

Los nodos finales representan respuestas posibles, por ejemplo el nombre de un país.

## Recorrido del árbol

El recorrido inicia en la raíz del árbol. Cuando el usuario responde Sí, el programa avanza por la rama Sí. Cuando responde No, avanza por la rama No.

Este proceso continúa hasta llegar a una respuesta final.

## Aprendizaje del árbol

Si el programa intenta adivinar un país y falla, solicita al usuario tres datos:

* La respuesta correcta.
* Una pregunta que diferencie la respuesta correcta de la respuesta incorrecta.
* Si para la respuesta correcta la contestación a esa pregunta sería Sí o No.

Con esa información, el programa reemplaza la respuesta incorrecta por una nueva pregunta y agrega dos respuestas: la nueva respuesta correcta y la respuesta incorrecta anterior.

## Manejo de archivos

El árbol se guarda en archivos JSON dentro de la carpeta `data`.

El archivo principal del proyecto será `paises.json`.

Cada vez que el programa aprende una nueva pregunta y una nueva respuesta, el árbol actualizado se guarda automáticamente en el archivo correspondiente.

## Conclusión

El diseño del proyecto se mantiene simple. Se utilizan pocas clases y cada una tiene una responsabilidad clara. De esta forma, el programa cumple con la Programación Orientada a Objetos, el uso de árboles binarios, la interfaz gráfica y el manejo de archivos.
