from tkinter import *
import geo01
import info02
import info05
import result
import login
import register

# exercises array
a_exercise = ["geo01", "info02", "info05"]
albl_image = [None, None, None]  # label (with images) array
a_image = [None, None, None]  # images array
a_title = [None, None, None]  # array of title (ex: GEO01)

dict_games = {"geo01": geo01.open_window_geo_01, "info02": info02.open_window_info_02, "info05": info05.open_window_info_05}

# call other windows (exercices)
def exercise(event, exer):
    dict_games[exer](window)

# call display_results
def display_result(event):
    result.open_window_result(window)
    print("display_result")

def login_window(event):
    print("Login")
    login.window_login(event)

def register_window(event):
    print("Register")
    register.window_register(event)

# fenetre principal
window = Tk()
window.title("Training, entrainement cérébral")
window.geometry("1100x900")

# color définition
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color
window.configure(bg=hex_color)
window.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

# Title création
lbl_title = Label(window, text="TRAINING MENU", font=("Arial", 15))
lbl_title.grid(row=0, column=1, ipady=5, padx=40, pady=40)

# positionnement des labels
for ex in range(len(a_exercise)):
    a_title[ex] = Label(window, text=a_exercise[ex], font=("Arial", 15))
    a_title[ex].grid(row=1 + 2 * (ex // 3), column=ex % 3, padx=40, pady=10)

    a_image[ex] = PhotoImage(file="img/" + a_exercise[ex] + ".gif")
    albl_image[ex] = Label(window, image=a_image[ex])
    albl_image[ex].grid(row=2 + 2 * (ex // 3), column=ex % 3, padx=40, pady=10)
    albl_image[ex].bind("<Button-1>", lambda event, ex=ex: exercise(event=None, exer=a_exercise[ex]))
    print(a_exercise[ex])

# Buttons, display results, login & quit
btn_display = Button(window, text="Display results", font=("Arial", 15))
btn_display.grid(row=1 + 2 * len(a_exercise) // 3, column=1)
btn_display.bind("<Button-1>", lambda e: display_result(e))

# bouton Login
btn_Login = Button(window, text="Login", font=("Arial", 15))
btn_Login.grid(row=3 + 3 * len(a_exercise) // 3, column=1)
btn_Login.bind("<Button-1>", lambda event: login_window(window))

# bouton Register
btn_Register = Button(window, text="Register", font=("Arial", 15))
btn_Register.grid(row=4 + 3 * len(a_exercise) // 3, column=1)
btn_Register.bind("<Button-1>", lambda event: register_window(window))

# bouton Quit
btn_finish = Button(window, text="Quitter", font=("Arial", 15))
btn_finish.grid(row=2 + 2 * len(a_exercise) // 3, column=1)
btn_finish.bind("<Button-1>", quit)

# main loop
window.mainloop()
