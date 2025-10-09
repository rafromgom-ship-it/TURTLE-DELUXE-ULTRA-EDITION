"""Versión incompleta del juego de tortugas.

Las secciones marcadas con TODO deben rellenarse utilizando tipos, variables,
diccionarios, bucles y funciones. El archivo acabado debería comportarse como
``full_game.py`` una vez estén resueltos todos los TODO.
"""

from __future__ import annotations

import turtle
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
START_X = -320
FINISH_X = 300
LANE_HEIGHT = 80
LINE_EXTRA_HEIGHT = 30
number_of_runners = int(6)
colores = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", 
    "gray", "cyan", "magenta", "lime", "maroon", "navy", "olive", "teal", "aqua", "fuchsia",
    "silver", "gold", "coral", "crimson", "indigo", "khaki", "lavender", "orchid", "plum",
    "salmon", "tan", "tomato", "violet"
]

def prepare_screen() -> turtle.Screen:
    """Devuelve la pantalla de Turtle configurada para la carrera."""
    screen = turtle.Screen()  # Crea la ventana principal donde se mostrará la carrera.
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)  # Ajusta el tamaño de la ventana usando las constantes declaradas.
    screen.title("Circuit de la Torthue")  # Asigna un título descriptivo a la ventana.
    return screen  # Devuelve la pantalla configurada para que otras funciones la utilicen.



def calculate_lane_positions(num_lanes: int) -> list[float]:
    """Calcula la coordenada Y para cada carril centrando la pista."""
    total_height = num_lanes * LANE_HEIGHT
    top_center= total_height / 2
    positions = []
    for i in range (num_lanes):
        lane = top_center - i * LANE_HEIGHT
        positions.append(lane)

    return positions


def draw_track(num_lanes: int) -> None:
    """Dibuja las líneas horizontales de la pista."""
    painter = turtle.Turtle(visible=False)
    painter.speed(0)
    painter.pensize(4)
    total_length = FINISH_X - START_X
    positions = calculate_lane_positions(number_of_runners)
    for i in range(num_lanes):
        for i in positions:
            painter.penup()
            painter.goto(START_X, i)
            painter.setheading(0)
            painter.pendown()
            painter.forward(total_length)

def draw_vertical_line(x_pos: float, top_y: float, bottom_y: float) -> None:
    """Dibuja una línea vertical roja entre las coordenadas dadas."""
    marker = turtle.Turtle(visible=False)
    marker.speed(0)
    marker.pensize(2)
    marker.color("red")
    marker.penup()
    marker.goto(x_pos, top_y)
    marker.setheading(270)
    marker.pendown()
    marker.forward(top_y - bottom_y)


def draw_start_line(num_lanes: int) -> None:
    """Marca la línea de salida con un trazo vertical rojo."""
    positions = calculate_lane_positions(num_lanes)
    draw_vertical_line(START_X, positions[0] + LINE_EXTRA_HEIGHT, positions[-1] - LINE_EXTRA_HEIGHT)



def draw_finish_line(num_lanes: int) -> None:
    """Marca la línea de meta con un trazo vertical rojo."""
    positions = calculate_lane_positions(num_lanes)
    draw_vertical_line(FINISH_X, positions[0] + LINE_EXTRA_HEIGHT, positions[-1] - LINE_EXTRA_HEIGHT)
    


def setup_track(screen: turtle.Screen, num_lanes: int) -> None:
    """Dibuja la pista completa antes de mostrar a las tortugas corredoras."""
    # Inicializa la ventana principal donde se verá la animación.
    screen.tracer(0)  # Apaga la animación mientras preparamos la pista.
    draw_track(num_lanes)  # Dibuja la pista con las líneas horizontales que delimitan los carriles.
    draw_start_line(num_lanes)  # Marca la línea de salida de la carrera.
    draw_finish_line(num_lanes)  # Marca la línea de llegada de la carrera.
    screen.tracer(1)


def create_runners(number_of_runners: int) -> list[tuple[turtle.Turtle, float]]:
    """Crea tortugas a partir de un diccionario de velocidades."""
    corredores = []

    positions = calculate_lane_positions(number_of_runners)

    for i in range(number_of_runners):
        tortuga = turtle.Turtle(shape="turtle")
        tortuga.color(colores.pop(random.randint(0, len(colores)-1)))
        tortuga.penup()
        tortuga.goto(START_X, positions[i])
        tortuga.setheading(0)
        # ...añade la tortuga y velocidad a la lista de corredores...
        corredores.append(tortuga)
    return corredores


def run_race(racers: list[turtle.Turtle]) -> turtle.Turtle:
    """Avanza a las tortugas hasta que alguna cruza la línea de meta."""
    winner = None
    while winner is None:
        for tortuga in racers:
            velocidad = random.uniform(1.2, 7.0)
            tortuga.forward(velocidad)
            if tortuga.xcor() >= FINISH_X:
                winner = tortuga
                break
    return winner
    
def show_winner_message(winner: turtle.Turtle) -> None:
    announcer = turtle.Turtle(visible=False) # MUESTRA EL GANADOR
    announcer.penup()
    announcer.color("black")
    announcer.goto(0, -SCREEN_HEIGHT // 2 + 40)
    announcer.write(
        f"El ganador es {winner.color()[0]}!", 
        align="center",
        font=("Arial", 16, "bold")
    )


def main() -> None:
    screen = prepare_screen()
    setup_track(screen, number_of_runners)
    racers = create_runners(number_of_runners)
    winner = run_race(racers)
    show_winner_message(winner)
    print(f"¡La tortuga ganadora es de color {winner.color()[0]}!")
    screen.mainloop()
    
if __name__ == "__main__":
    main()
