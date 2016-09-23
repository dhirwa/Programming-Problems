def key(dict):
    values=list(dict.values())
    keys=list(dict.keys())
    return keys[values.index(max(values))]

people= {"mike":30, "jack":22, "frank":16,"karl":19,"matt":47}
print "The oldest person is " + str(key(people))
