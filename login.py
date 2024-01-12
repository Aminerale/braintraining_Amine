from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

# Window
window = Tk()
window.geometry('400x200')
window.title('Login User')
# couleur de la fenetre
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color
window.configure(bg=hex_color)

# Entré de l'username
usernameLabel = Label(window, text="UserName").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(window, textvariable=username).grid(row=0, column=1)

# Mot de passe hachage et floutage
passwordLabel = Label(window,text="Mot de Passe").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(window, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

# Login button
loginButton = Button(window, text="Login", command=validateLogin).grid(row=4, column=0)

window.mainloop()