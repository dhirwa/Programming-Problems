from random import randrange



def generateList(num):
    arrayy=[]
    array=[]
    if num > 40:
        for i in range(40, num+1):
            if i % 2 !=0:
                arrayy.append(i)
        return arrayy
    else:
        for i in range(0,num+1):
            if i % 2 !=0:
                array.append(i)
        return array

def reverse(lst):
    reverse_list = []
    for i in reversed(lst):
        reverse_list.append(i)
    return reverse_list

numb = randrange(100)
print("number is {0}".format(numb))
print(reverse(generateList(numb)))
