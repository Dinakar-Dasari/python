birthdays = {"Alice": 'Apr 21', 'Bob': 'March 1', 'tony': 'May 1' }

while True:
    name = input("enter a name to know their birthdays. ")
    if name == "":
        break

    if name in birthdays:
        print(f'birthday of {name} is on {birthdays[name]}')
    else:
        print(f'{name} is not in the birthday list. Will add it now.')
        birthdays[name] = input("Enter the birthday date. ")
