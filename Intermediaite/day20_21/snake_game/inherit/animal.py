
class Animal:
    name = None

    def __init__(self):
        self.name = None
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")
    def eat_mode(self):
        return "Eat"

    def sleep_mode(self):
        return "Sleep"