#1st approach
def removeSpecialChar(s):
    ans=[]
    for i in s:
        if i in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            ans.append(i)
    return ''.join(ans)
inp=input()
print(removeSpecialChar(inp))
 #2nd appraoch       
def removeSpecialChar(s):
    ans=[]
    for i in s:
        if ((ord(i) in range(65,91)) or (ord(i) in range(97,123))
            or (ord(i) in range(48,58))):
            ans +=i
    return ans
inp=input()
print(removeSpecialChar(inp))
