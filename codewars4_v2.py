def findspec(integers):
    odd=[]
    even=[]
    for i in integers:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(even)>=2:
        print(odd[0])
    else:
        print(even[0])

findspec([2,4,6,8,7,6,4,2])
findspec([1,1,3,5,7,9,11,2,3,5,7,9,9])
