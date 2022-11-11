from Intermediaite.day20_21.snake_game.inherit.animal import Animal


class Fish(Animal):


    def __init__(self):
        super().__init__()
        self.form = "Form"

    def rename(self):
        self.name = "New Name"
    def __str__(self):
        print(self.eat_mode())
        print(self.sleep_mode())
        self.rename()

