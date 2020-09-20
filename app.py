import random

number_table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
newline = []
clone_table = number_table
for element in range(len(number_table)):
    picked_element = random.choice(clone_table)
    newline.append(picked_element)
    clone_table.remove(picked_element)


print(newline)
for i in range(6):
    # print(random.randint(1, 6))
    pass

members = ["Lu", "Mosh", "Lee", "Andy", "Ken"]

for i in range(10):
    # print(random.choice(members))
    pass


class Dice:
    def __init__(self, sides, tries):
        self.sides = sides
        self.tries = tries

    def roll(self):
        streak = []
        for ii in range(self.tries):
            streak.append(random.randint(1, self.sides))

        tup = tuple(streak)
        return tup


kauliukas = Dice(16,4)

print(kauliukas.roll())
