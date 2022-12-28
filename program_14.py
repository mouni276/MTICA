#using lambda function 
lst1=[11,22,33,44,55]
lst2=[1,2,3,4,5]
def add(a,b):
    return a+b
ans=list(map(add,lst1,lst2))
print(lst1)
print(lst2)
print('-'*40)
ans=list(map(lambda a,b:a+b,lst1,lst2))

print(ans)
