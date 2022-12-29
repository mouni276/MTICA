
#print the names in upper case
dict1={"sedan":1500,"bicycle":7,"motorcycle":2500}
ans=[i.upper() for i in dict1 if dict1[i]<5000]   
print(ans)

#2nd approach
dict1={"sedan":1500,"bicycle":7,"motorcycle":2500}
ans=[]
for i in dict:
    if dict[i]<5000:
        ans.append(i.upper())
print(ans)
