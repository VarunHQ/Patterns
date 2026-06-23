def fib_series(nterms):
    #First two terms
    n1, n2 = 0, 1
    count = 0
    while count < nterms:
        print(n1)
        nth = n1 + n2
        #update values
        n1 = n2
        n2 = nth
        count += 1


nterms = int(input("How many terms? "))

#Check if the number of terms is vaild
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    fib_series(nterms)
else:
    print("Fibonacci sequence:")
    fib_series(nterms)