string = "this is a string"
New_String = ""
#New_String = ''.join([''.join(char.upper() if i%2 == 0 else char.lower() for i, char in enumerate(word)) for word in string.split()])
Case = []
for word in string.split():
    for i, char in enumerate(word):
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