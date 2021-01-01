from tkinter import *
import random
from PIL import ImageTk, Image
import itertools

# 6 sided dice
# 1-3 dice ask user
# Interface containing a textbox 
# Textbox will take userinput number of dice 1-3 dices
# Login button under the textbox 
# After game starts there will be two buttons
# Right one for rolling dice
# Left one stop the game


root = Tk()

def open_window():

    #GUI dice window

    nw = Toplevel(root) # nw = new window
    nw.geometry("700x450")
    nw.title("Roll the Dice")
    # nw.resizable(False,False)

    lb3 = Label(nw, text = "Good Luck")
    lb3.pack()
    lb2 = Label(nw,text = 'Number of Dice can be changed from the Login page \n Exit the Roll the Dice window \n Then Relogin again')
    lb2.pack()
    lb2.place(x=200, y= 380)
    # dicenum.delete(0,END)

    # For demo change directory to the direct path of the images
    # Random Dice
    dice = ['/home/furkan/Desktop/Projects/PythonProjects/GlobalAI-IntroductiontoPython/TopLearner/DiceRollingSimulator/Dice/Dice1.jpeg',
    '/home/furkan/Desktop/Projects/PythonProjects/GlobalAI-IntroductiontoPython/TopLearner/DiceRollingSimulator/Dice/Dice2.jpeg',
    '/home/furkan/Desktop/Projects/PythonProjects/GlobalAI-IntroductiontoPython/TopLearner/DiceRollingSimulator/Dice/Dice3.jpeg',
    '/home/furkan/Desktop/Projects/PythonProjects/GlobalAI-IntroductiontoPython/TopLearner/DiceRollingSimulator/Dice/Dice4.jpeg',
    '/home/furkan/Desktop/Projects/PythonProjects/GlobalAI-IntroductiontoPython/TopLearner/DiceRollingSimulator/Dice/Dice5.jpeg',
    '/home/furkan/Desktop/Projects/PythonProjects/GlobalAI-IntroductiontoPython/TopLearner/DiceRollingSimulator/Dice/Dice6.jpeg']
    dnum = int(dicenum.get())
    
    if dnum>=3:
        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

        im1 = Label(nw, image=image1)
        im2 = Label(nw, image=image2)
        im3 = Label(nw, image=image3)

        im1.pack()
        im1.place(x=100,y=150)
        im2.pack()
        im2.place(x=300,y=150)
        im3.pack()
        im3.place(x=500,y=150)

        im1.configure(image=image1)
        im1.image = image1
        im2.configure(image=image2)
        im2.image = image2
        im3.configure(image=image3)
        im3.image = image3
        
    elif dnum==2:
        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

        im1 = Label(nw, image=image1)
        im2 = Label(nw, image=image2)

        im1.pack()
        im1.place(x=100,y=150)
        im2.pack()
        im2.place(x=300,y=150)

        im1.configure(image=image1)
        im1.image = image1
        im2.configure(image=image2)
        im2.image = image2

    else:
        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

        im1 = Label(nw, image=image1)

        im1.pack()
        im1.place(x=100,y=150)

        im1.configure(image=image1)
        im1.image = image1
    
        

    def dice_roll():

        dcheck = int(dicenum.get())

        if dcheck >=3:
            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            im1.configure(image=image1)
            im1.image = image1

            image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            im2.configure(image=image2)
            im2.image = image2

            image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            im3.configure(image=image3)
            im3.image = image3

        elif dcheck==2:
            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            im1.configure(image=image1)
            im1.image = image1

            image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            im2.configure(image=image2)
            im2.image = image2

        else:
            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            im1.configure(image=image1)
            im1.image = image1

 
        
    # Roll Again Button
    broll = Button(nw,text="Roll again",command = dice_roll)
    broll.pack()
    broll.place(x = 340, y = 330)
     
    # Exit Button  
    bexit = Button(nw,text="Exit",command=lambda: nw.destroy())
    bexit.pack()
    bexit.place(x = 280, y = 330)

    # nw.mainloop()


# GUI Login

l1 = Label(root, text = "Number of Dice (MAX 3)")
l1.place(x=330,y=110)

dicenum = Entry(root, width= 10)
dicenum.place(x = 330, y = 140)

# Login Button
blogin = Button(root,text="Login",foreground='red',command=open_window)
blogin.pack()
blogin.place(x=330,y=170)

# Exit Button
bclose = Button(root,text="Exit",command=lambda: root.destroy())
bclose.pack()
bclose.place(x = 330, y = 230)

root.resizable(False,False)
root.geometry("700x450")
root.title("Dice Roller")
root.mainloop()
