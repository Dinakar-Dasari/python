import os

folders=input("Enter the folders to list the files separated by spaces: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print(f"{folder} is not a valid folder name. PLease check")
        continue    
    print(f"Files present in the {folder} are: ")
    for file in files:
            print(file)