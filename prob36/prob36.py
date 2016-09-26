def countZeros(stri):
    count=0

    for i in stri:
        if stri[i] == 0:
            count=count + 1
        else:
            count=count + 0
    return count

print "{0}".format(countZeros([0,0,0,1,1,2,4,0]))
