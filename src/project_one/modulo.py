from . import config

def main():
    print("¡Hola, este es el módulo principal de mi proyecto!")
    print("¡Espero que te guste!")
    print("¡Hasta luego!")
    print("Ruta para guardar datos:", config.DATA_DIR)
    print("Número de épocas:", config.API_KEY)

if __name__ == "__main__":
    main() 