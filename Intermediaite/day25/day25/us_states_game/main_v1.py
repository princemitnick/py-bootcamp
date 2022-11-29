import turtle
import pandas
from state import State
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
image_2 = "prince.gif"
screen.addshape(image)

turtle.shape(image)


# def get_mouse_click_coord(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coord)
# turtle.mainloop()


data = pandas.read_csv("50_states.csv")
data_list = data['state'].to_list()
states_count = data['state'].count()
print(states_count)
guess_states = []
states_to_learn = []
game_is_on = True

count = 0

while count < states_count:
    answer_state = screen.textinput(title=f"{count}/{states_count} States Correct", prompt="What's the state?").title()
    print(answer_state)
    print(data_list)
    if answer_state == "Exit":
        for state in data_list:
            if state not in guess_states:
                states_to_learn.append(state)

        states_to_learn_dict = {"states": states_to_learn}
        df = pandas.DataFrame(states_to_learn_dict)
        df.to_csv("states_to_learn.csv")

        break
    if answer_state not in data_list or answer_state in guess_states:
        pass
    else:
        guess_states.append(answer_state)
        data_state_name = data[data['state'] == answer_state]
        x_cor = int(data_state_name.x)
        y_cor = int(data_state_name.y)
        State(answer_state, x_cor, y_cor)
        count += 1



