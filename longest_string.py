## Given an array of strings strarr and an integer k, return the longest string formed by concatenating k consecutive strings from the array.

def longest_consec(strarr, k):
    n = len(strarr)
    if k<=0 or k >n:
        return ""
    highest = ""
    for index in range(0,n):
        if n-index >=k:
            sum_of_strings = "".join(strarr[index:index+k])
            if len(sum_of_strings) > len(highest):
                highest = sum_of_strings
    return highest      
                  
                
    
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
        