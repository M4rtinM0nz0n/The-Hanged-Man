from time import sleep
import unicodedata
import os
import sys
import random

theHangedManModes = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
'''
]

# Me rehuso a programar en español y nombrar esta variable como "palabras"
words = [
    "perro",
    "gato",
    "mesa",
    "silla",
    "reloj",
    "queso",
    "playa",
    "lluvia",
    "bosque",
    "tiburon",
    "montania",
    "castillo",
    "barril",
    "nieve",
    "fuego",
    "globo",
    "lapiz",
    "camino",
    "puente",
    "coche",
    "avion",
    "barco",
    "trenes",
    "planeta",
    "jirafa",
    "sombrero",
    "estrella",
    "volcan",
    "ventana",
    "escuela"
]

# Esto quita tildes y normaliza a minúsculas para comparar con el string que pase el usuario posteriormente
def normalize(str):
    """
        - pasa a minúsculas
        - descompone caracteres unicode (NFD)
        - remueve acentos
    """
    str = str.lower()
    str = str.strip()
    str = unicodedata.normalize('NFD', str)
    str = ''.join(ch for ch in str if unicodedata.category(ch) != 'Mn')
    return str

# Muestra el titulo, no retorna nada, simplemente está pensado así para mostrar constantemente el nombre del juego.
def displayTitle():
    print("""
             ________          __ __                      __  __  ___        
            /_  __/ /  ___    / // /__ ____  ___ ____ ___/ / /  |/  /__ ____ 
             / / / _ \\/ -_)  / _  / _ `/ _ \\/ _ `/ -_) _  / / /|_/ / _ `/ _ \\
            /_/ /_//_/\\__/  /_//_/\\_,_/_//_/\\_, /\\__/\\_,_/ /_/  /_/\\_,_/_//_/
                                           /___/                             
        """)

    # Básicamente ejecuta "cls" específicamente en Windows y, sino, "clear" en cualquier OS basado en Posix
def clearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    return displayTitle()

# Le pregunta al usuario si quiere reiniciar y verifica si la opción que ingresa es válida.
# Si el usuario ingresa cualquier cosa que no sea "si", "s", "n" o "no", le sigue pidiendo que ingrese una opción válida hasta que lo haga.
# El resto es auto-explicativo, si dice que sí el usuario sale, si dice que no, se corta
def getRestart():
    valid = False
    restart = True

    while not valid:
        res = normalize(input("\n¿Salir? (S)i / (n)o: "))

        if res in ["s", "si"]:
            restart = False
            valid = True
        elif res in ["n", "no"]:
            restart = True
            valid = True
        else:
            print("Respuesta inválida. Escribí 's', 'si', 'n' o 'no'.")

    return restart

# Finalmente, se inicia el juego
def play(words):
    word = random.choice(words)

    guessedLetters = []
    wrongLetters = []

    # La cantidad máxima de errores obviamente será el tamaño del array - 1 (índice máximo)
    maxMistakes = len(theHangedManModes) - 1
    gameOver = False

    while not gameOver:
        clearScreen()

        mistakes = len(wrongLetters)
        print(theHangedManModes[mistakes])
        print(f"\nIntentos: {mistakes}/{maxMistakes}")
        print("Letras incorrectas:", " ".join(sorted(wrongLetters)) if wrongLetters else "(ninguna)")

        # Esto construye la representación visible de la palabra, si la letra ya fue adivinada, se muestra, sino, se muestra un guión bajo (_)
        displayWord = " ".join([l if l in guessedLetters else "_" for l in word])
        print("\nPalabra:", displayWord)

        # Si no hay ningún "_" en la palabra, no queda ninguna por adivinar
        if "_" not in displayWord:
            print("\nGanaste!")
            break

        if mistakes >= maxMistakes:
            print("\nPerdiste. La palabra era:", word)
            break


        guess = input("\nLetra: ").strip().lower()

        # Esta es la condición b ásica de la letra, implica que el input no esté vacío y que su longitud sea 1, si no lo es lanza una alerta.
        if not guess.isalpha() or len(guess) != 1:
            print("Introduce una sola letra válida.")
            sleep(1)
            continue

        # Y obvio que busca después en las letras adivinadas/erróneas si el usuario ya adivinó la susodicha.
        if guess in guessedLetters or guess in wrongLetters:
            print("Ya probaste esa letra.")
            sleep(1)
            continue

        if guess in word:
            guessedLetters.append(guess)
        else:
            wrongLetters.append(guess)

    sleep(1)

if __name__ == "__main__":
    keepPlaying = True
    while keepPlaying:
        play(words)
        keepPlaying = getRestart()
    print("\nGracias por jugar!\n")
