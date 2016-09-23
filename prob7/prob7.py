def getdisc(total,perc):
    if perc > 100 or perc < 0:
        print "Invalid percentage"
    else:
        disc=total*(perc * .01)
        return round(disc, 2)

print(getdisc(200, 40))
