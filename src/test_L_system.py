import turtle_gcode as turtle
import random
from src.Lsystem import Lsystem
from pathlib import Path
from src.Gcode_cache import Gcode_cache


def defaultMutator(**kwargs):
    return kwargs


def sierpinskiMutator(**kwargs):
    kwargs.update({"dist": kwargs.get("dist") / 2})
    return kwargs


def cantorMutator(**kwargs):
    kwargs.update({"length": kwargs.get("length") * 3})
    return kwargs


def test_sierpinski():
    items = {"t": turtle.Turtle(), "dist": 200}
    items["t"].speed(0)
    gc = Gcode_cache(items["t"])
    instructions = {
        "G": lambda t, dist: gc.forward(t, dist),
        "F": lambda t, dist: gc.forward(t, dist),
        "-": lambda t, dist: t.right(120),
        "+": lambda t, dist: t.left(120),
    }
    start = "F-G-G"
    rules = {"F": "F-G+F+G-F", "G": "GG", "-": "-", "+": "+"}
    sierpinski_L_System = Lsystem(
        start=start,
        rules=rules,
        actions=instructions,
        actionsInput=items,
        mutatorByIteration=sierpinskiMutator,
    )
    items["t"].setheading(180)
    sierpinski_L_System.run(5)
    assert items["t"].write_gcode(10, 10) == gc.output_gcode(10, 10)
    with open(
        Path(__file__)
        .parent.resolve()
        .joinpath("gcode_output", "output_sierpinski.gcode"),
        "w+",
        encoding="utf-8",
    ) as file:
        file.write(gc.output_gcode(10, 10))


def test_binary_tree():
    items = {"t": turtle.Turtle(), "store": []}
    items["t"].speed(0)
    gc = Gcode_cache(items["t"])
    instructions = {
        "0": lambda t, store: (
            gc.forward(t, 5),
            t.right(30),
            gc.forward(t, 2),
            gc.back(t, 2),
            t.left(60),
            gc.forward(t, 2),
            gc.back(t, 2),
            t.right(30),
            gc.back(t, 5),
        ),
        "1": lambda t, store: gc.forward(t, 8),
        "[": lambda t, store: (
            store.append({"x": t.xcor(), "y": t.ycor(), "angle": t.heading()}),
            t.left(45),
        ),
        "]": lambda t, store: (
            t.penup(),
            gc.setpos(
                t, store[len(store) - 1].get("x"), store[len(store) - 1].get("y")
            ),
            t.pendown(),
            t.seth(store[len(store) - 1].get("angle")),
            store.pop(len(store) - 1),
            t.right(45),
        ),
    }
    start = "0"
    rules = {
        "1": "11",
        "0": "1[0]0",
        "[": "[",
        "]": "]",
    }

    binary_tree_L_System = Lsystem(
        start=start,
        rules=rules,
        actions=instructions,
        actionsInput=items,
        mutatorByIteration=defaultMutator,
    )
    binary_tree_L_System.run(5)
    assert items["t"].write_gcode(10, 10) == gc.output_gcode(10, 10)
    with open(
        Path(__file__)
        .parent.resolve()
        .joinpath("gcode_output", "output_binary_tree.gcode"),
        "w+",
        encoding="utf-8",
    ) as file:
        file.write(gc.output_gcode(10, 10))


def test_sierpinski_arrowhead():
    items = {"t": turtle.Turtle(), "dist": 200}
    items["t"].speed(0)
    gc = Gcode_cache(items["t"])
    instructions = {
        "A": lambda t, dist: gc.forward(t, dist),
        "B": lambda t, dist: gc.forward(t, dist),
        "-": lambda t, dist: t.right(60),
        "+": lambda t, dist: t.left(60),
    }
    start = "A"
    rules = {"A": "B-A-B", "B": "A+B+A", "-": "-", "+": "+"}

    sierpinski_L_System = Lsystem(
        start=start,
        rules=rules,
        actions=instructions,
        actionsInput=items,
        mutatorByIteration=sierpinskiMutator,
    )
    sierpinski_L_System.run(4)
    assert items["t"].write_gcode(10, 10) == gc.output_gcode(10, 10)
    with open(
        Path(__file__)
        .parent.resolve()
        .joinpath("gcode_output", "output_sierpinski_arrowhead.gcode"),
        "w+",
        encoding="utf-8",
    ) as file:
        file.write(gc.output_gcode(10, 10))


def test_dragon_curve():
    items = {"t": turtle.Turtle(), "dist": 10}
    items["t"].speed(0)
    gc = Gcode_cache(items["t"])
    instructions = {
        "F": lambda t, dist: gc.forward(t, dist),
        "G": lambda t, dist: gc.forward(t, dist),
        "-": lambda t, dist: t.right(90),
        "+": lambda t, dist: t.left(90),
    }
    start = "F"
    rules = {"F": "F+G", "G": "F-G", "-": "-", "+": "+"}

    dragon_curve_L_System = Lsystem(
        start=start,
        rules=rules,
        actions=instructions,
        actionsInput=items,
        mutatorByIteration=defaultMutator,
    )
    dragon_curve_L_System.run(7)
    assert items["t"].write_gcode(10, 10) == gc.output_gcode(10, 10)
    with open(
        Path(__file__)
        .parent.resolve()
        .joinpath("gcode_output", "output_dragon_curve.gcode"),
        "w+",
        encoding="utf-8",
    ) as file:
        file.write(gc.output_gcode(10, 10))


