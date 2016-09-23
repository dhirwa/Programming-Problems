from random import randrange

def triangle(num):
    for i in range(1,num+1):
        print("*" * i +'\n')
        #print()

numb=randrange(10)
print(triangle(numb))
print "The number is " +str(numb)
