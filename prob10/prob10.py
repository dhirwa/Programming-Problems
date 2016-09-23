from random import randrange

def sum(num):
    total=0;
    for i in str(num):
        total=total+int(i)
    return total

numb=randrange(1000,9999)
print "The number is " + str(numb)
print "The sum is "+ str(sum(numb))
