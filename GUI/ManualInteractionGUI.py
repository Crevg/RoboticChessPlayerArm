from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Boolean to know if the arm is holding a piece
global hasOnePicked
hasOnePicked = False

#test command
def moveCommand():
    print ("Move called\n")

def pickCommand():
    global hasOnePicked
    if hasOnePicked:
        messagebox.showerror("Error", "The robotic player is already holding a piece\nCall Drop or Move & Drop first")
    else:
        hasOnePicked = True
        print ("Pick called\n")

def dropCommand():
    global hasOnePicked
    if not hasOnePicked:
        messagebox.showerror("Error", "The robotic player is not holding a piece\nCall Pick or Move & Pick first")
    else:
        hasOnePicked = False
        print ("Drop called\n")

def movePickCommand():
    global hasOnePicked
    if hasOnePicked:
        messagebox.showerror("Error", "The robotic player is already holding a piece\nCall Drop or Move & Drop first")
    else:
        hasOnePicked = True
        print("MovePick called\n")

def moveDropCommand():
    global hasOnePicked
    if not hasOnePicked:
        messagebox.showerror("Error", "The robotic player is already holding a piece\nCall Drop or Move & Drop first")
    else:
        hasOnePicked = False
        print("MoveDrop called\n")
    
########################### WINDOW CREATION ###########################
#Root window creation
root = Tk()
root.title("Checkers GUI")


#Main frame that stores content
mainframe = Frame(master = root, width= 500, height = 300)

#Frame for the title
titleFrame = Frame(master = mainframe, bg = "blue")

#Frame for positions selection
positionFrame = Frame(master = mainframe, bg = "blue")

#Frame for move buttons
moveFrame = Frame(master = mainframe, bg = "blue")

#Frame for positions selection
pickDropFrame = Frame(master = mainframe, bg = "blue")

######################### Components for title frame ##########################
titleLabel = Label (titleFrame, text = "Manual Interaction GUI", bg = "blue", fg = "white", font=("Helvetica", 18))

######################### Components for position frame ##########################
#Position labels
labelX= Label(positionFrame, text = "Position X", bg = "blue" ,fg= "white", font=("Helvetica", 10))
labelY= Label(positionFrame, text = "Position Y", bg = "blue", fg= "white", font=("Helvetica", 10))

#Position comboboxes
comboboxX= ttk.Combobox(positionFrame, values=[1,2,3,4,5,6,7,8,9,10])
comboboxX.config(state = "readonly")
comboboxX.current(0)
comboboxY= ttk.Combobox(positionFrame, values=[1,2,3,4,5,6,7,8,9,10])
comboboxY.config(state = "readonly")
comboboxY.current(0)

########################## Components for move frame #########################
#Button to move, drop and pick
buttonMove= Button(moveFrame,text = "Move", command = moveCommand)
buttonMovePick= Button(moveFrame,text = "Move & Pick", command = movePickCommand)
buttonMoveDrop= Button(moveFrame,text = "Move & Drop", command = moveDropCommand)
buttonMove.config(width = 17)
buttonMovePick.config(width = 17)
buttonMoveDrop.config(width = 17)
######################### Components for the pick and drop frame #########################
buttonPick= Button(pickDropFrame,text = "Pick", command = pickCommand)
buttonDrop= Button(pickDropFrame,text = "Drop", command = dropCommand)
buttonPick.config(width = 27)
buttonDrop.config(width = 27)

#########################  Packing components  #########################
#Frames
mainframe.pack(side= BOTTOM)
titleFrame.pack(side = TOP , fill = X)
positionFrame.pack(side = TOP, fill =X)
moveFrame.pack(side = TOP, fill =X )
pickDropFrame.pack(side = TOP ,fill = X)

#Title frame
titleLabel.pack(side = TOP, fill =X )
#Position frame
labelX.pack(side = LEFT)
comboboxX.pack(side=LEFT)
labelY.pack(side = LEFT)
comboboxY.pack(side=LEFT)

#Move frame
buttonMovePick.pack(expand = True, side = LEFT)
buttonMove.pack(expand = True, side = LEFT)
buttonMoveDrop.pack(expand = True, side = LEFT)

#pick drop frame
buttonPick.pack(expand = True, side = LEFT)
buttonDrop.pack(expand = True, side = LEFT)

#########################  Mainloop #########################
root.mainloop()
