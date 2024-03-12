String = input("Write a string: ")
New_String = ""
#New_String = ''.join([''.join(char.upper() if i%2 == 0 else char.lower() for i, char in enumerate(word)) for word in string.split()])
Case = []

for i, char in enumerate(String):
    if i%2 == 0:
        New_String = "".join(char.upper())
        #print(New_String)
        Case.append(New_String)
    else:
        New_String = "".join(char.lower())
        #print(New_String)
        Case.append(New_String)
    New_String = "".join(Case)

print(New_String)

Case2 = []
Word_String = ""


for i, word in enumerate(String.split()):

    if i%2 == 0:
        Word_String = (word.upper())
        # print(Word_String)
        Case2.append(Word_String)

    else:
        Word_String = (word.lower())
        #print(Word_String)
        Case2.append(Word_String)
    
    Word_String = " ".join(Case2)

print(Word_String)
