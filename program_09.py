#to remove digits in the given string
string=input()
ans=[i for i in string if i in '0123456789']
print(ans)
#to remove vowels in the string
string='''practice problems for list comprehensoin in python'''
ans=[]
for i in string:
    if i not in 'AEIOUaeiou':
        ans.append(i)
print(*ans)
