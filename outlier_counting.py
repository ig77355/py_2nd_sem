my_file = 'outliers_rl.txt'
d = dict()

with open(my_file, 'r') as f:
    for line in f:
        line = line.strip()
        # splitting the line into words
        words = line.split(" ")
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
    for key in list(d.keys()):
        print(key, ":", d[key])