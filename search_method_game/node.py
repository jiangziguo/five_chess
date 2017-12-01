class Node:
    def __init__(self, parent, position):
        self.parent = parent
        self.position = position
        self.alpha = float("-inf")
        self.beta = float("inf")
        self.children = []

    def set_children(self, children):
        self.children = children

    def get_children(self):
        return self.children
