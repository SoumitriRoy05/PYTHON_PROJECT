#SNAKE,WATER AND GUN GAME
import random
'''
1->GUN
-1->WATER
0->SNAKE
'''
computer=random.choice([-1,0,1])
user_input=input("ENTER YOUR CHOICE:")
userDict={"S":0,"W":-1,"G":1}
reverse_userDict={0:"SNAKE",-1:"WATER",1:"GUN"}
user=userDict[user_input]
print(f"The user chose {reverse_userDict[user]}\n The computer chose {reverse_userDict[computer]}")
if(computer==user):
    print("IT'S A DRAW")
elif(computer==-1 and user==0):     # -1->water and 0->snake  =>snake wins
     print("COMPUTER LOSES AND USER WINS!!")
elif(computer==-1 and user==1):    # -1->water and 1->gun   =>water wins
       print("COMPUTER WINS AND USER LOSES!!")
elif(computer==0 and user==1):     # 1->gun and 0->snake    =>gun wins
       print("COMPUTER LOSES AND USER WINS!!")
elif(computer==0 and user==-1):     # -1->water and 0->snake  =>snake wins
       print("COMPUTER WINS AND USER LOSES!!")
elif(computer==1 and user==-1):      # -1->water and 1->gun   =>water wins
       print("COMPUTER LOSES AND USER WINS!!")
elif(computer==1 and user==0):       # 1->gun and 0->snake    =>gun wins
       print("COMPUTER WINS AND USER LOSES!!")


       

