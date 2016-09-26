def longest_word(stri):
    array=stri.split(' ')
    maxi=""
    for i in stri:
        if array[i].length > maxi.length :
            maxi =  array[i]

    return maxi


strng="hsjdjhjhcj jdhjc jhdjdchjchdjchjd ejhdc sdhjd dh"
print "The longest string is {0}".format(longest_word(strng))
