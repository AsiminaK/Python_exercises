text= open("file.txt", "r")
words= text.read().split(" ")
end= len(words)
i=0
for i in range(end):
    if len(words[i])>3:
        new_word = words[i][1:len(words[i])]
        words[i] = new_word + words[i][0] + "ay"
print(words)