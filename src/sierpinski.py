from src.ifs import ifs
import turtle
from typing import Union

draw_turtle = turtle.Turtle()
draw_turtle.speed(0)


def halve_distance(data_dict):
    data_dict["distance"] = data_dict["distance"] / 2
    return "H"


def draw_forward_A(data_dict):
    distance = data_dict.get("distance")
    draw_turtle.forward(distance)
    return "B-A-B"


def draw_forward_B(data_dict):
    draw_forward_A(data_dict)
    return "A+B+A"


def turn_left(data_dict):
    angle = data_dict.get("angle")
    draw_turtle.left(angle)
    return ""


def turn_right(data_dict):
    angle = data_dict.get("angle")
    draw_turtle.right(angle)
    return ""


def create_sierpinski_ifs(distance: Union[int, float], angle: Union[int, float] = 60):
    data_dict = {"distance": distance, "angle": angle}
    function_dict = {
        "H": halve_distance,
        "A": draw_forward_A,
        "B": draw_forward_B,
        "-": turn_right,
        "+": turn_left,
    }
    return ifs("AH", function_dict, data_dict)
