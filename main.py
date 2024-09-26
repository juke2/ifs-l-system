import turtle_gcode as turtle
from src.test_L_system import *


def main() -> None:
    test_sierpinski()
    test_sierpinski_arrowhead()
    test_dragon_curve()
    test_fractal_plant()
    for iteration in range(0, 10):
        test_stochastic_system()
    test_context_aware_system()
    test_binary_tree()
    test_cantor_set()
    test_koch_curve()
    turtle.mainloop()


if __name__ == "__main__":
    main()

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
