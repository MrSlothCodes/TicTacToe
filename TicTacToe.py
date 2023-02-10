print("TIC - TAC - TOE \nBy Suryansh Ahuja ")
print("Press The Number To Select Box ")
input("\nPress Any Key....")

ch = [1,2,3,
      4,5,6,
      7,8,9]

used = [-1]
OorX=0
work = True
wincon = False

       
print("\nPress [0] For Exit")

while work==True:
       print("\n")
       print(
             '|     |     |     |\n'
              
              '| ',ch[0],' | ',ch[1],' | ',ch[2],' |\n'
              
              '|_____|_____|_____|\n'
              '|     |     |     |\n'
              
              '| ',ch[3],' | ',ch[4],' | ',ch[5],' |\n'
              
              '|_____|_____|_____|\n'
              '|     |     |     |\n'

              '| ',ch[6],' | ',ch[7],' | ',ch[8],' |\n'

              '|     |     |     |\n'      
              )
       ox = ["O","X"]
       print(ox[OorX],"turn \n")
       box=input("Select Box :")

       if(box == '0','1','2','3','4','5','6','7','8','9'):
              box=int(box)
              if(box==0):
                     work == False
              
              elif(box>=1 and box<=9):
                     if(ch[box-1]=='O'):
                            print("Box",box,"is already Taken By O")
                            box=15
              
                     elif(ch[box-1]=='X'):
                            print("Box",box,"is already Taken By X")
                            box=15
       else :       
              print("Select A Valid Box")
              box=int(box)
              box=15

       
  
       if(box>0 and box<10):
              ch[box-1]=ox[OorX]
              used.append(box)
           
              if(OorX<=0):
                 OorX=1
              else:
                 OorX=0
       
       else :
              print("Not a valid box")

       #Win Conditions
       
       #1
       if (ch[0] == ch[1] == ch[2] == 'O') :
              print("O wins 1")
              work = False
              wincon = True
       elif (ch[0] == ch[1] == ch[2] == 'X') :
              print("X wins")
              work = False
              wincon = True
       #2
       elif (ch[3] == ch[4] == ch[5] == 'O') :
              print("O wins")
              work = False
              wincon = True
       elif (ch[3] == ch[4] == ch[5] == 'X') :
              print("X wins")
              work = False
              wincon = True

       #3
       elif (ch[6] == ch[7] == ch[8] == 'O') :
              print("O wins")
              work = False
              wincon = True
       elif (ch[6] == ch[7] == ch[8] == 'X') :
              print("X wins")
              work = False
              wincon = True
       #4
       elif (ch[0] == ch[3] == ch[6] == 'O') :
              print("O wins")
              work = False
              wincon = True
       elif (ch[0] == ch[3] == ch[6] == 'X') :
              print("X wins")
              work = False
              wincon = True
       
       #5
       elif (ch[1] == ch[4] == ch[7] == 'O') :
              print("O wins")
              work = False
              wincon = True
       elif (ch[1] == ch[4] == ch[7] == 'X') :
              print("X wins")
              work = False
              wincon = True
       #6
       elif (ch[2] == ch[5] == ch[8] == 'O') :
              print("O wins")
              work = False
              wincon = True
       elif (ch[2] == ch[5] == ch[8] == 'X') :
              print("X wins")
              work = False
              wincon = True
       #7
       elif (ch[0] == ch[4] == ch[8] == 'O') :
              print("O wins")
              work = False
              wincon = True
       elif (ch[0] == ch[4] == ch[8] == 'X') :
              print("X wins")
              work = False
              wincon = True
       #8
       elif (ch[2] == ch[4] == ch[6] == 'O') :
              print("O wins")
              work = False
              wincon = True
       elif (ch[2] == ch[4] == ch[6] == 'X') :
              print("X wins")
              work = False
              wincon = True

while wincon == True :
       print("\n")
       print('|     |     |     |\n'
              
              '| ',ch[0],' | ',ch[1],' | ',ch[2],' |\n'
              
              '|_____|_____|_____|\n'
              '|     |     |     |\n'
              
              '| ',ch[3],' | ',ch[4],' | ',ch[5],' |\n'
              
              '|_____|_____|_____|\n'
              '|     |     |     |\n'

              '| ',ch[6],' | ',ch[7],' | ',ch[8],' |\n'

              '|     |     |     |\n'      )

       wincon=False
input()