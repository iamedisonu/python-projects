#fibonacci

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

terms=int(input("enter a number of terms for fibonacci series: "))
for n in range (0,terms):
    print(fibo(n))
    


     