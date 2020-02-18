smth = open("file.txt", "r")
words = smth.read().split(" ")
end = len(words)
i = 0
for i in range(end):
    pl1 = words[i].count("f") + words[i].count("c") + words[i].count("k") + words[i].count("r")
    pl2 = words[i].count("b") + words[i].count("d") + words[i].count("g") + words[i].count("h") + words[i].count("j") + words[i].count("l") + words[i].count("m") + words[i].count("n") + words[i].count("p") + words[i].count("q") + words[i].count("s") + words[i].count("t") + words[i].count("v") + words[i].count("w") + words[i].count("x") + words[i].count("z")
    if pl1 > pl2:
        print("Η λέξη", words[i], "είναι ΚΑΚΗ")
    else:
        print("Η λέξη", words[i], "είναι ΚΑΛΗ")

