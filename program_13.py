def removeVowels(s):
    temp=''
    for i in s:
        if i in 'AEIOUaeiou':
            temp+=i
    return temp
str1=input("enter your text:")
a=removeVowels(str1)
print("vowels are:",a)
