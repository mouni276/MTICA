#to count how many times 'a' is repeated
string='''practice problems for list comprehensoin in python'''
print(string.count('a'))
#extract vowels 
string=input()
ans=[]
for i in string:
    if i in 'AEIOUaeiou':
        ans.append(i)
print(*ans)
# to find length and extract vowels
string=input('enter the text:')
ans=[i for i in string if i in 'AEIOUaeiou']
print(ans)
print('length is:',len(ans))
print(*ans)

