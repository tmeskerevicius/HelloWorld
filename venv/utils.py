def find_max(list):
    max = list[0]
    for element in list:
        if element > max:
            max = element
    return max
