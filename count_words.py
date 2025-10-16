import sys
from collections import Counter

file_name = sys.argv[1]
print("File name is:", file_name)
with open(file_name,"r") as file:
    text = file.read()
# if used file.readlines() --> ['words\n', 'Words word Wor1ds\n', 'exit exle exile WorDs']
# if used file.readline() --> words
# if used file.read() --> complete file

words = text.split()
word_count = {}
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

top_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
print(top_words)