'''
py del árbol de decisión:
- Hace preguntas de Sí o No para adivinar un país.
- Recorre el árbol según las respuestas del usuario.
- Aprende una nueva pregunta si falla al adivinar.
- Guarda y carga la información usando archivos JSON.
alejandro campos lopez
2026090719
taller de progra 2026
'''

import json
import os


import json
import os


class Nodo:
    def __init__(self, tipo, texto, si=None, no=None):
        # tipo puede ser "pregunta" o "respuesta"
        self.tipo = tipo

        # texto guarda la pregunta o la respuesta final
        self.texto = texto

        # si y no son las dos ramas del árbol
        self.si = si
        self.no = no

    def es_respuesta(self):
        # Retorna True si el nodo es una respuesta final
        return self.tipo == "respuesta"

    def convertir_a_diccionario(self):
        # Convierte el nodo en diccionario para poder guardarlo en JSON
        datos = {
            "tipo": self.tipo,
            "texto": self.texto
        }

        # Si es una pregunta, también se guardan las ramas Sí y No
        if self.tipo == "pregunta":
            datos["si"] = self.si.convertir_a_diccionario()
            datos["no"] = self.no.convertir_a_diccionario()

        return datos


def crear_nodo_desde_diccionario(datos):
    # Esta función convierte un diccionario en un nodo del árbol

    if not isinstance(datos, dict):
        raise ValueError("El nodo no tiene formato correcto.")

    # Se revisa que el nodo tenga los datos básicos
    if "tipo" not in datos or "texto" not in datos:
        raise ValueError("Faltan datos en el nodo.")

    tipo = datos["tipo"]
    texto = datos["texto"]

    # Si el nodo es una respuesta, no necesita ramas
    if tipo == "respuesta":
        return Nodo("respuesta", texto)

    # Si el nodo es una pregunta, debe tener rama Sí y rama No
    if tipo == "pregunta":
        if "si" not in datos or "no" not in datos:
            raise ValueError("Una pregunta debe tener rama Sí y rama No.")

        # Se crean los nodos hijos de forma recursiva
        nodo_si = crear_nodo_desde_diccionario(datos["si"])
        nodo_no = crear_nodo_desde_diccionario(datos["no"])

        return Nodo("pregunta", texto, nodo_si, nodo_no)

    # Si el tipo no es pregunta ni respuesta, el archivo está malo
    raise ValueError("Tipo de nodo no válido.")


