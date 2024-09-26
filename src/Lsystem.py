import copy
from turtle import Turtle
from typing import Optional
import tkinter
import inspect


class Lsystem:

    def __init__(
        self,
        start: str,
        rules: dict,
        actions: dict,
        actionsInput: dict = dict(),
        mutatorByIteration=lambda **kwargs: kwargs,
        delayRun: bool = False,
        mode: Optional[str] = None,
    ):
        self.rules = rules
        self.actions = actions
        self.mutatorByIteration = mutatorByIteration
        self.delayRun = delayRun
        self.processedStrings = [start]
        self.actionsInput = actionsInput
        self.mode = mode
        self.functions = {
            None: self.next_process_string,
            "functional": self.next_process_string_functional,
        }

    def __getitem__(self, i):
        """returns the ith process string"""
        return self.processString(i)

    def processString(self, i: int) -> str:
        """process states and returns the ith state such that i=0 --> initial state. caches process states as well"""
        for index in range(len(self.processedStrings), i + 1):
            previous_string = self.processedStrings[index - 1]
            self.processedStrings.append(self.functions.get(self.mode)(previous_string))
        return self.processedStrings[i]

    def next_process_string_functional(self, previous_iteration: str):
        next_process_string = []
        for pos, character in enumerate(previous_iteration):
            next_process_string.append(
                self.rules.get(character)(pos, previous_iteration)
            )
        return "".join(next_process_string)

    def next_process_string(self, previous_iteration: str):
        next_process_string = []
        for character in previous_iteration:
            next_process_string.append(self.rules.get(character))
        return "".join(next_process_string)

    def run(self, i: int = -1):
        """runs the ith iteration -- defaults to last"""
        actionsInput = {}
        for key, value in self.actionsInput.items():
            try:
                actionsInput[copy.deepcopy(key)] = copy.deepcopy(value)
            except TypeError as e:
                actionsInput[key] = value
        # had to remove my pretty dict comp because of the gcode implementation having non-copyable types... I am very sad
        for iteration in range(0, i if i > 0 else range(len(self.processedStrings))[i]):
            actionsInput = self.mutatorByIteration(**actionsInput)
        for character in self.processString(i):
            self.actions.get(character)(**actionsInput)

        # actionsInput = {
        #         copy.deepcopy(key): copy.deepcopy(value)
        #         for key, value in self.actionsInput.items()
        # }
        #
