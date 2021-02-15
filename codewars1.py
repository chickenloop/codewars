import sys
def spinWords(playstring):
    #Check if the paramter is a string, if not exit
    if type(playstring) != str:
        print("This is not a string")
        sys.exit()
    else:
        listofwords = playstring.split()
        mystring=""
        for x in listofwords:
        #print(x)
            if len(x) > 5:
                mystring = mystring +" "+ x[::-1]               
            else:
                mystring = mystring +" "+ x 
        print(mystring)   

spinWords("Hey fellow warriors")
