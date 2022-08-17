import random

class Probabilidad:
    pass

class Tree:

    def __init__(self):
        self.id = random.randint(0,1000)

    def __str__(self):
        return f"Tree{self.id}"