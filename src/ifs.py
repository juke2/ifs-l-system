class Lsystem:
    def __init__(
        self,
        start,
        rules,
        actions,
        actionsInput=dict(),
        mutatorByIteration=lambda **kwargs: kwargs,
        delayRun=False,
    ):
        self.rules = rules
        self.actions = actions
        self.mutatorByIteration = mutatorByIteration
        self.delayRun = delayRun
        self.processedStrings = [start]
        self.actionsInput = actionsInput

        def __getitem__(self, i):
            """returns the ith process string"""
            return self.processString(i)

        def processString(self, i):
            """process states and returns the ith state such that i=0 --> initial state. caches process states as well"""

        def run(self, i=-1):
            """runs the ith iteration -- defaults to last"""
