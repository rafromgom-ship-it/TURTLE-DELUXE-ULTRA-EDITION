# Turtle-GAME
Este es el primer juego/entregable de teoría. Para comenzar a desarrollar nuestro videojuego, comenzaremos creando un pequeño juego de carreras de tortugas.

Para no comenzar desde cero y poder familiarizarnos con el desarrollo de juegos básicos, se nos provee de una demo del juego con funcionalidad reducida. 

> Cómo entregar: Una vez, tengas el juego resuelto, cada uno de los alumnos del grupo, se encargará de subir un fichero .zip al formulario disponible en ev.us.es con el nombre `tortuga-"Nombre del grupo".zip`

## Cómo ejecutar `demo.py`
1. Asegúrate de tener instalado Python 3 en tu equipo. Puedes comprobarlo ejecutando `python --version` o `python3 --version` en la terminal.
2. Abre una terminal y sitúate en la carpeta del proyecto con `cd /ruta/al/proyecto`.
3. Ejecuta el archivo con uno de los siguientes comandos, según cómo tengas configurado Python:
   - `python demo.py`
   - `python3 demo.py`
4. Si ves la ventana de Turtle, la ejecución ha sido correcta. Para detener el programa, cierra la ventana o usa `Ctrl + C` en la terminal. 

> Nota: No necesitas instalar librerías externas; el módulo `turtle` forma parte de la biblioteca estándar de Python.

## Comienza ejecutando y realizando algunos cambios
Para comenzar a entender el código de la demo, para ello genera otra versión del videojuego en el que haya 4 tortugas, una amarilla y una verde, compitiendo en dos carriles

## Ejercicio: Completa `full_game.py`.

El juego final debe generar una pista para tantas tortugas como se definan, posicionarlas en carriles separados, moverlas según sus velocidades, anunciar a la ganadora y mantener la ventana abierta hasta que el usuario la cierre manualmente; todo esto no ocurre en la demo inicial.

En la carpeta encontrarás un archivo específico para este ejercicio:

- `full_game.py`: plantilla incompleta con instrucciones `TODO` para que practiques tipos, variables, diccionarios, bucles y funciones. Completa todos los apartados para conseguir el juego final.

### Objetivo
Logra que `full_game.py` cuente con todas las partes necesarias para ejecutar la carrera completa resolviendo cada uno de los `TODO` del archivo.

### Pasos recomendados
1. **Revisa las constantes y comentarios** al principio del archivo para entender qué valores se reutilizan en todo el juego.
2. **Rellena las funciones en el orden propuesto**: primero utilidades (`prepare_screen`, `calculate_lane_positions`, `draw_track`, etc.), luego la lógica de creación de tortugas (`create_runners`) y por último la carrera (`run_race` y `main`).
3. **Comprueba el tipado**: respeta las anotaciones de tipo existentes y añade las que resulten necesarias para variables intermedias.
4. **Prueba tus cambios** ejecutando `python full_game.py`. Ajusta lo necesario hasta que la carrera funcione sin errores.
5. **Experimenta con el diccionario de velocidades** (`RUNNER_SPEEDS`) para comprobar que la pista se adapta cuando añades o quitas tortugas.

### Consejos
- Usa `calculate_lane_positions` en el resto de funciones para evitar duplicar cálculos.
- Si la ventana de Turtle no se cierra automáticamente, recuerda finalizar el programa cerrando la ventana o usando `Ctrl + C`.
- Revisa cada `TODO` antes de dar por buena la solución y prueba diferentes configuraciones para asegurarte de que todo responde correctamente.
