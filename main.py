
from home.hw1_2 import Hero

class Air(Hero):
    two_heads = 2

    def __init__(self, name, nickname, hp, damage, fly=False):
        Hero.__init__(self, name, nickname, hp, damage)
        self.fly = fly

    def __Gen_x(self):
        pass

    def Gen_x(self, value):
        pass

    def brand_phrase(self):
        self.fly = True
        print('fly in the True_phrase')


class Graund(Hero):
    foot = 4

    def __init__(self, name, nickname, hp, damage, fly=0):
        Hero.__init__(self, name, nickname, hp, damage)
        self.fly = fly

    def __Gen_x(self):
        pass

    def brand_phrase(self):
        self.fly = True
        print('fly in the True_phrase')


class Galaxy(Hero):
    hands = 4

    def __init__(self, name, nickname, hp, damage, fly=not True):
        Hero.__init__(self, name, nickname, hp, damage)
        self.fly = fly

    def __Gen_x(self):
        pass

    def brand_phrase(self):
        self.fly = True
        print('fly in the True_phrase')

