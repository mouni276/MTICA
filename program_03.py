#find the numbers between 1-100 that are divisible by 1or2or......9

ans=[]
for i in range(1,101):
    if  i%2==0 or i%3==0 or i%4==0 or i%5==0 or i%6==0 or i%7==0 or i%8==0 or i%9==0:
        ans.append(i)
print(ans)        
 #2 nd approach
ans=[]
for i in range(1,101):
    for j in range(2,10):
        if i%j==0:
            ans.append(i)
            break
print(ans)
 #3rd approach
ans={i for i in range(1,101)for j in range(2,10)if i%j==0 }
     
print(ans)


