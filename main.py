import turtle
import pandas

# create the screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# get the image in the adjoining file as the background of the screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# read the file using pandas
states_data = pandas.read_csv("50_states.csv")
states_names = states_data["state"].to_list()
states_xcor = states_data["x"].to_list()
states_ycor = states_data["y"].to_list()
guessed_states = []
num_correct = 0

while len(guessed_states) < 50:
    # get the state from the user in the text box
    answer_state = screen.textinput(title=f"{num_correct}/50 States Correct", prompt="Enter a state: ").title()

    if answer_state in states_names:
        num_correct += 1

        # get index of answer state
        index = states_names.index(answer_state)

        # get x and y coordinates for the state chosen by the user
        x = states_xcor[index]
        y = states_ycor[index]

        # create a turtle for the name of the state
        state_title = turtle.Turtle()
        state_title.hideturtle()
        state_title.penup()
        state_title.goto(x, y)
        state_title.pendown()
        state_title.write(answer_state, move=False, align="center", font=("Arial", 8, "normal"))

        # add guessed state to list of guessed states
        guessed_states.append(answer_state)

# print the finishing title to the screen when the user guesses all 50 states
title = turtle.Turtle()
title.hideturtle()
title.penup()
title.goto(-150, 200)
title.pendown()
title.write("Congrats, You Win!", move=False, align="center", font=("Arial", 16, "normal"))

screen.exitonclick()
