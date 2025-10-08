"""Versión incompleta del juego de tortugas.

Las secciones marcadas con TODO deben rellenarse utilizando tipos, variables,
diccionarios, bucles y funciones. El archivo acabado debería comportarse como
``full_game.py`` una vez estén resueltos todos los TODO.
"""

from __future__ import annotations

import turtle


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
START_X = -320
FINISH_X = 300
LANE_HEIGHT = 80
LINE_EXTRA_HEIGHT = 30

# TODO: crea un diccionario de velocidades con al menos tres tortugas
#       usando colores como claves y distancias (float o int) como valores.
RUNNER_SPEEDS: dict[str, float] = {}


def prepare_screen() -> turtle.Screen:
    """Devuelve la pantalla de Turtle configurada para la carrera."""
    screen = turtle.Screen()
    # TODO: usa SCREEN_WIDTH y SCREEN_HEIGHT para ajustar el tamaño
    # TODO: asigna un título a la ventana de la carrera
    return screen


def calculate_lane_positions(num_lanes: int) -> list[float]:
    """Calcula la coordenada Y para cada carril centrando la pista."""
    # TODO: valida que num_lanes sea mayor que 0
    # TODO: calcula la lista de posiciones usando un bucle for
    raise NotImplementedError


def draw_track(num_lanes: int) -> None:
    """Dibuja las líneas horizontales de la pista."""
    painter = turtle.Turtle(visible=False)
    painter.speed(0)
    painter.pensize(2)
    total_length = FINISH_X - START_X

    # TODO: obtiene las posiciones con calculate_lane_positions
    # TODO: usa un bucle para dibujar cada carril con forward(total_length)
    raise NotImplementedError


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
    # TODO: reutiliza calculate_lane_positions para obtener los extremos
    # TODO: llama a draw_vertical_line pasando START_X y los valores calculados
    raise NotImplementedError


def draw_finish_line(num_lanes: int) -> None:
    """Marca la línea de meta con un trazo vertical rojo."""
    # TODO: reutiliza calculate_lane_positions para obtener los extremos
    # TODO: llama a draw_vertical_line pasando FINISH_X y los valores calculados
    raise NotImplementedError


def setup_track(screen: turtle.Screen, num_lanes: int) -> None:
    """Dibuja la pista completa antes de mostrar a las tortugas corredoras."""
    screen.tracer(0)
    # TODO: dibuja la pista, la salida y la meta usando las funciones anteriores
    screen.tracer(1)


def create_runners(speed_map: dict[str, float]) -> list[tuple[turtle.Turtle, float]]:
    """Crea tortugas a partir de un diccionario de velocidades."""
    # TODO: calcula las posiciones de los carriles según len(speed_map)
    # TODO: recorre speed_map.items() junto con las posiciones y crea cada tortuga
    # TODO: devuelve una lista de tuplas (tortuga, velocidad)
    raise NotImplementedError


def run_race(racers: list[tuple[turtle.Turtle, float]]) -> turtle.Turtle:
    """Avanza a las tortugas hasta que alguna cruza la línea de meta."""
    # TODO: inicializa una variable para almacenar a la ganadora
    # TODO: usa un bucle while para avanzar a cada tortuga según su velocidad
    # TODO: rompe el bucle cuando una tortuga alcance FINISH_X y devuélvela
    raise NotImplementedError


def main(speed_map: dict[str, float] | None = None) -> None:
    """Punto de entrada del juego: prepara la pista y lanza la carrera."""
    # TODO: si no se recibe speed_map, utiliza RUNNER_SPEEDS como valor por defecto
    # TODO: crea la pantalla y configura la pista con setup_track
    # TODO: genera las tortugas con create_runners y llama a run_race
    # TODO: mantén la ventana abierta con screen.mainloop()
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: invoca main() para probar la solución cuando termines
    pass
