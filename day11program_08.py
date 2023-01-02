sample_dict={
    "name":"kelly",
    "age":25,
    "salary":5000,
    "city":"new york"}
keys={"name","salary"}
##for k in keys:
##    sample_dict.pop(k)
##print(sample_dict)

d=dict()
for i in sample_dict.keys()-keys:
    d[i]=sample_dict[i]
print(d)


