def globals():
    global egg 
    egg = "twenty"
    return egg

egg = "sixty"
egg = globals()
print(f"{egg}")

# use global keyword for the variable using in function