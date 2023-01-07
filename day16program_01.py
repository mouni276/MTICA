lst=[1,2,3,4]
it=iter(lst)
##print (next(it))
for x in it:
    print(x,end=" ")
import sys
while True:
    try:
        print (next(it))
    except Exception as ob:
        print(ob)
        break
