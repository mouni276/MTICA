def printDay(dn):
    if(dn==1):
        return "monday"
    elif(dn==2):
        return "tuesday"
    elif(dn==3):
        return "wednesday"
    elif(dn==4):
        return "thursday"
    elif(dn==5):
        return "friday"
    elif(dn==6):
        return "saturday"
    elif(dn==7):
        return "sunday"
    else:
        return "Invalid"
import time
inpNum=int(input())
start=time.time()
print(printDay(inpNum))
print(time.time()-start)
    
                    
