
def par_to_array(par):
    array=[]

    d=par.split(" ")
    array.append(d)
    return array

para="Write a function that takes a paragraph as an argument and returns an array that contains each string as an element."
print(par_to_array(para))
