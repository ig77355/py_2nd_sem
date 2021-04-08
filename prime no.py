n = int(input("How many prime numbers would you like to display?\n"))
a=0
for i in range(2, 1000000000):
    if a<n:
        if i>1:
            for b in range(2, i):
                if (i % b) == 0:
                    break
            else:
                print(i)
                a=a+1