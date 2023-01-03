set1={19,20,30,40,50}
set2={90,70,80,100}
if set1.isdisjoint(set2):
    print("two sets have no items in common")
else:
    print("two sets have items in common")
    print(set1.intersection(set2))
