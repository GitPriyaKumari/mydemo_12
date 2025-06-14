
#my first rock paper scisosor game
import random

computer=random.choice([-1,0,1])
youstr=(input("enter your choice for the whooping scissor paper rock game:"))
youdict={"s":0,"p":-1,"r":1}
reversedict={-1:"paper",1:"rock",0:"scissor"}
you=youdict[youstr]
print(f"you entered{reversedict[you]} \n the computer entered {reversedict[computer]}")

if(you==computer):
    print("its a draw bro")
else:
    if(computer==0 and you==-1):
        print("computer won hurrah!")
    elif(computer==0 and you==1):
        print("you win! congrats")
    elif(computer==1 and you==0):
        print("computer won")
    elif(computer==1 and you==-1):
        print("you won")
    elif(computer==-1 and you==0):
        print("you won")    
    elif(computer==-1 and you==1):
        print("computer won")
    else:
        print ("something is wrong lol")        
                
        
