import random
n=random.randint(1,100)
a=-1
guesses=1
while(a!=n):
    
    a=int(input("enter a random number"))
    if(a>n):
        print("please enter a smaller numer")
        guesses+=1
    elif(a<n):
        print("higher number please")
        guesses+=1
    
print(f"congratulations! you have guessed the very right number{n} in {guesses} guesses")
