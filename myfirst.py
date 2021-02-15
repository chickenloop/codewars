# example imput [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]

def open_or_senior(data):
    
    membertype = []
    mystr=""
    for x in data:
        if x[0] >=54 and x[1]>=7:
            membertype.append("senior")
        else:
            membertype.append("open")
    return print(membertype)

open_or_senior([[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]])