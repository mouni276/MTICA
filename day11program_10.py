sample_dict={
    "name":"kelly",
    "age":25,
    "salary":5000,
    "city":"new york"}

sample_dict['location']=sample_dict.pop('city')
print(sample_dict)
