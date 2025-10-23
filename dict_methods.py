### get()

student1 = {
    "name": "Messi",
    "position": "LWF",
    "jerseyn": 10
}

print(student1.get("Country", "Argentina"))
print(student1)  ### --> Country is not added to the dict

### setdefault()

student1 = {
    "name": "Messi",
    "position": "LWF",
    "jerseyn": 10
}

print(student1.setdefault('country','Argentina'))
print(student1)  ### --> Country is added to the dict

