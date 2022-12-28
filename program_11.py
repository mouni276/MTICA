string='''practice problems for list comprehensoin in python'''
wordsList=string.split(' ')
ans=[i for i in wordsList if len(i.strip('\n'))==8 ]
print(*ans)
