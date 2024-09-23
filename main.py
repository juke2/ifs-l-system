import src.ifs as ifs
import src.sierpinski as sier

"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""


import turtle
from src.Lsystem import Lsystem

instructions = {
    "G": lambda t, dist: t.forward(dist),
    "F": lambda t, dist: t.forward(dist),
    "-": lambda t, dist: t.right(120),
    "+": lambda t, dist: t.left(120),
}
start = "F-G-G"
rules = {"F": "F-G+F+G-F", "G": "GG", "-": "-", "+": "+"}
items = {"t": turtle.Turtle(), "dist": 200}
items["t"].speed(0)


def defaultMutator(**kwargs):
    return kwargs


def sierpinskiMutator(**kwargs):
    kwargs.update({"dist": kwargs.get("dist") / 2})
    return kwargs


# import turtle

# t = turtle.Turtle()

# # for c in ['red', 'green', 'blue', 'yellow']:
# #     t.color(c)
# #     t.forward(75)
# #     t.left(90)

# dist = 100
# angle = 120
# F = lambda : t.forward(dist)
# left = lambda : t.left(angle)
# G = lambda : t.forward(dist)
# right = lambda : t.right(angle)

# s = [ 'F-G-G' ]
# rules = {
#   'F':'F-G+F+G-F',
#         'G':'GG'
# }
# interpretations = {
#   'F':lambda : t.forward(dist),
#   'G':lambda : t.forward(dist)
# }

# F()
# left()
# G()
# left()
# G()

# t.setheading(0)
# dist /= 2
# F()
# left()
# G()
# right()
# F()
# right()
# G()
# left()
# F()
# left()
# G()
# G()
# left()
# G()
# G()


# Code up an IFS for Serpinski's and others with the same partner as before.
# The partner who has done the least work on the previous project is required
# to take up the mantle for this one.
# Additional Challenge: use nary an if-block
#
# def interpret(current: str, mappings: dict) -> None
# def nextGeneration(current: str, genRules: dict) -> str
def main() -> None:
    sier_ifs = sier.create_sierpinski_ifs(100)
    sier_ifs.iterate(5)
    sier.draw_turtle.screen.mainloop()
    pass


if __name__ == "__main__":
    main()
