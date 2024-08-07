class Animatronic():

    position = '1a'
    level = 0
    def setPosition(self, new_positon):
        self.position = new_positon

    def setLevel(self, new_level):
        self.level = new_level

    def printPosition(self):
        print(self.position)


class Foxy(Animatronic):
    stage = 0
    sprite = 1

    def setStage(self, new_stage):
        self.stage = new_stage