def test_fractal_plant():
    items = {"t": turtle.Turtle(), "store": []}
    items["t"].speed(0)
    gc = Gcode_cache(items["t"])
    instructions = {
        "X": lambda t, store: "",
        "F": lambda t, store: gc.forward(t, 5),
        "-": lambda t, store: t.right(25),
        "+": lambda t, store: t.left(25),
        "[": lambda t, store: store.append(
            {"x": t.xcor(), "y": t.ycor(), "angle": t.heading()}
        ),
        "]": lambda t, store: (
            t.penup(),
            gc.setpos(
                t, store[len(store) - 1].get("x"), store[len(store) - 1].get("y")
            ),
            t.pendown(),
            t.seth(store[len(store) - 1].get("angle")),
            store.pop(),
        ),
    }
    start = "X"
    rules = {
        "X": "F+[[X]-X]-F[-FX]+X",
        "F": "FF",
        "-": "-",
        "+": "+",
        "[": "[",
        "]": "]",
    }
    fractal_plant_L_System = Lsystem(
        start=start,
        rules=rules,
        actions=instructions,
        actionsInput=items,
        mutatorByIteration=defaultMutator,
    )
    fractal_plant_L_System.run(3)
    assert items["t"].write_gcode(10, 10) == gc.output_gcode(10, 10)
    with open(
        Path(__file__)
        .parent.resolve()
        .joinpath("gcode_output", "output_fractal_plant.gcode"),
        "w+",
        encoding="utf-8",
    ) as file:
        file.write(items["t"].write_gcode(10, 10))


def test_stochastic_system():
    items = {"t": turtle.Turtle()}
    items["t"].speed(0)
    gc = Gcode_cache(items["t"])
    instructions = {
        "A": lambda t: gc.forward(t, 5),
        "-": lambda t: t.right(45),
        "+": lambda t: t.left(45),
    }
    start = "A"
    rules = {
        "A": lambda pos, context: "-AA" if random.randrange(0, 2) == 0 else "+AA",
        "-": lambda pos, context: "-",
        "+": lambda pos, context: "+",
    }

    stochastic_L_System = Lsystem(
        start=start,
        rules=rules,
        actions=instructions,
        actionsInput=items,
        mutatorByIteration=defaultMutator,
        mode="functional",
    )
    stochastic_L_System.run(5)
    assert items["t"].write_gcode(10, 10) == gc.output_gcode(10, 10)
    with open(
        Path(__file__)
        .parent.resolve()
        .joinpath("gcode_output", "output_stochastic.gcode"),
        "w+",
        encoding="utf-8",
    ) as file:
        file.write(gc.output_gcode(10, 10))


def test_context_aware_system():
    items = {"t": turtle.Turtle()}
    items["t"].speed(0)
    gc = Gcode_cache(items["t"])
    instructions = {
        "A": lambda t: gc.forward(t, 5),
        "B": lambda t: gc.forward(t, 10),
        "-": lambda t: t.right(45),
        "+": lambda t: t.left(45),
    }
    start = "A"
    rules = {
        "A": lambda pos, context: (
            "A+B"
            if (context[pos + 1] if pos + 1 < len(context) else "") != "B"
            else "A-"
        ),
        "B": lambda pos, context: (
            "B-A"
            if (context[pos + 1] if pos + 1 < len(context) else "") != "A"
            else "B+"
        ),
        "-": lambda pos, context: "-",
        "+": lambda pos, context: "+",
    }

    context_aware_L_System = Lsystem(
        start=start,
        rules=rules,
        actions=instructions,
        actionsInput=items,
        mutatorByIteration=defaultMutator,
        mode="functional",
    )
    context_aware_L_System.run(5)
    assert items["t"].write_gcode(10, 10) == gc.output_gcode(10, 10)
    with open(
        Path(__file__)
        .parent.resolve()
        .joinpath("gcode_output", "output_context_aware.gcode"),
        "w+",
        encoding="utf-8",
    ) as file:
        file.write(gc.output_gcode(10, 10))


def test_cantor_set():
    items = {"t": turtle.Turtle(), "dist": 200, "length": 1}
    items["t"].speed(0)
    gc = Gcode_cache(items["t"])
    instructions = {
        "A": lambda t, dist, length: gc.forward(t, dist / length),
        "B": lambda t, dist, length: (
            t.penup(),
            gc.forward(t, dist / length),
            t.pendown(),
        ),
    }
    start = "A"
    rules = {"A": "ABA", "B": "BBB"}
    cantor_L_System = Lsystem(
        start=start,
        rules=rules,
        actions=instructions,
        actionsInput=items,
        mutatorByIteration=cantorMutator,
    )
    cantor_L_System.run(5)
    # assert items["t"].write_gcode(10, 10) == gc.output_gcode(10, 10)
    # this test actually breaks the library I am using to test... uh whoops... (a straight line in the x plane)
    with open(
        Path(__file__).parent.resolve().joinpath("gcode_output", "output_cantor.gcode"),
        "w+",
        encoding="utf-8",
    ) as file:
        file.write(gc.output_gcode(10, 10))


def test_koch_curve():
    items = {"t": turtle.Turtle(), "dist": 5}
    items["t"].speed(0)
    gc = Gcode_cache(items["t"])
    instructions = {
        "F": lambda t, dist: gc.forward(t, dist),
        "-": lambda t, dist: t.right(90),
        "+": lambda t, dist: t.left(90),
    }
    start = "F"
    rules = {"F": "F+F-F-F+F", "-": "-", "+": "+"}

    koch_curve_L_System = Lsystem(
        start=start,
        rules=rules,
        actions=instructions,
        actionsInput=items,
        mutatorByIteration=defaultMutator,
    )
    koch_curve_L_System.run(4)
    assert items["t"].write_gcode(10, 10) == gc.output_gcode(10, 10)
    with open(
        Path(__file__)
        .parent.resolve()
        .joinpath("gcode_output", "output_koch_curve.gcode"),
        "w+",
        encoding="utf-8",
    ) as file:
        file.write(gc.output_gcode(10, 10))
