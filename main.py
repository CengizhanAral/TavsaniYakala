import turtle
import random

# Oyun Ayarları
screen_width = 900 # Ekran genişliği
screen_height = 600 # Ekran yüksekliği
duration = 20 # Saniye cinsinden oyun süresi
max_speed = 40 # Tavşanın maksimum hızı (px/s)

screen = turtle.Screen()
screen.title("Tavşanı Yakala")
screen.bgcolor("#87CEEB")
screen.setup(width=screen_width, height=screen_height)
screen.tracer(0)

rabbit_shape = (
    (-8, 20), (-9, 35), (-8, 48), (-6, 55), (-4, 48),
    (-5, 35), (-4, 25), (-4, 25), (-2, 28), (0, 30),
    (2, 28), (4, 25), (4, 25), (5, 35), (4, 48),
    (6, 55), (8, 48), (9, 35), (8, 20), (8, 15),
    (12, 5), (14, -5), (12, -15), (8, -20), (0, -25),
    (-8, -20), (-12, -15), (-14, -5), (-12, 5), (-8, 15),
    (-8, 20)
)
screen.register_shape("rabbit", rabbit_shape)

rabbit = turtle.Turtle()
rabbit.shape("rabbit")
rabbit.color("#A9A9A9", "#FFFFFF")
rabbit.shapesize(1.4)
rabbit.penup()
rabbit.speed(0)

score_writer = turtle.Turtle(visible=False)
score_writer.penup()
score_writer.color("black")
score_writer.goto(0, screen_height / 2 - 50)

timer_writer = turtle.Turtle(visible=False)
timer_writer.penup()
timer_writer.color("darkred")
timer_writer.goto(0, screen_height / 2 - 80)

game_over_writer = turtle.Turtle(visible=False)
game_over_writer.penup()
game_over_writer.color("darkblue")

score = 0
game_is_over = False


def update_score_display():
    score_writer.clear()
    score_writer.write(f"Puan: {score}", align="center", font=("Arial", 20, "bold"))


def update_timer_display():
    timer_writer.clear()
    timer_writer.write(f"Süre: {duration}", align="center", font=("Arial", 16, "normal"))


def handle_click(x, y):
    global score
    if not game_is_over:
        score += 1
        update_score_display()


def move_rabbit():
    if game_is_over:
        return

    turn_angle = random.randint(-60, 60)
    move_distance = random.randint(round(max_speed/3), max_speed)

    rabbit.right(turn_angle)
    rabbit.forward(move_distance)

    x, y = rabbit.pos()
    half_width = screen_width / 2 - 50
    half_height = screen_height / 2 - 50

    if not (-half_width < x < half_width and -half_height < y < half_height):
        rabbit.backward(move_distance * 1.5)
        rabbit.setheading(rabbit.towards(0, 0))

    screen.update()
    screen.ontimer(move_rabbit, 60)


def countdown():
    global duration, game_is_over
    if duration > 0:
        duration -= 1
        update_timer_display()
        screen.ontimer(countdown, 1000)
    else:
        game_is_over = True
        end_game()


def end_game():
    timer_writer.clear()
    rabbit.goto(0, -40)
    rabbit.setheading(90)

    game_over_writer.goto(0, 40)
    game_over_writer.write("Oyun Bitti!", align="center", font=("Arial", 32, "bold"))
    screen.update()


update_score_display()
update_timer_display()
rabbit.onclick(handle_click)
move_rabbit()
countdown()
screen.mainloop()
