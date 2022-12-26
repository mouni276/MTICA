def remove_duplicates(s):
    str2=''
    for i in s:
        if i not in str2:
            str2+=i
    return str2
str1=input("enter your text: ")
print("without duplicates: ",remove_duplicates(str1))
