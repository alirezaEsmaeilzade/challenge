def prime_nums(r):
    for i in range(2,r):
        prime = True
        for j in range(2,i):
            if (i%j==0):
                prime = False
        if prime:
            print (i, end=' ')
    print()

prime_nums(10000)