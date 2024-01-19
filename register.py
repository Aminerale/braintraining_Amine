'''
Auteur : Amine Kaddouri
Version : 1.0
Date : 10.01.2024
Description : L'utilisateur peut se créé un compte qui va être stocké dans la base de donnée puis pourra par la suite se login via une autre fenêtre
'''

from tkinter import *
from functools import partial
import bcrypt
import database
from tkinter import messagebox
import tkinter as tk
import tkinter

# Fonction pour s'enregistrer
def registerUser(pseudo, password):
    # Vérifie si les champs ne sont pas vides
    if not pseudo.get() or not password.get():
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return

    hashed_password = hash_password(password.get())
    db_connection = database.open_db()

    try:
        cursor = db_connection.cursor()
        query = "INSERT INTO users (pseudo, password) VALUES (%s, %s)"
        cursor.execute(query, (pseudo.get(), hashed_password))
        db_connection.commit()
        messagebox.showinfo("Succès", "Utilisateur enregistré avec succès.")
    except Exception as e:
        messagebox.showerror("Erreur", "Erreur lors de l'enregistrement de l'utilisateur: " + str(e))
    finally:
        cursor.close()
        db_connection.close()

# Fonction qui va hasher le mot de passe
def hash_password(password):
    password_bytes = password.encode('utf-8')
    hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')

# Fonction pour afficher la fenêtre
def window_register(parent):
    global registerPseudo, registerPassword

    window = tk.Toplevel(parent)
    window.title("Inscription Utilisateur")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcule les coordonnées pour centrer la fenêtre
    x_coordinate = (screen_width - 400) // 2
    y_coordinate = (screen_height - 200) // 2

    # Définit les coordonnées de la fenêtre
    window.geometry(f'400x200+{x_coordinate}+{y_coordinate}')


    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color
    window.configure(bg=hex_color)

    frame = tkinter.Frame(window, bg=hex_color)
    # entrée du pseudo
    Label(frame, text="Pseudo", bg="white").grid(row=0, column=0, padx=10, pady=10)
    registerPseudo = StringVar()
    Entry(frame, textvariable=registerPseudo, width=20).grid(row=0, column=1, padx=10, pady=10)

    # entrée du mot de passe
    Label(frame, text="Mot de Passe", bg="white").grid(row=1, column=0, padx=10, pady=10)
    registerPassword = StringVar()
    Entry(frame, textvariable=registerPassword, show='*', width=20).grid(row=1, column=1, padx=10, pady=10)

    # Bouton d'inscription
    registerButton = Button(frame, text="S'enregistrer", command=partial(registerUser, registerPseudo, registerPassword))
    registerButton.grid(row=2, column=0, columnspan=2, pady=10)

    frame.pack()
