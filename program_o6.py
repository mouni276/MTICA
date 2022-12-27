# to print 1-1000 numbers that divisible by 9  
lst=[]
for i in range(1,1001):
    if i%9==0:

       lst.append(i)
print(lst)
# to print 1-1000 numbers that divisible by 5
print([i for i in range(1,1001) if i%5==0]) 
# to print 1-1000 numbers that divisible by 8
ans=[i for i in range(1,1001) if i%8==0]
print(ans)
