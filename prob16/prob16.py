from random import randrange
import os

def rand_st(num):
    #text=""
    #letters="abcdefghijklmnopqrstuvwxyz"
    text = os.urandom(num)
    #for i in range(0,num):
        #if text.length<num:
        #    text=text+letters.random()

    return text

def char_t(s1,s2):
    if s1[0:1] == s2[0:1]:
        print "true"
    else:
        print "false"

ss1=rand_st(10)
ss2=rand_st(10)

print "Strings are {0} and {1}".format(ss1,ss2)
print(char_t(ss1,ss2))
