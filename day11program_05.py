
#1.
sampleDict={
    "class":{
        "student":{
            "name":"mike",
            "marks":{
                "physics":70,
                "history":80
                }
            }
        }
    }
print(sampleDict["class"]["student"]["marks"]["history"])

#2.
employees={'seeta','geeta','ramu'}
defaults={"designation":'developer','salary':8000}
data=dict.fromkeys(employees,defaults)
print(data)
print(data["ramu"])
