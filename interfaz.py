'''
interfaz grafica del juego:
- muestra la pantalla inicial
- deja jugar con botones de si y no
- deja cargar arboles desde archivos
- muestra el formulario para aprender
alejandro campos lopez
2026090719
'''

import tkinter as tk
from tkinter import filedialog, messagebox

from arbol_decision import ArbolDecision


class InterfazJuego:
    def __init__(self):
        # se crea la ventana principal
        self.ventana = tk.Tk()

        # titulo de la ventana
        self.ventana.title("Árbol de Decisión Interactivo")

        # tamano de la ventana
        self.ventana.geometry("650x450")

        # se carga el arbol principal
        self.arbol = ArbolDecision("data/paises.json")

    def iniciar(self):
        # se muestra el menu principal
        self.mostrar_inicio()

        # se mantiene abierta la ventana
        self.ventana.mainloop()

    def limpiar_ventana(self):
        # borra todo lo que este en pantalla
        for elemento in self.ventana.winfo_children():
            elemento.destroy()

    def mostrar_inicio(self):
        # pantalla inicial del programa
        self.limpiar_ventana()

        # titulo principal
        titulo = tk.Label(
            self.ventana,
            text="Adivina en qué estoy pensando",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=20)

        # instrucciones del juego
        instrucciones = tk.Label(
            self.ventana,
            text="Cargá un archivo JSON o usá el árbol principal.\n"
                "Luego pensá en un elemento y respondé Sí o No.",
            font=("Arial", 12)
        )
        instrucciones.pack(pady=10)

        # boton para iniciar una partida
        boton_iniciar = tk.Button(
            self.ventana,
            text="Iniciar partida",
            width=25,
            command=self.iniciar_partida
        )
        boton_iniciar.pack(pady=8)

        # boton para cargar un archivo json
        boton_cargar = tk.Button(
            self.ventana,
            text="Cargar árbol desde archivo",
            width=25,
            command=self.cargar_archivo
        )
        boton_cargar.pack(pady=8)

        # boton para cerrar el programa
        boton_salir = tk.Button(
            self.ventana,
            text="Salir",
            width=25,
            command=self.ventana.destroy
        )
        boton_salir.pack(pady=8)

    def cargar_archivo(self):
        # abre una ventana para buscar el archivo
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo del árbol",
            filetypes=[
                ("Archivos JSON", "*.json"),
                ("Todos los archivos", "*.*")
            ]
        )

        # si no se escoge nada, no hace nada
        if ruta == "":
            return

        # se intenta cargar el archivo escogido
        cargado = self.arbol.cambiar_archivo(ruta)

        # mensaje si cargo bien
        if cargado:
            messagebox.showinfo(
                "Archivo cargado",
                "El árbol se cargó correctamente."
            )

        # mensaje si hubo error
        else:
            messagebox.showwarning(
                "Error al cargar",
                "No se pudo cargar el archivo.\n"
                "El programa continuará con un árbol básico."
            )

        # vuelve al menu
        self.mostrar_inicio()

    def iniciar_partida(self):
        # reinicia el arbol desde el inicio
        self.arbol.reiniciar()

        # muestra la primera pregunta
        self.mostrar_nodo_actual()

    def mostrar_nodo_actual(self):
        # limpia la pantalla
        self.limpiar_ventana()

        # obtiene el texto del nodo actual
        texto_actual = self.arbol.obtener_texto_actual()

        # revisa si ya llego a una respuesta
        if self.arbol.nodo_actual_es_respuesta():
            # pregunta si la respuesta era correcta
            pregunta = tk.Label(
                self.ventana,
                text="¿Estabas pensando en " + texto_actual + "?",
                font=("Arial", 16, "bold")
            )
            pregunta.pack(pady=40)

            # boton si adivino
            boton_si = tk.Button(
                self.ventana,
                text="Sí",
                width=15,
                command=self.mostrar_gano
            )
            boton_si.pack(pady=8)

            # boton si fallo
            boton_no = tk.Button(
                self.ventana,
                text="No",
                width=15,
                command=self.mostrar_aprendizaje
            )
            boton_no.pack(pady=8)

        else:
            # muestra una pregunta normal del arbol
            pregunta = tk.Label(
                self.ventana,
                text=texto_actual,
                font=("Arial", 16, "bold")
            )
            pregunta.pack(pady=40)

            # avanza por la rama si
            boton_si = tk.Button(
                self.ventana,
                text="Sí",
                width=15,
                command=lambda: self.responder("si")
            )
            boton_si.pack(pady=8)

            # avanza por la rama no
            boton_no = tk.Button(
                self.ventana,
                text="No",
                width=15,
                command=lambda: self.responder("no")
            )
            boton_no.pack(pady=8)

        # boton para volver al menu
        boton_inicio = tk.Button(
            self.ventana,
            text="Volver al inicio",
            width=20,
            command=self.mostrar_inicio
        )
        boton_inicio.pack(pady=20)

    def responder(self, respuesta):
        # manda la respuesta al arbol
        self.arbol.responder(respuesta)

        # actualiza la pantalla
        self.mostrar_nodo_actual()

    def mostrar_gano(self):
        # pantalla cuando el programa gana
        self.limpiar_ventana()

        # mensaje de victoria
        mensaje = tk.Label(
            self.ventana,
            text="¡Gané! Adiviné correctamente.",
            font=("Arial", 16, "bold")
        )
        mensaje.pack(pady=40)

        # boton para jugar otra vez
        boton_nueva = tk.Button(
            self.ventana,
            text="Nueva partida",
            width=20,
            command=self.iniciar_partida
        )
        boton_nueva.pack(pady=8)

        # boton para volver al menu
        boton_inicio = tk.Button(
            self.ventana,
            text="Volver al inicio",
            width=20,
            command=self.mostrar_inicio
        )
        boton_inicio.pack(pady=8)

        # boton para salir
        boton_salir = tk.Button(
            self.ventana,
            text="Salir",
            width=20,
            command=self.ventana.destroy
        )
        boton_salir.pack(pady=8)

    def mostrar_aprendizaje(self):
        # guarda la respuesta que fallo
        respuesta_incorrecta = self.arbol.obtener_texto_actual()

        # limpia la pantalla
        self.limpiar_ventana()

        # titulo de aprendizaje
        titulo = tk.Label(
            self.ventana,
            text="No adiviné. Ayudame a aprender.",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=15)

        # muestra lo que el programa habia pensado
        texto_error = tk.Label(
            self.ventana,
            text="Yo había pensado que era: " + respuesta_incorrecta,
            font=("Arial", 11)
        )
        texto_error.pack(pady=5)

        # pide la respuesta correcta
        etiqueta_respuesta = tk.Label(
            self.ventana,
            text="¿Cuál era la respuesta correcta?"
        )
        etiqueta_respuesta.pack(pady=5)

        # campo para escribir la respuesta
        entrada_respuesta = tk.Entry(self.ventana, width=45)
        entrada_respuesta.pack(pady=5)

        # pide la nueva pregunta
        etiqueta_pregunta = tk.Label(
            self.ventana,
            text="Escribí una pregunta que diferencie ambas respuestas:"
        )
        etiqueta_pregunta.pack(pady=5)

        # campo para escribir la pregunta
        entrada_pregunta = tk.Entry(self.ventana, width=45)
        entrada_pregunta.pack(pady=5)

        # pregunta si para la respuesta correcta seria si o no
        etiqueta_si_no = tk.Label(
            self.ventana,
            text="Para la respuesta correcta, la respuesta a esa pregunta sería:"
        )
        etiqueta_si_no.pack(pady=5)

        # variable para guardar si o no
        opcion = tk.StringVar()

        # opcion si
        radio_si = tk.Radiobutton(
            self.ventana,
            text="Sí",
            variable=opcion,
            value="si"
        )
        radio_si.pack()

        # opcion no
        radio_no = tk.Radiobutton(
            self.ventana,
            text="No",
            variable=opcion,
            value="no"
        )
        radio_no.pack()

        # boton para guardar lo aprendido
        boton_guardar = tk.Button(
            self.ventana,
            text="Guardar aprendizaje",
            width=25,
            command=lambda: self.guardar_aprendizaje(
                entrada_respuesta,
                entrada_pregunta,
                opcion
            )
        )
        boton_guardar.pack(pady=15)

        # boton para cancelar
        boton_cancelar = tk.Button(
            self.ventana,
            text="Cancelar",
            width=20,
            command=self.mostrar_inicio
        )
        boton_cancelar.pack(pady=5)

    def guardar_aprendizaje(self, entrada_respuesta, entrada_pregunta, opcion):
        # toma los datos escritos
        respuesta_correcta = entrada_respuesta.get()
        nueva_pregunta = entrada_pregunta.get()
        respuesta_si_no = opcion.get()

        # valida la respuesta correcta
        if respuesta_correcta.strip() == "":
            messagebox.showwarning(
                "Dato faltante",
                "Debe escribir la respuesta correcta."
            )
            return

        # valida la nueva pregunta
        if nueva_pregunta.strip() == "":
            messagebox.showwarning(
                "Dato faltante",
                "Debe escribir una nueva pregunta."
            )
            return

        # valida que se seleccione si o no
        if respuesta_si_no == "":
            messagebox.showwarning(
                "Dato faltante",
                "Debe seleccionar Sí o No."
            )
            return

        # convierte la opcion a verdadero o falso
        respuesta_correcta_es_si = respuesta_si_no == "si"

        # manda los datos al arbol
        aprendido = self.arbol.aprender(
            respuesta_correcta,
            nueva_pregunta,
            respuesta_correcta_es_si
        )

        # mensaje si se guardo bien
        if aprendido:
            messagebox.showinfo(
                "Aprendizaje guardado",
                "Listo, ya aprendí la nueva respuesta."
            )
            self.mostrar_aprendido()

        # mensaje si paso algun error
        else:
            messagebox.showerror(
                "Error",
                "No se pudo guardar el aprendizaje."
            )

    def mostrar_aprendido(self):
        # pantalla luego de aprender
        self.limpiar_ventana()

        # mensaje principal
        mensaje = tk.Label(
            self.ventana,
            text="El árbol fue actualizado correctamente.",
            font=("Arial", 16, "bold")
        )
        mensaje.pack(pady=40)

        # boton para jugar de nuevo
        boton_nueva = tk.Button(
            self.ventana,
            text="Nueva partida",
            width=20,
            command=self.iniciar_partida
        )
        boton_nueva.pack(pady=8)

        # boton para volver al menu
        boton_inicio = tk.Button(
            self.ventana,
            text="Volver al inicio",
            width=20,
            command=self.mostrar_inicio
        )
        boton_inicio.pack(pady=8)

        # boton para salir
        boton_salir = tk.Button(
            self.ventana,
            text="Salir",
            width=20,
            command=self.ventana.destroy
        )
        boton_salir.pack(pady=8)