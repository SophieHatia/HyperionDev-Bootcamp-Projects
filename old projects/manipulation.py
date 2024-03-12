str_manip=input("Write a sentence: ")
print(len(str_manip))
Len=len(str_manip)
print(str_manip[len(str_manip)-1])
str2= str_manip.replace(str_manip[len(str_manip)-1],"@")
print(str2)

str3=str_manip[len(str_manip)-1:len(str_manip)-4:-1]
print(str3)
str_word_start=str_manip[0:3]
str_word_end=str_manip[len(str_manip)-2:len(str_manip):1]
print(str_word_start+str_word_end)