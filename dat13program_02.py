def printSunday():
    print('Sunday')
def printMonday():
    print('Monday')
def printTuesday():
    print('Tuesday')
def printWednesday():
    print('Wednesday')
def printThursday():
    print('Thursday')
def printFriday():
    print('Friday')
def printSaturday():
    print('Saturday')
def choice():
    print("enter day number between 1 to7:")
    return
dayDict={ 1:printSunday, 2:printMonday, 3:printTuesday, 4:printWednesday,
       5:printThursday, 6:printFriday, 7:printSaturday }
choice()
inpNum=int(input())
if inpNum>=1 and inpNum<=7:
    dayDict[inpNum]()
else:
    print("Invalid")
    
