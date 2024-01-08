from tkinter import *
from PIL import Image,ImageTk
from random import randint

#main window
root=Tk()
root.title("Rock-Paper-Scissor")
root.configure(background="#7C1034")

# importing picture
rock_img=ImageTk.PhotoImage(Image.open("rock.png"))
paper_img=ImageTk.PhotoImage(Image.open("paper.png"))
sci_img=ImageTk.PhotoImage(Image.open("scissors.png"))
rock_img_comp=ImageTk.PhotoImage(Image.open("rock_c.png"))
paper_img_comp=ImageTk.PhotoImage(Image.open("paper_c.png"))
sci_img_comp=ImageTk.PhotoImage(Image.open("sci_c.png"))

#inserting images
user_label = Label(root, image=rock_img , bg="#7C1034")
comp_label = Label(root,image=rock_img_comp,bg="#7C1034")

user_label.grid(row=1,column=0)
comp_label.grid(row=1,column=4)

playerscore= Label(root,text=0,font=100,bg="#7C1034",fg="white")
computerscore= Label(root,text=0,font=100,bg="#7C1034",fg="white")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

#indicators

user_ind=Label(root,font=50,text="USER",bg="#7C1034",fg="white")
comp_ind=Label(root,font=50,text="COMPUTER",bg="#7C1034",fg="white")
user_ind.grid(row=0,column=1)
comp_ind.grid(row=0,column=3)

#messages

msg=Label(root,font=50,bg="#7C1034",fg="white")
msg.grid(row=3,column=2)

#update message

def updatemsg(x):
    msg['text']= x
    
#update user score
def updateuserscore():
    score=int(playerscore["text"])
    score +=1
    playerscore["text"]=str(score)
    

#update computer score    
def updatecompscore():
    score=int(computerscore["text"])
    score +=1
    computerscore["text"]=str(score)
# check winner

def check(player,computer):
    if player == computer:
        updatemsg("Its a Tie!!")
    elif player == "rock":
        if computer == "paper":
            updatemsg("You Loose")
        else:
            updatemsg("You Win")
            updateuserscore()
    elif player == "paper":
        if computer == "scissor":
            updatemsg("You Loose")
            updatecompscore()
        else:
            updatemsg("You Win")
            updateuserscore()
    elif player=="scissor":
        if computer=="rock":
            updatemsg("You Loose")
            updatecompscore()
        else:
            updatemsg("You Win!")
            updateuserscore()
  
        
    
#update choice

choices=["ROCK","PAPER","SCISSOR"]
def updatechoices(x):
#for computers
    compchoice = choices[randint(0,2)]
    if compchoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compchoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=sci_img_comp)


#for user
    if x=="ROCK":
        user_label.configure(image=rock_img)
    elif(x=="PAPER"):
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=sci_img)
    
    check(x,compchoice)
    
#buttons

rock=Button(root,width=20,height=2,text="ROCK",bg="#FF3E40",fg="white",command= lambda:updatechoices("ROCK"))
paper=Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command= lambda:updatechoices("PAPER"))
sci=Button(root,width=20,height=2,text="SCISSORS",bg="#0ABDE3",fg="white",command= lambda:updatechoices("SCISSORS"))
rock.grid(row=2,column=1)
paper.grid(row=2,column=2)
sci.grid(row=2,column=3)

root.mainloop()
