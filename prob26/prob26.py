def timec(num):
    h=num/60
    m=num % 60

    return "{0}:{1}".format(h,m)

numb = 468
numb2 = 243
print timec(numb)
print timec(numb2)
