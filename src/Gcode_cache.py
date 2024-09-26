import turtle
import copy
from typing import Union


class Gcode_cache:

    cache: list

    def __init__(self, t: turtle.Turtle):
        self.cache = [(False, list(t.pos()))]

    def get_gcode_of_pos(self, pendown, posx, posy):
        type_of_func = "G1" if pendown else "G0"
        return f"{type_of_func} X{posx:.3f} Y{posy:.3f}"

    def forward(self, t: turtle.Turtle, distance: Union[float, int]):
        t.forward(distance)
        self.cache.append((t.pen().get("pendown"), list(t.pos())))

    def back(self, t: turtle.Turtle, distance: Union[float, int]):
        t.back(distance)
        self.cache.append((t.pen().get("pendown"), list(t.pos())))

    def setpos(self, t: turtle.Turtle, x: Union[float, int], y: Union[float, int]):
        previous_pos = t.pos()
        t.setpos(x, y)
        (  # you said no restrictions on ternaries... these are definitely the cheesiest ones.
            self.cache.pop()
            if previous_pos != t.pos() and not self.cache[-1][0]
            else None
        )
        (
            self.cache.append((t.pen().get("pendown"), list(t.pos())))
            if previous_pos != t.pos()
            else None
        )

    def clear_cache(self, t: turtle.Turtle):
        self.cache = [[False, list(t.pos())]]

    def output_gcode(self, xbound: Union[float, int], ybound: Union[float, int]):
        while not self.cache[-1][0]:  # remove any useless movement commands at end
            self.cache.pop()
        lower_x_bound = min([pos[0] for pendown, pos in self.cache])
        lower_y_bound = min([pos[1] for pendown, pos in self.cache])
        for pendown, pos in self.cache:
            # offset so all vals are pos
            pos[0] += abs(lower_x_bound) if lower_x_bound <= 0 else 0
            pos[1] += abs(lower_y_bound) if lower_y_bound <= 0 else 0
        upper_x_bound = max([pos[0] for pendown, pos in self.cache])
        upper_y_bound = max([pos[1] for pendown, pos in self.cache])
        for pendown, pos in self.cache:
            # scale so within bounds
            pos[0] *= (
                (
                    xbound
                    if upper_x_bound > upper_y_bound
                    else (
                        xbound
                        if upper_y_bound == 0
                        else xbound * upper_x_bound / upper_y_bound
                    )
                )
                / abs(upper_x_bound)
                if upper_x_bound != 0
                else 1
            )
            pos[1] *= (
                (
                    ybound
                    if upper_y_bound > upper_x_bound
                    else (
                        ybound
                        if upper_x_bound == 0
                        else ybound * upper_y_bound / upper_x_bound
                    )
                )
                / abs(upper_y_bound)
                if upper_y_bound != 0
                else 1
            )
        output_string = []
        for pendown, pos in self.cache:
            # write output
            output_string.append(self.get_gcode_of_pos(pendown, pos[0], pos[1]))
        return "\n".join(output_string)
