import random
list1=[0,1,2,3,4,5,6,7,8]
k= []
def start():
    print("     ENTER TO THE GAME OF TIC-TAC-TOE     ")
    print("                ",list1[0],"|",list1[1],"|",list1[2],"\n",
          "              ","---","---","---","\n",
          "               ",list1[3],"|",list1[4],"|",list1[5],"\n",
          "              ","---","---","---","\n",
          "               ",list1[6],"|",list1[7],"|",list1[8])
    name1=input("ENTER THE NAME OF PLAYER 1=")
    #name2=input("ENTER THE NAME OF PLAYER 2=")
    print("YOU SHOULD ENTER ONLY 'X' OR 'O'     ")
    print("     LETS START THE GAME     ")
    print("INSTRUCTION:","\n","PLAYER 1 WILL BE ASSIGNED 'O'","\n","COMPUTER WILL BE ASSIGNED 'X'","\n","ENTER THE CELL NUMBER AS SHOWN IN THE DIAGRAM FOR ENTERING EITHER 'X' OR 'O'")
    play()
def play():
    for i in range(10):
        
        in1=input("player 1 enter your choice")
        list1[eval(in1)]="O"
        k.append(in1)
        print(k)
        show()
        check()

        print("computers choice")
        test_list = [0,1,2,3,4,5,6,7,8]
        res = random.choice([ele for ele in test_list if ele not in k])
        if i==0:
          list1[res]="X"
          show()
          check()
        
        else:
          
          if list1[0]==list1[4]=="O":
             list1[8]="X"
             show()
             check()
          elif list1[0]==list1[1]=="O":
              list1[2]="X"
              show()
              check()              
          elif list1[0]==list1[3]=="O":    
              list1[6]="X"
              show()
              check()
          elif list1[1]==list1[4]=="O":
               list1[7]="X"
               show()
               check()
          elif list1[6]==list1[7]=="O":
               list1[8]="X"
               show()
               check()
          elif  list1[2]==list1[5]=="O":
               list1[8]="X"
               show()
               check()
          elif list1[2]==list1[4]=="O":
               list1[6]="X"
               show()
               check()   
          elif  list1[3]==list1[4]=="O":
               list1[5]="X"
               show()
               check()               
def check():
    if  list1[0]==list1[4]==list1[8]=="o" or list1[0]==list1[1]==list1[2]=="o" or list1[0]==list1[3]==list1[6]=="o"  or list1[1]==list1[4]==list1[7]=="o" or list1[6]==list1[7]==list1[8]=="o" or list1[2]==list1[5]==list1[8]=="o" or list1[2]==list1[4]==list1[6]=="o" or list1[3]==list1[4]==list1[5]=="o":
        print("player 2 has won")
        check2()
    elif list1[0]==list1[4]==list1[8]=="x" or list1[0]==list1[1]==list1[2]=="x" or list1[0]==list1[3]==list1[6]=="x"  or list1[1]==list1[4]==list1[7]=="x" or list1[6]==list1[7]==list1[8]=="x" or list1[2]==list1[5]==list1[8]=="x" or list1[2]==list1[4]==list1[6]=="x" or list1[3]==list1[4]==list1[5]=="x":
        print("player 1 has won")
        check2()
def show():
    print("                ",list1[0],"|",list1[1],"|",list1[2],"\n",
          "              ","---","---","---","\n",
          "               ",list1[3],"|",list1[4],"|",list1[5],"\n",
          "              ","---","---","---","\n",
          "               ",list1[6],"|",list1[7],"|",list1[8])
def check2():
    in2=input("IF YOU WANT TO CONTINUE TYPE 'YESSSS' or 'NO'=")
    if in2=="YESSSS":
        play()
    else:
        print("THANK YOU FOR PLAYING THE GAME")
        exit()
        
start()