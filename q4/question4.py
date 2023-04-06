def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)

if __name__ == "__main__":
    for i in range(8):
        print(factorial(2*i))

