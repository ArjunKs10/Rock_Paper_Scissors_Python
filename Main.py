import random

dict={"r":0,"p":1,"s":2}
reversedict={0:"r",1:"p",2:"s"}

while True:
  f=input("Enter your choice Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors and Enter q to quit : ")
  if f == "q":
    print("Thanks for playing!")
    break

  if f not in dict:
   print("Enter a valid choice ")
   continue


  comp=random.randint(0,2)
  n=dict[f]

  if(comp==n):
   print("Draw")
  else:
    if((comp==0 and n==1) or(comp==1 and n==2) or(comp==2 and n==0)):
      print("You Win!")
    elif((comp==0 and n==2)or(comp==1 and n==0)or(comp==2 and n==1)):
      print("You Lose!")
  a=reversedict[comp]
  print(f"Computer chose {a}")
