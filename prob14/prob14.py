from random import randrange

def calc_power(num1,num2):
    total=1
    for i in range(0,num2):
        total*=num1
    return total

numb1=randrange(10)
numb2=randrange(10)

print "The numbers are {0} and {1}".format(numb1,numb2)
print "{0} power {1} equals ".format(numb1,numb2)
print(calc_power(numb1,numb2))
