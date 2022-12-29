#use a dictionary comprehensoin,to reverse the string
string='''practice problems for list comprehension in python'''
wordslst=string.split(' ')
wordslst=[i.strip("\n") for i in wordslst ]
ans={i:i[::-1] for i in wordslst }
print(ans)
