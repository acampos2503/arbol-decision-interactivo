'''
archivo principal:
- importa la interfaz
- crea la ventana del juego
- inicia el programa
alejandro campos lopez
2026090719
'''
from interfaz import InterfazJuego


def main():
    # crea la app
    app = InterfazJuego()

    # abre la ventana
    app.iniciar()


if __name__ == "__main__":
    # arranca el programa
    main()