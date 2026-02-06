import turtle
import json

def draw_from_json(json_file):
    # Configurar pantalla
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(800, 800)
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    # Cargar regiones desde JSON
    with open(json_file, "r") as f:
        regions = json.load(f)

    # Obtener todos los puntos para calcular límites
    all_points = [(p[0], p[1]) for r in regions for p in r["contour"]]

    min_x = min(p[0] for p in all_points)
    max_x = max(p[0] for p in all_points)
    min_y = min(p[1] for p in all_points)
    max_y = max(p[1] for p in all_points)

    # Calcular escala y centro
    width = max_x - min_x
    height = max_y - min_y
    scale = min(600 / width, 600 / height)

    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2

    # Dibujar cada región
    for region in regions:
        r, g, b = region["color"]
        color = (r / 255, g / 255, b / 255)

        t.color(color)
        t.fillcolor(color)

        points = region["contour"]

        t.penup()
        x0 = (points[0][0] - center_x) * scale
        y0 = (center_y - points[0][1]) * scale
        t.goto(x0, y0)
        t.pendown()

        t.begin_fill()
        for point in points[1:]:
            x = (point[0] - center_x) * scale
            y = (center_y - point[1]) * scale
            t.goto(x, y)

        t.goto(x0, y0)
        t.end_fill()

    screen.update()
    screen.mainloop()


if __name__ == "__main__":
    draw_from_json("sunflowers.json")
