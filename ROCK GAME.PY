# ROCK,PAPER,SCISSOR  GAME
import random


gameconsole='''
 _____________________________   
/        _____________        \  
| ======|             |====== |  
|   _   |  ROCK       | X  B  |  
|  / \  |             | A  Y  |  
| | O | |       PAPER |       |  
|  \_/  |             |*******|  
|  \_/  |  SCISSOR    |*******|  
|       |             | . . . |  
|  :::  |             | . . . |  
|  :::  |_____________| . . . |  
|           R P S             |  
\_____________________________/

'''
print(gameconsole)
computer_choice=random.choice(["R","P","S"])
user_choice=input("CHOOSE YOUR MOVE\n FOR ROCK[R]\n FOR PAPER[P]\n FOR SCISSOR[S] ")
print("COMPUTER CHOOSES: "+ computer_choice)
if user_choice==computer_choice:
    print("MATCH IS TIE")
elif (user_choice=="R")and(computer_choice=="S"):
    print("YOU WON,ROCK SMASHES THE SCISSORS")
elif (user_choice=="R")and(computer_choice=="P"):
    print("YOU LOSE,PAPER FOLD THE ROCK")
elif (user_choice=="P")and(computer_choice=="R"):
    print("YOU WON,PAPER FOLD THE ROCK")
elif (user_choice=="P")and(computer_choice=="S"):
    print("YOU LOSE,SCISSOR CUTS THE PAPER")
elif (user_choice=="S")and(computer_choice=="P"):
    print("YOU WON,SCISSOR CUTS THE PAPER")
elif (user_choice=="S")and(computer_choice=="R"):
    print("YOU LOSE,ROCK SMASHES THE SCISSORS")
else:
    print("INVALID INPUT")