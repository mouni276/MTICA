#to find the highest single digit any of the numbers is divisible by 
ans=[]
for i in range(100,111):
    temp=[]
    for j in range(1,11):
        if i%j==0:
            temp.append(j)
    ans.append([i,max(temp)])
print(ans)
#2 nd approach
ans=[]
for i in range(100,111):
    ans.append([i,max([ j for j in range(1,11)if i%j==0 ])])
print(ans)
#3 rd approach
ans=[ [i,max([j for j in range(1,11)if i%j==0 ])]
      for i in range(100,111) ]
print(ans)
#4th approach
print([ [i,max([j for j in range(1,11)if i%j==0 ])]
         for i in range(100,111) ])
