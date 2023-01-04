def squares(x=0):
    while x<10:
        x = x + 1
        yield x*x
#yieldedList = list(squares())#materialise list from generator using list()
yieldedList=[i for i in squares()]
print(yieldedList)
        
