def extract_consonants(s):
    consonants=''
    for i in s:
        if i in 'bcdfghjklmnpqrstvwxyz':
            consonants+=i
    return consonants
str1=input()
a=extract_consonants(str1)
print("consonants in:",str1,"is:",a)
