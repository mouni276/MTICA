lstEven=[]
lstOdd=[]
while(True):
    inpNum=int(input("enter a value(0 to end):"))
    if inpNum==-1:
        break
    elif inpNum%2==0:
        lstEven.append(inpNum)
    elif inpNum%2==1:
        lstOdd.append(inpNum)
print("Even:",*lstEven)
print("min:",lst(lstEven))
print("max:",lst(lstEven))
print("avg:",round(sum(lstEven)/len(lstEven),1)) 

print("odd:",*lstOdd)
print("min:",lst(lstOdd))
print("max:",lst(lstOdd))
print("avg:",round(sum(lstOdd)/len(lstOdd),1)) 

