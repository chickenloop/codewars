def spin_words(sentence):
    if type(sentence) != str:
        print("This is not a string")
        sys.exit()
    else:
        listofwords = sentence.split()
        mystring=""
        for x in listofwords:
            if len(x) > 5:
                if ' ' in x == True: 
                    mystring = mystring + x[::-1]+" "
                else:
                    mystring = mystring + x[::-1]+" "
            else:
                if ' ' in x =True: 
                    mystring = mystring + x +" "
                else:
                    mystring = mystring + x + " "
    return mystring