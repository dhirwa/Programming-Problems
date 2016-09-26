def spiral(arr):
    test=[]
    for x in arr:
        for y in x:
            test.append(y)
    return sorted(test)
array=[[1,2,9],[8,3,6],[7,4,5]]
print spiral(array)
