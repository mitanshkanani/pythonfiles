
#taking word
word=input("Enter the word:")
print("word before cyphering:"+word)
#taking shift length
length=int(input("Enter the shift lengt:"))
print(length)
#converting ito list
listmain=[ord(ch) for ch in word]
#print(listmain)
listb=[x+length for x in listmain]
#print(listb)
listc=[chr(ch) for ch in listb]
#print(listc)
x=''.join(listc)
print("cyphered text is :"+x)

# for decyphering
listdecypher=[x-length for x in listb]
print(listdecypher)

listdecypher2=[chr(ch) for ch in listdecypher]
y=''.join(listdecypher2)
print("decyphered list is:"+y)