class ArbolDecision:
    def __init__(self, archivo="data/paises.json"):
        # Archivo principal del árbol
        self.archivo = archivo

        # raiz es el primer nodo del árbol
        self.raiz = None

        # actual es el nodo donde va la partida
        self.actual = None

        # Se guarda el último error para poder mostrarlo en la interfaz
        self.ultimo_error = ""

        # Al crear el árbol, se intenta cargar desde el archivo
        self.cargar_arbol()

    def crear_arbol_por_defecto(self):
        # Este árbol pequeño se usa si el archivo no existe o tiene errores
        return Nodo(
            "pregunta",
            "¿Está en América?",
            Nodo("respuesta", "Costa Rica"),
            Nodo("respuesta", "España")
        )

    def reiniciar(self):
        # Reinicia la partida desde la raíz del árbol
        self.actual = self.raiz

    def obtener_texto_actual(self):
        # Devuelve la pregunta o respuesta donde está la partida
        if self.actual is None:
            return ""

        return self.actual.texto

    def nodo_actual_es_respuesta(self):
        # Revisa si ya se llegó a una respuesta final
        if self.actual is None:
            return False

        return self.actual.es_respuesta()

    def responder(self, respuesta):
        # Mueve la partida dependiendo de la respuesta del usuario

        if self.actual is None:
            return

        # Si ya estamos en una respuesta, no se puede avanzar más
        if self.actual.es_respuesta():
            return

        respuesta = respuesta.lower().strip()

        # Si responde Sí, se avanza por la rama Sí
        if respuesta == "si" or respuesta == "sí" or respuesta == "s":
            self.actual = self.actual.si

        # Si no, se avanza por la rama No
        else:
            self.actual = self.actual.no

    def aprender(self, respuesta_correcta, nueva_pregunta, respuesta_correcta_es_si):
        # Este método se usa cuando el programa falla al adivinar

        if self.actual is None:
            return False

        # Solo se puede aprender cuando estamos en una respuesta final
        if not self.actual.es_respuesta():
            return False

        # Se limpian los textos para evitar espacios vacíos
        respuesta_correcta = respuesta_correcta.strip()
        nueva_pregunta = nueva_pregunta.strip()

        # Validación para que el usuario no deje campos vacíos
        if respuesta_correcta == "" or nueva_pregunta == "":
            return False

        # Esta era la respuesta incorrecta que el programa había dado
        respuesta_anterior = self.actual.texto

        # Se crean los dos nuevos nodos de respuesta
        nodo_correcto = Nodo("respuesta", respuesta_correcta)
        nodo_anterior = Nodo("respuesta", respuesta_anterior)

        # El nodo actual deja de ser respuesta y ahora será una pregunta
        self.actual.tipo = "pregunta"
        self.actual.texto = nueva_pregunta

        # Por si la respuesta viene como texto en vez de True o False
        if isinstance(respuesta_correcta_es_si, str):
            respuesta_correcta_es_si = respuesta_correcta_es_si.lower().strip()
            respuesta_correcta_es_si = (
                respuesta_correcta_es_si == "si"
                or respuesta_correcta_es_si == "sí"
                or respuesta_correcta_es_si == "s"
            )

        # Si para la nueva respuesta la pregunta se contesta con Sí
        if respuesta_correcta_es_si:
            self.actual.si = nodo_correcto
            self.actual.no = nodo_anterior

        # Si para la nueva respuesta la pregunta se contesta con No
        else:
            self.actual.si = nodo_anterior
            self.actual.no = nodo_correcto

        # Se guarda el árbol actualizado automáticamente
        self.guardar_arbol()

        # Se reinicia la partida para poder jugar otra vez
        self.reiniciar()

        return True

    def guardar_arbol(self):
        # Guarda el árbol completo en el archivo JSON

        try:
            carpeta = os.path.dirname(self.archivo)

            # Si la carpeta no existe, se crea
            if carpeta != "" and not os.path.exists(carpeta):
                os.makedirs(carpeta)

            # Se abre el archivo y se guarda la información
            with open(self.archivo, "w", encoding="utf-8") as archivo_json:
                json.dump(
                    self.raiz.convertir_a_diccionario(),
                    archivo_json,
                    indent=4,
                    ensure_ascii=False
                )

            return True

        except OSError:
            # Si ocurre un error, se guarda el mensaje
            self.ultimo_error = "No se pudo guardar el archivo."
            return False

    def cargar_arbol(self):
        # Carga el árbol desde el archivo JSON

        self.ultimo_error = ""

        try:
            # Si el archivo no existe, se usa un árbol básico
            if not os.path.exists(self.archivo):
                self.raiz = self.crear_arbol_por_defecto()
                self.guardar_arbol()
                self.reiniciar()
                return False

            # Si el archivo está vacío, también se usa un árbol básico
            if os.path.getsize(self.archivo) == 0:
                self.raiz = self.crear_arbol_por_defecto()
                self.guardar_arbol()
                self.reiniciar()
                return False

            # Se abre el archivo JSON
            with open(self.archivo, "r", encoding="utf-8") as archivo_json:
                datos = json.load(archivo_json)

            # Se reconstruye el árbol usando los datos del archivo
            self.raiz = crear_nodo_desde_diccionario(datos)

            # Se inicia la partida desde la raíz
            self.reiniciar()

            return True

        except json.JSONDecodeError:
            # Error cuando el JSON está mal escrito
            self.raiz = self.crear_arbol_por_defecto()
            self.reiniciar()
            self.ultimo_error = "El archivo tiene formato incorrecto."
            return False

        except (OSError, ValueError):
            # Error al leer el archivo o reconstruir el árbol
            self.raiz = self.crear_arbol_por_defecto()
            self.reiniciar()
            self.ultimo_error = "No se pudo cargar el árbol."
            return False

    def cambiar_archivo(self, nuevo_archivo):
        # Cambia el archivo del árbol y trata de cargarlo
        self.archivo = nuevo_archivo
        return self.cargar_arbol()