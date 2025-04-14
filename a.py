# Import libraries
import turtle
import pandas as pd

screen=turtle.Screen()
game_is_on=True                          # for while loop
data=pd.read_csv('states_data.csv')      # to read csv file which contain states data

# set india gif image at background
image="India-state.gif"
screen.addshape(image)
turtle.shape(image)
count=0                                   # keep track of the all atempts 

while game_is_on == True:
    screen.title("India State Game")
    guess=screen.textinput(title="Guess The State Game",prompt=f"you'r attempts are ={count}").title()    # for taking input from user
    if guess in data['state'].values:               # this statement check does input from user is in csv dataset
        guess_cor=data[data['state']==guess]        # to access the row  of state from csv
        x_chor=int(guess_cor['x'].values[0])        # to collect cordinates from selected row
        y_chor=int(guess_cor['y'].values[0])
        # creating new turtle to go on retrived co-ordinates
        t=turtle.Turtle()                           
        t.penup()
        t.shape('circle')
        t.color('blue')
        t.goto(x_chor, y_chor)
        t.pendown()
        t.write(guess, font=('Arial',8), align='Center')   # To write the name of state on map
        count+=1                    # Increase the count
    else:
        count+=1

screen.exitonclick()


# screen.exitonclick()
