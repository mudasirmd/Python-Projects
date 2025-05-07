import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states=[state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


50 STATE CSV
state,x,y
Alabama,139,-77
Alaska,-204,-170
Arizona,-203,-40
Arkansas,57,-53
California,-297,13
Colorado,-112,20
Connecticut,297,96
Delaware,275,42
Florida,220,-145
Georgia,182,-75
Hawaii,-317,-143
Idaho,-216,122
Illinois,95,37
Indiana,133,39
Iowa,38,65
Kansas,-17,5
Kentucky,149,1
Louisiana,59,-114
Maine,319,164
Maryland,288,27
Massachusetts,312,112
Michigan,148,101
Minnesota,23,135
Mississippi,94,-78
Missouri,49,6
Montana,-141,150
Nebraska,-61,66
Nevada,-257,56
New Hampshire,302,127
New Jersey,282,65
New Mexico,-128,-43
New York,236,104
North Carolina,239,-22
North Dakota,-44,158
Ohio,176,52
Oklahoma,-8,-41
Oregon,-278,138
Pennsylvania,238,72
Rhode Island,318,94
South Carolina,218,-51
South Dakota,-44,109
Tennessee,131,-34
Texas,-38,-106
Utah,-189,34
Vermont,282,154
Virginia,234,12
Washington,-257,193
West Virginia,200,20
Wisconsin,83,113
Wyoming,-134,90

