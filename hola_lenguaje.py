import os

def main():
    nombre = os.getenv("LANGUAGE")
    print(f"¡Hola, {nombre} desde GitHub!")


if __name__ == "__main__":
    main()
