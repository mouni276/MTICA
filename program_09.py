def extract_consonants(s):
    specialcharacter=''
    for i in s:
        if i in '!@#$%&*':
            specialcharacter+=i
    return specialcharacter
str1=input()
a=extract_specialcharacter(str1)
print("special characters in:",str1,"is:",a)
