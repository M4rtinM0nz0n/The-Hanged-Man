# Informe de Desarrollo del Proyecto: The Hanged Man
Autores: Agustín Russo & Martín (Ezequiel) Monzón
## 1. Breve descripción del problema a resolver
El objetivo del proyecto era desarrollar un juego de "ahorcado" para terminal que permitiera al jugador adivinar palabras de forma interactiva. Los principales retos residían en gestionar la lógica de la adivinación de letras, registrar los intentos fallidos, mostrar el progreso del juego, esos creemos que fueron los 3 retos más importantes
## 2. Breve descripción de la estructura del proyecto
El proyecto se organizó en un único archivo Python (The-Hanged-Man.py, llamado así por la carta del Tarot, sino se llamaría the Hangman) que contiene todas las funciones necesarias para ejecutar el juego. La estructura lógica del programa se puede resumir en:
    • Definición de recursos:
        ◦ Lista de palabras posibles (words)
        ◦ ASCII art para representar el ahorcado (theHangedManModes)
    • Funciones auxiliares:
        ◦ normalize(parámetro: str <string>): normaliza cadenas eliminando acentos, espacios y convirtiendo a minúsculas
        ◦ displayTitle(): imprime el título en unas grandes letras ASCII
        ◦ clearScreen(): limpia la terminal de manera cross-platform (ejecuta cls si estás en Windows y clear si estás en posix)
        ◦ getRestart(): gestiona la opción de reiniciar o salir del juego o no
    • Función principal del juego:
        ◦ play(parámetro: words <array>): implementa la lógica del juego, incluyendo control de letras adivinadas, errores cometidos, visualización del progreso y finalización por victoria o derrota
## 3. Organización dentro del equipo
El desarrollo se realizó en colaboración de manera paralela:
    • Agustín Russo se encargó principalmente de la lógica del juego, incluyendo:
        ◦ Control de letras adivinadas y errores
        ◦ Verificación de victoria/derrota
        ◦ Integración del ASCII art según los errores
    • Martín (Ezequiel) Monzón se centró en la interfaz y robustez del código, implementando:
        ◦ Funciones de normalización de palabras
        ◦ Limpieza de pantalla y visualización del título
        ◦ Manejo de la opción de reiniciar el juego y validación de entradas
Posteriormente, ambos colaboramos revisando el código entero, asegurando que cada función cumpliese su propósito

## 4. Secciones importantes en el código
    1. Definición de recursos:
        ◦ Contiene la lista de palabras y los distintos estados gráficos del ahorcado.
    2. Funciones de utilidades:
        ◦ normalize(), displayTitle(), clearScreen(), getRestart().
        ◦ Estas funciones permiten mantener el código limpio y modular.
    3. Función play(parámetro: words <array>):
        ◦ Maneja toda la lógica del juego, incluyendo validación de entradas, actualización de letras adivinadas y errores, y finalización.
    4. Bucle principal (while keepPlaying <boolean>):
        ◦ Controla la ejecución de partidas consecutivas y permite al usuario decidir si continuar jugando o salir.

## 5. Conclusiones y posibles mejoras
El proyecto logró cumplir con el objetivo principal, que era crear un juego funcional del Ahorcado en consola, robusto frente a entradas inválidas y con soporte para palabras con acentos. La colaboración del equipo permitió dividir responsabilidades y mantener el código modular y legible.
Posibles mejoras futuras:
    • Cargar las palabras desde un archivo externo, que podría ser un archivo de texto (.txt), otro módulo .py, o incluso un JSON para facilitar la expansión del array de palabras (que es demasiado limitado, por cierto)
    • Implementar niveles de dificultad, posiblemente ajustando la longitud de palabras, y, quizás, mostrar más o menos palabras dependiendo del nivel de dificultad.
    • Migrar el juego a una interfaz gráfica simple (por ejemplo usando tkinter) para mejorar la experiencia de usuario
    • Guardar estadísticas de partidas, como número de victorias o letras más adivinadas, para aumentar el aspecto interactivo, en otro archivo externo, podría ser un JSON donde al usuario se le pediría ingresar su nombre para registrarlo.
