n=int(input("enter any number:"))
for i in range(0,n):
    def fact(n):
     if n==0:
        return 1
     elif n==1:
        return 1
     else:
        return fact(n-1)*n
     
print(f"the factorial of the required number is {fact(n)} ")     
        
    