class Number:
    def __init__(self,n):
        self.n=n
    def CalculateFactorial(self):
        if self.n==0:
            return 1
        res=1
        for i in range(1,self.n+1):
            res *=i
        return res
    def checkEvenOdd(self):
        if self.n%2==0:
            return "Even"
        else:
            return "Odd"
    def sumofDigits(self):
        if self.n<0:
            self.n=abs(self.n)
        temp=str(self.n)
        t=0
        for i in temp:
            t+=int(i)
        return t
    def checkArmstrong(self):
        assert self.n>=0,'the number should be >=0'
        temp=str(self.n)
        t=0
        for i in temp:
            t+=int(i)**len(temp)
        if t==self.n:
            return 'Armstrong'
        else:
            return 'not Armstrong'
    def checkPrime(self):
        assert(self.n>=0),"invalid"
        if (self.n==1 or self.n==2 or self.n==3):
            return "prime"
        for i in range(2,self.n):
            if self.n%i==0:
                return "not prime"
        return "prime"
        
                       
inp=int(input())
obj=Number(inp)
print('Factorial of ',inp,'is',obj.CalculateFactorial())
print(inp,'is',obj.checkEvenOdd())
print('sum of Digits of',inp,'is',obj.sumofDigits())
try:
    print(inp,'is',obj.checkArmstrong())
except AssertionError as a:
    print(a)
try:
    prim=obj.checkPrime()
    print(prim)
except AssertionError as ob:
    print(ob)

