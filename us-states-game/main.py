import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
found = 0
found_states=[]
data = pandas.read_csv("50_states.csv")
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

while found < 50:
    answer_state = screen.textinput(title=f" {found}/50 States Correct", prompt="What's another state name?").title()
    if answer_state == "Exit":
        break
    result = data[data['state'] == answer_state]
    if result.empty or answer_state in found_states:
        pass
    else:
        found += 1
        writer.goto(result.x.item(),result.y.item())
        writer.write(answer_state)
        found_states.append(answer_state)

all_states = data.state.to_list()
states_to_learn = [s for s in all_states if s not in found_states]
data2 = pandas.DataFrame(states_to_learn)
data2.to_csv("states_to_learn.csv")