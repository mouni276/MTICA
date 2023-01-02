#1st approach
dict1={'ten':10,'twenty':20,'thirty':30}
dict2={'thirty':30,'fourty':40,'fifty':50}

dict3={**dict1,**dict2}
print(dict3)

#2nd approach
dict1={'ten':10,'twenty':20,'thirty':30}
dict2={'thirty':30,'fourty':40,'fifty':50}
dict3=dict1.copy()
dict3.update(dict2)
print(dict3)


