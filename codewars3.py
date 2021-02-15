import re

test=" "
mystr2 = "AWUBBWUBC"
mystr3 = "AWUBWUBWUBBWUBWUBWUBC"
#test=mystr3.replace("WUB"," ")
#print(re.sub(' +', ' ', test))

print(re.sub(' +', ' ', mystr2.replace("WUB"," ")))