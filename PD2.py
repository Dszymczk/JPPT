# JPPT - praca domowa
# Damian Szymczyk


def get_dividers(number):
    dividers_list = []
    for i in range(number - 1):
        if number % (i + 1) == 0:
            dividers_list.append(i + 1)
    return dividers_list


def is_perfect(number):
    if number == 0:
        return False
    if number == sum(get_dividers(number)):
        return True
    else:
        return False


numbers = list(range(500))
NewList = [(is_perfect(i), i) for i in numbers]
print(NewList)
