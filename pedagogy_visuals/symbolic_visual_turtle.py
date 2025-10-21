# symbolic_visual_turtle.py
import turtle

def draw_polynomial(coeffs, scale=10):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    for x in range(-100, 100):
        y = sum(c * (x / scale)**i for i, c in enumerate(coeffs))
        t.goto(x, y)
        t.pendown()
    turtle.done()

# Example: draw_polynomial([1, -2, 3])  # Represents 3x² - 2x + 1
