n=int(input("enter the number of your choice:"))

def fib(n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return (fib(n- 1) + fib(n- 2))
print(f"the fibonacci series of that number is {fib(n)}")        