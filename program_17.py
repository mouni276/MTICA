#using map function
inpl=['apple','gua','jamakaya','mango','papaya','orange']
def rev_str(a):
    return a[::-1]
outl=list(map(rev_str,inpl))
print(inpl)
print(outl)
print('-'*60)
#using lambda
inpl=['apple','gua','jamakaya','mango','papaya','orange']
outl=list(map(lambda x:x[::-1],inpl))
print(inpl)
print(outl)
