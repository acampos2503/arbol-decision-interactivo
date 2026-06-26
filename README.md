# arbol de decision interactivo

proyecto de taller de programacion desarrollado en python.
instituto tecnologico de costa rica 

## descripcion

este proyecto consiste en una aplicacion grafica llamada **adivina en que estoy pensando**.

el programa utiliza un arbol binario de decision para hacer preguntas de **si** o **no** e intentar adivinar el elemento pensado por el usuario.

el arbol principal del proyecto es el archivo de **paises**, pero tambien se incluyen otros archivos json de ejemplo con diferentes categorias.

si el programa no logra adivinar correctamente, puede aprender una nueva respuesta y una nueva pregunta. despues de aprender, el arbol se guarda automaticamente en el archivo json.

## tecnologias utilizadas

- python
- tkinter
- programacion orientada a objetos
- archivos json
- arbol binario de decision

## estructura del proyecto

```text
arbol-decision-interactivo/
│
├── main.py
├── arbol_decision.py
├── interfaz.py
├── README.md
│
├── data/
│   ├── paises.json
│   ├── animales.json
│   ├── comidas.json
│   ├── deportes.json
│   └── personajes.json
│
└── docs/
    └── diseno_orientado_a_objetos.md
```

## archivos principales

### main.py

archivo principal del proyecto.

se encarga de importar la interfaz, crear la aplicacion e iniciar el programa.

### arbol_decision.py

contiene la logica principal del arbol de decision.

en este archivo se manejan los nodos, el recorrido del arbol, el aprendizaje, la carga de archivos y el guardado automatico del arbol actualizado.

### interfaz.py

contiene la interfaz grafica del programa.

este archivo se encarga de mostrar la ventana principal, los botones, las preguntas, los mensajes y el formulario que se usa cuando el programa debe aprender una nueva respuesta.

### data/

carpeta donde se guardan los archivos json con los arboles de decision.

cada archivo contiene preguntas, respuestas y ramas de si o no.

### docs/

carpeta donde se encuentra el documento de diseno orientado a objetos.

## archivos json incluidos

el proyecto incluye cinco archivos de ejemplo:

- paises.json
- animales.json
- comidas.json
- deportes.json
- personajes.json

el archivo principal que se carga al iniciar el programa es:

```text
data/paises.json
```

tambien se puede cargar otro archivo desde la interfaz usando el boton de cargar archivo.

## como ejecutar el programa

para ejecutar el programa, se debe abrir una terminal en la carpeta del proyecto y escribir:

```bash
python main.py
```

en mac tambien se puede usar:

```bash
python3 main.py
```

## funcionamiento del juego

1. el usuario abre el programa.
2. el usuario puede iniciar con el arbol principal o cargar otro archivo json.
3. el programa muestra una pregunta.
4. el usuario responde con si o no.
5. el programa avanza por el arbol segun la respuesta.
6. al llegar a una respuesta final, el programa intenta adivinar.
7. si adivina correctamente, muestra un mensaje de victoria.
8. si falla, pide una nueva respuesta y una nueva pregunta.
9. el arbol se actualiza y se guarda automaticamente.

## aprendizaje del arbol

si el programa falla al adivinar, le pide al usuario la respuesta correcta y una pregunta que sirva para diferenciarla de la respuesta incorrecta.

tambien le pregunta si para la nueva respuesta la contestacion seria si o no.

con esa informacion, el programa actualiza el arbol y guarda los cambios en el archivo json.

## manejo de archivos

los arboles se guardan en formato json.

cada nodo del arbol tiene un tipo y un texto.

los nodos de pregunta tienen dos ramas:

- si
- no

los nodos de respuesta son hojas del arbol y no tienen ramas.

## validaciones

el programa valida que el usuario no deje campos vacios cuando agrega una nueva respuesta.

tambien valida que se seleccione si o no antes de guardar el aprendizaje.

si un archivo json no se puede cargar correctamente, el programa muestra un mensaje y continua con un arbol basico.

## autor

alejandro campos lopez 2026090719 

## profesor

diego mora 
