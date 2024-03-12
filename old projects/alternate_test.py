s = (input("Write a String = "))

ss = ''.join([x.lower() if i%2 else x.upper() for i,x in enumerate(s)])
print(ss)
    
    #iteration over a range until 10
#range not defined to start at 1 rather than 0
#product is initially 10*0 = 0
#each subsequent product is then multiplying 0
#giving 0 as each result rather than a series of products multiplying each previous result by a number from 1 - 10
