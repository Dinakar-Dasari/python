name=''
while True:
    name = input("Enter your name: ")
    if name != "joe":
        continue
    state = input("Hello, joe. How are you")
    if state == "fine":
        break
print("Good to hear, joe")    
