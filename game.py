import random
l=["rock","scissor","paper"]

#rock vs paper->paper wins
#rock vs scissor-> rock wins
#paper vs scissor-> scissor wins

while True:
    uc=int(input('''
Game Start.....
1.Yes
2.NO | Exit                 
'''))
    ccount=0
    ucount=0
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1.Rock
2.Scissor
3.Paper                                
'''))
            if userInput==1:
                uchoice="rock"
            elif userInput==3:
                uchoice="paper"
            elif userInput==2:
                uchoice="scissor"
            Cchoice=random.choice(l)    
            if Cchoice==uchoice:
                print("Computer Value",Cchoice)
                print("User Value",uchoice)
                print("Game.Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif(uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                print("You win")
                ucount=ucount+1
            else:
                print("Computer Value",Cchoice)
                print("User Value",uchoice)   

        if ucount==ccount:
            print("Final Game Draw....")
            print("User Score",ucount)
            print("Computer SCore",ccount)
        elif ucount>ccount:
            print("Final You Win11 The Game....")
            print("User Score",ucount)
            print("Computer SCore",ccount)
        else:
            print("Final Computer Win The Game Draw....")
            print("User Score",ucount)
            print("Computer SCore",ccount)    
                      
        
    else:
        break
        