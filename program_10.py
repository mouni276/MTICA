string='''practice problems for list comprehensoin in python'''
ans=[i for i in string if i not in 'AEIOUaeiou']
print(''.join(ans))
