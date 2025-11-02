def filter_list(list):
    return [i for i in list if isinstance(i,int)]

print(filter_list([1,2,'aasf','1','123',123]))

