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
    def Armstrong(self):
        n=str(self)
        n=len(self)
        total=0
        for i in self:
            total+=int(i)**n
        if (self)==total:
            return 'Armstrong'
        else:
            return 'not Armstrong'
        
                       
inp=int(input())
obj=Number(inp)
print('Factorial of ',inp,'is',obj.CalculateFactorial())
print(inp,'is',obj.checkEvenOdd())
print('sum of Digits of',inp,'is',obj.sumofDigits())
print(inp,'is',obj.Armstrong())
