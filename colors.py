import random

class Colors:
    Blue = [(63,110,181), (57, 101, 166), (59,103,170), (50,87,144)] 
    Red = [(164,65,45), (189,75,52), (197,78,54), (201,80,55)]
    Yellow = [(218,162,51), (228,170,54), (252,188,60), (241,180,57)]
    Green = [(98,158,72), (107,171,78), (114,183,84), (109,175,80)]

    color_dict = {"Blue": Blue, "Red": Red, "Yellow": Yellow, "Green": Green}

    @classmethod
    def return_color(cls, col):
        return random.choice(cls.color_dict[col])