from __future__ import annotations
import turtle
import random
import time

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
START_X = -320
FINISH_X = 300
LANE_HEIGHT = 80
LINE_EXTRA_HEIGHT = 30

# Tortugas y sus velocidades (ya no importan para el resultado)
RUNNER_SPEEDS: dict[str, float] = {
    "yellow": 3.5,
    "green": 4.0,
    "blue": 2.8,
    "red": 3.2,
}


def prepare_screen() -> turtle.Screen:
    screen = turtle.Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("Carrera de Tortugas")
    return screen


def calculate_lane_positions(num_lanes: int) -> list[float]:
    if num_lanes <= 0:
        raise ValueError("Debe haber al menos un carril.")
    total_height = (num_lanes - 1) * LANE_HEIGHT
    start_y = total_height / 2
    return [start_y - i * LANE_HEIGHT for i in range(num_lanes)]


def draw_track(num_lanes: int) -> None:
    painter = turtle.Turtle(visible=False)
    painter.speed(0)
    painter.pensize(2)
    positions = calculate_lane_positions(num_lanes) # Posiciones Y de los carriles
    total_length = FINISH_X - START_X

    for y in positions:
        painter.penup()
        painter.goto(START_X, y - LINE_EXTRA_HEIGHT)
        painter.setheading(0)
        painter.pendown()
        painter.forward(total_length)


def draw_vertical_line(x: float, top_y: float, bottom_y: float) -> None:
    marker = turtle.Turtle(visible=False)
    marker.speed(0)
    marker.color("green") # PARA CAMBIAR EL COLOR DE LAS LINEAS
    marker.pensize(2) #ANCHO LINEAS
    marker.penup() 
    marker.goto(x, top_y)
    marker.setheading(270)
    marker.pendown() #SIN ESTO NO HAY LINEA
    marker.forward(top_y - bottom_y) #DIBUJA LA LINEA


def draw_start_line(num_lanes: int) -> None:
    positions = calculate_lane_positions(num_lanes)
    draw_vertical_line(START_X, positions[0] + LINE_EXTRA_HEIGHT, positions[-1] - LINE_EXTRA_HEIGHT) 
    # DIBUJA LA LINEA DE SALIDA


def draw_finish_line(num_lanes: int) -> None:
    positions = calculate_lane_positions(num_lanes)
    draw_vertical_line(FINISH_X, positions[0] + LINE_EXTRA_HEIGHT, positions[-1] - LINE_EXTRA_HEIGHT)
 # DIBUJA LA LINEA DE LLEGADA

def setup_track(screen: turtle.Screen, num_lanes: int) -> None:
    screen.tracer(0) # PONE EL MAPA DEL TIRON
    draw_track(num_lanes)
    draw_start_line(num_lanes)
    draw_finish_line(num_lanes)
    #DIBUJA LO ANTERIOR
    screen.tracer(1) # ACTIVA EL MAPA DE NUEVO


def create_runners(speed_map: dict[str, float]) -> list[tuple[turtle.Turtle, float]]:
    positions = calculate_lane_positions(len(speed_map)) #POSICION TORTUGAS
    runners: list[tuple[turtle.Turtle, float]] = [] #LISTA DE TORTUGAS

    for (color, speed), y in zip(speed_map.items(), positions): # CREA LAS TORTUGAS
        t = turtle.Turtle(shape="turtle")
        t.color(color) # COLOR DE LA TORTUGA
        t.penup()
        t.goto(START_X, y) # POSICION INICIAL
        runners.append((t, speed)) 

    return runners


def countdown(screen: turtle.Screen) -> None:
    announcer = turtle.Turtle(visible=False)
    announcer.penup()
    announcer.goto(0, 0)
    announcer.color("green") # COLOR DEL TEXTO INICIO

    announcer.write("¡Preparados!", align="center", font=("Arial", 24, "bold"))
    time.sleep(1)

    for i in range(3, 0, -1):
        announcer.clear()
        announcer.write(str(i), align="center", font=("Arial", 36, "bold"))
        time.sleep(1)

    announcer.clear() #LIMPIA EL TEXTO
    announcer.write("¡YA!", align="center", font=("Arial", 28, "bold"))
    time.sleep(1) # MUESTRA "YA" POR 1 SEGUNDO
    announcer.clear()


def run_race(racers: list[tuple[turtle.Turtle, float]]) -> turtle.Turtle: 
    """Simula una carrera igualada con un ganador aleatorio."""
    winner_turtle, _ = random.choice(racers)

    race_over = False
    while not race_over:
        for turtle_obj, _ in racers:
            if turtle_obj == winner_turtle:
                velocidad = random.uniform(5.0, 7.0)  # Gana con paso ligeramente mayor
            else:
                velocidad = random.uniform(3.5, 6.8)  # Paso muy similar

            turtle_obj.forward(velocidad) # MUEVE LA TORTUGA

            if turtle_obj.xcor() >= FINISH_X:
                race_over = True
                break

    return winner_turtle


def show_winner_message(winner: turtle.Turtle, duration: float) -> None:
    announcer = turtle.Turtle(visible=False) # MUESTRA EL GANADOR
    announcer.penup()
    announcer.color("black")
    announcer.goto(0, -SCREEN_HEIGHT // 2 + 40)
    announcer.write(
        f"Ganador: {winner.color()[0]} - Tiempo: {duration:.2f} s", 
        align="center",
        font=("Arial", 16, "bold")
    )


def main(speed_map: dict[str, float] | None = None) -> None:
    if speed_map is None: 
        speed_map = RUNNER_SPEEDS 

    screen = prepare_screen()
    setup_track(screen, num_lanes=len(speed_map))
    runners = create_runners(speed_map)

    countdown(screen)

    start_time = time.time()
    winner = run_race(runners)
    end_time = time.time()
    duration = end_time - start_time

    print(f"Ganador: {winner.color()[0]}")
    print(f"Tiempo total: {duration:.2f} segundos")

    show_winner_message(winner, duration)

    screen.mainloop()


if __name__ == "__main__":
    main()
