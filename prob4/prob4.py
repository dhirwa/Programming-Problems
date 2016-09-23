from random import randrange


def generateList(num):
    array = []

    for x in range(0, num + 1):
        if x % 2 == 0:
            array.append(x)
    return array

rand_num = randrange(100)
print("The number is {0}".format(rand_num))
print(generateList(rand_num))
