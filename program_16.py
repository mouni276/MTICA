lst1=[11,22,33,44,55]
lst2=[1,2,3,4,5,6,7,8]
lst3=[5,6,5,2,1,3,2,3]

print(" a:",lst1)
print(" b:",lst2)
print(" c:",lst3)

ans=list(map(lambda a,b,c:a*b+c,lst1,lst2,lst3))
print("a*b+c:",ans)
