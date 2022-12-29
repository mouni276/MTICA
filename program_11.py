
#remove empty string
lst=["sedan","suv","","pickup",'',' ']
ans=[]
for i in lst:
    if i:
        ans.append(i)
print(ans)
