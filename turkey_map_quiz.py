import turtle

screen = turtle.Screen()
screen.setup(width=900, height=700)
screen.bgpic("turkey_map.png")
screen.title("Turkey Map Quiz")

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()


cities = {
    "Ankara": {"x": -132.0, "y": 60.0, "r": 20},
    "Istanbul": {"x": -301, "y": 135.0, "r": 25},
    "Izmir": {"x": -349, "y": -15, "r": 20}
}

# def on_click(x, y):
#     print(x, y)

def draw_check_mark(x, y):
    marker = turtle.Turtle()
    marker.hideturtle()
    marker.penup()
    marker.color("red")
    marker.goto(x, y)
    marker.write("✔", align="center", font=("Arial", 20, "bold"))

def is_inside_city(x, y, city):
    dx = x - city["x"]
    dy = y - city["y"]
    return dx*dx + dy*dy <= city["r"]**2

def get_clicked_city(x, y):
    for city_name, city_data in cities.items():
        if is_inside_city(x, y, city_data):
            return city_name, city_data
    return None, None

def on_click(x, y):
    city_name, city_data = get_clicked_city(x, y)

    if city_name is None:
        return

    answer = screen.textinput("Şehir Bul", "Bu şehrin adı nedir?")

    if answer is None:
        return

    if answer.strip().lower() == city_name.lower():
        draw_check_mark(city_data["x"], city_data["y"])


screen.onclick(on_click)
turtle.mainloop()
