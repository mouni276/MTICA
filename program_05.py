def extract_digit(s):
    n_digit=0
    for i in s:
        if i in '123456789':
            n_digit+=1
    return n_digit
str1=input()
a=extract_digit(str1)
print("no of digit in:",str1,"is:",a)
