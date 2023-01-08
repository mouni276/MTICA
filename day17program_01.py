import sys
print("coming through stdout")
save_stdout=sys.stdout
fh=open(r"D:\pythonpractice37\test.txt","w")
sys.stdout=fh
print("this line goes to test.txt")
print(input())
fh.close()
      
