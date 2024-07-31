
from tkinter import *
from PIL import ImageTk, Image
import random

#*********************************************************************************************************
window = Tk()
window.geometry("800x600")
window.title('The Rock Paper Scissor Game A Timeless Batle Of Element')
window.configure(bg="black")

canvas = Canvas(window, width=800, height=600)
canvas.grid(row=0, column=0)
canvas.configure(bg='black')

############################################ IMAGES  #####################################################

#********************* Default image *************************
img_com = Image.open("D:\PYTHON\IMGS\default.jpeg")
img_com = img_com.resize((300, 300))
 
# Flipping image from left to right
img_you = img_com.transpose(Image.FLIP_LEFT_RIGHT)
 
# Loading images to put on canvas
img_com = ImageTk.PhotoImage(img_com)
img_you = ImageTk.PhotoImage(img_you)

#************************ rock  *****************************
rock_com = Image.open("D:\PYTHON\IMGS\Rock.jpg")
rock_com = rock_com.resize((300, 300))
 
# Flipping image from left to right
rock_you = rock_com.transpose(Image.FLIP_LEFT_RIGHT)
 
# Loading images to put on canvas
rock_com = ImageTk.PhotoImage(rock_com)
rock_you = ImageTk.PhotoImage(rock_you)

#**********************  paper  ******************************
paper_com = Image.open("D:\PYTHON\IMGS\paper.jpg")
paper_com = paper_com.resize((300, 300))
 
# Flipping image from left to right
paper_you = paper_com.transpose(Image.FLIP_LEFT_RIGHT)
 
# Loading images to put on canvas
paper_com = ImageTk.PhotoImage(paper_com)
paper_you = ImageTk.PhotoImage(paper_you)

#********************** scissor ******************************
scissor_com = Image.open("D:\PYTHON\IMGS\scissor.jpg")
scissor_com = scissor_com.resize((300, 300))
 
# Flipping image from left to right
scissor_you = scissor_com.transpose(Image.FLIP_LEFT_RIGHT)
 
# Loading images to put on canvas
scissor_com = ImageTk.PhotoImage(scissor_com)
scissor_you = ImageTk.PhotoImage(scissor_you)

#*************************************************************

canvas.create_image(0, 150, anchor=NW, image=img_com)
canvas.create_image(500, 150, anchor=NW, image=img_you)

#####################################################################################################

#  ROCK = 1
#  PAPER = 2
#  SCISSOR = 3

########################################## ROCK  #####################################################
def rock():
# Randomly selects option for computer.
    randNo = random.randint(1,3)
    if randNo == 1:
        computer = 'ROCK'
        canvas.create_image(0, 150, anchor=NW, image=rock_com)
    elif randNo == 2:
        computer = 'PAPER'
        canvas.create_image(0, 150, anchor=NW, image=paper_com)
    elif randNo == 3:
        computer = 'SCISSOR'
        canvas.create_image(0, 150, anchor=NW, image=scissor_com)
        
    if computer == 'ROCK':
        print('TIE')
        res = 'TIE'
        
    elif computer == 'PAPER':
        print('LOOSE')
        res = 'LOOSE'
    elif computer == 'SCISSOR':
        print('YOU WIN')
        res = 'YOU WIN'

    canvas.create_text(390, 300, text=res,anchor="center",fill="white", font= ('Algerian 20'), tag='result')
    canvas.create_text(150, 100, text=computer,anchor="center",fill="white", font= ('Algerian 20'), tag='result')
    canvas.create_text(650,100, text='ROCK',anchor="center",fill="white", font= ('Algerian 20'), tag='result')
    
    canvas.create_image(500, 150, anchor=NW, image=rock_you)

#################################################  PAPER  #########################################################

def paper():
    randNo = random.randint(1,3)
    if randNo == 1:
        computer = 'ROCK'
    elif randNo == 2:
        computer = 'PAPER'
    elif randNo == 3:
        computer = 'SCISSOR'
    
    if computer == 'ROCK':
        print('You WIN')
        res = 'YOU WIN'
        canvas.create_image(0, 150, anchor=NW, image=rock_com)
        
    elif computer == 'PAPER':
        print('TIE')
        res = 'TIE'
        canvas.create_image(0, 150, anchor=NW, image=paper_com)

    elif computer == 'SCISSOR':
        print('LOOSE')
        res = 'LOOSE'
        canvas.create_image(0, 150, anchor=NW, image=scissor_com)

    canvas.create_text(390, 300, text=res,anchor="center",fill="white", font= ('Algerian 20'), tag='result')
    canvas.create_text(150, 100, text=computer,anchor="center",fill="white", font= ('Algerian 20'), tag='result')
    canvas.create_text(650,100, text='PAPER',anchor="center",fill="white", font= ('Algerian 20'), tag='result')

    canvas.create_image(500, 150, anchor=NW, image=paper_you)

########################################### SCISSOR ######################################################    

def scissor():
    randNo = random.randint(1,3)
    if randNo == 1:
        computer = 'ROCK'
    elif randNo == 2:
        computer = 'PAPER'
    elif randNo == 3:
        computer = 'SCISSOR'
    
    if computer == 'ROCK':
        print('LOOSE')
        res = 'LOOSE'
        canvas.create_image(0, 150, anchor=NW, image=rock_com)

    elif computer == 'PAPER':
        print('YOU WIN')
        res = 'YOU WIN'
        canvas.create_image(0, 150, anchor=NW, image=paper_com)

    elif computer == 'SCISSOR':
        print('TIE')
        res = 'TIE'
        canvas.create_image(0, 150, anchor=NW, image=scissor_com)

    canvas.create_text(390, 300, text=res,anchor="center",fill="white", font= ('Algerian 20'), tag='result')
    canvas.create_text(150, 100, text=computer,anchor="center",fill="white", font= ('Algerian 20'), tag='result')
    canvas.create_text(650,100, text='SCISSOR',anchor="center",fill="white", font= ('Algerian 20'), tag='result')

    canvas.create_image(500, 150, anchor=NW, image=scissor_you)

#############################################  CLEAR BUTTON ###############################################
def clear():
   
    canvas.delete('result')

    canvas.create_image(0, 150, anchor=NW, image=img_com)
    canvas.create_image(500, 150, anchor=NW, image=img_you)

#############################################  LABELS   ###################################################

l1=Label(window,text="COMPUTER's CHOISE ",anchor="center",bg = "black",fg="cyan",font="Roman 20 bold ")
l1.place(x=50,y=30)
l2= Label(window,text='YOUR CHOISE',anchor="center",bg = "black",fg="cyan",font="Roman 20 bold")
l2.place(x=580,y=30)
l3=Label(window,text='RESULT',anchor="center",bg = "black",fg="magenta",font="Roman 20 bold ")
l3.place(x=350,y=230)

############################################  BUTTONS  #######################################################

c=Button(window,text='CLEAR',width=20, command=clear )
c.place(x=330,y=480)

r=Button(window,text='ROCK',width=20, command=rock)
r.place(x=100,y=530)

p=Button(window,text='PAPER',width=20, command=paper )
p.place(x=330,y=530)

s=Button(window,text='SCISSOR',width=20, command=scissor)
s.place(x=580,y=530)

###############################################################################################################

window.mainloop()

