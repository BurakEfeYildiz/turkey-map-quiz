import turtle


WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
MARK_COLOR = "red"
MARK_FONT = ("Arial", 20, "bold")
PROMPT_TITLE = "City Quiz"
PROMPT_TEXT = "What is the name of this city?"


screen = turtle.Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.bgpic("turkey_map.png")
screen.title("Turkey Map Quiz")


cities = {
    "Ankara": {"x": -132.0, "y": 60.0, "r": 20},
    "Istanbul": {"x": -301, "y": 135.0, "r": 25},
    "Izmir": {"x": -349, "y": -15, "r": 20},
}
guessed_cities = set()


def draw_check_mark(x, y):
    marker = turtle.Turtle()
    marker.hideturtle()
    marker.penup()
    marker.color(MARK_COLOR)
    marker.goto(x, y)
    marker.write("✔", align="center", font=MARK_FONT)


def is_inside_city(x, y, city):
    dx = x - city["x"]
    dy = y - city["y"]
    return dx * dx + dy * dy <= city["r"] ** 2


def get_clicked_city(x, y):
    for city_name, city_data in cities.items():
        if is_inside_city(x, y, city_data):
            return city_name, city_data
    return None, None


def on_click(x, y):
    city_name, city_data = get_clicked_city(x, y)

    if city_name is None or city_name in guessed_cities:
        return

    answer = screen.textinput(PROMPT_TITLE, PROMPT_TEXT)
    if answer is None:
        return

    if answer.strip().lower() == city_name.lower():
        guessed_cities.add(city_name)
        draw_check_mark(city_data["x"], city_data["y"])
        screen.title(f"Turkey Map Quiz - {len(guessed_cities)}/{len(cities)} cities found")

        if len(guessed_cities) == len(cities):
            screen.textinput("Completed", "Great job! You found all available cities. Press OK to close.")
            turtle.bye()


screen.onclick(on_click)
turtle.mainloop()
