count = 0
with open("input.txt") as f:
    for line in f:
        if line == "\n":
            continue
        count = count + 1
        with open("ex1.txt", "a+") as f1:
            f1.write('(%d) %s' %(count,line))