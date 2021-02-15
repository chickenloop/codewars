def findspec(integers):
    odd=0
    even=0
    for i in integers:
        if i%2 == 0:
            even+=1
        else:
            odd+=1
    if even > 2:
        for i in integers:
            if i%2 != 0:
                print(i)
                break
    else:
        for i in integers:
            if i%2 ==0:
                print(i)
                break
findspec([2,4,6,8,7,6,4,2])
findspec([1,1,3,5,7,9,11,2,3,5,7,9,9])
