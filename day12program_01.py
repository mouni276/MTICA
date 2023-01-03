def printSeries(ch,n):
    assert(n>=0),'invalid'
    sp='.'
    for i in range(0,n):
        print(sp*(n-i-1) +ch*(2*i+1)+sp*(n-i-1))
        
    return None
inpch=input()
inpNum=int(input())
try:
    printSeries(inpch,inpNum)
except AssertionError as ob:
    print(ob)
