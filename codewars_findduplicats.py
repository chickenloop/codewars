def duplicate_count(mytext):
    # Your code goes heredef
    myval=[]
    mydict={}
    counter = 0
    for x in mytext:
        mydict[x]=mytext.lower.count(x)
    
    for i in mydict:
        if mydict.get(i) > 1:
           counter=counter+1
    return counter

print(duplicate_count("abcccddee"))
