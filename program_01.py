#use a dictionary comprehensoin,to count the length of each word in a sentence
string='''practice problems for list comprehension in python'''
wordslst=string.split(' ')
print(wordslst)
wordslst=[i.strip("\n") for i in wordslst ]
ans={i:len(i) for i in wordslst }
print(ans)
