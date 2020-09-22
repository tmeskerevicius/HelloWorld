import random

number_table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
newline = []
listoflines = []
covers = []
numberOfCoversNeeded = 10
linesNeededToCoverTable = 8
numbersinline = 5
linestocoverfulltable = 5
clone_table = number_table
for coverNo in range(numberOfCoversNeeded):
    for element in range(linesNeededToCoverTable):
        if len(clone_table) == 0:
            break
        for onenumber in range(numbersinline):
            if len(clone_table) == 0:
                break
            picked_element = random.choice(clone_table)
            newline.append(picked_element)
            clone_table.remove(picked_element)
        newline.sort()
        listoflines.append(newline)
        newline = []
    listoflines.sort()
    covers.append(listoflines)

print("All covers : ", covers)
