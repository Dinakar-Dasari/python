student1 = {
    "name": "Messi",
    "position": "LWF",
    "jerseyn": 10
}

for key in student1.keys():
    print(key)   ## ---> name
                 #      position
                 #     jerseyn

for value in student1.values():
    print(value)  ## Messi, 
                  ## LWF
                  #  10      

for data in student1.items():
    print(data)                  