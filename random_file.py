import random


class RandomName:
    def __init__(self, name_list):
        self.name_list = name_list

    def return_name(self):
        name = ""
        if len(self.name_list) == 0:
            return False
        for i in range(random.randint(1, len(self.name_list))):
            name = self.name_list[i]
        return name
