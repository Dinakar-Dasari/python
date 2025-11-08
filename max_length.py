def max_length(a1,a2):
    if a1 == [] or a2 == []:
        return -1
    else:
        new_a1 = sorted([len(word) for word in a1]) # or new_a1 = min([len(word) for word in a1]))
        new_a2 = sorted([len(word) for word in a2])
        max_diff_1 = abs(new_a1[0]-new_a2[-1])
        max_diff_2 = abs(new_a1[-1]-new_a2[0])
        return max(max_diff_1,max_diff_2)

print(max_length(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"],["bbbaaayddqbbrrrv"]))



#### chat_gpt version ###
# def max_length(a1, a2):
#     if not a1 or not a2:
#         return -1
#     a1_min, a1_max = min(map(len, a1)), max(map(len, a1))
#     a2_min, a2_max = min(map(len, a2)), max(map(len, a2))
#     return max(abs(a1_max - a2_min), abs(a2_max - a1_min))

