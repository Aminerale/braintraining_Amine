'''
Auteur : Amine Kaddouri
Version : 1.0
Date : 10.01.2024
Description : lorsque cet fenêtre se lance l'utilisateur peut se login si il est déja dans la base de donné et affiche des erreurs si il ne remplit pas certaine condition
'''

from tkinter import *
from functools import partial
import bcrypt
import database
from tkinter import messagebox
import tkinter as tk
import tkinter
# Fonction pour se connecter
def loginUser():
    # Vérifie si les champs ne sont pas vides
    username = loginPseudo.get()
    password = loginPassword.get()

    if not username or not password:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return

    db_connection = database.open_db()

    try:
        cursor = db_connection.cursor()
        query = "SELECT Password FROM users WHERE pseudo = %s"
        cursor.execute(query, (username,))
        user_data = cursor.fetchone()

        if user_data:

            stored_hashed_password = user_data[0]
            byte_db = bytes(stored_hashed_password,'utf-8')
            print(byte_db)
            entered_password = password
            byte_enterred = bytes(entered_password,'utf-8')
            print(byte_enterred)
            if bcrypt.checkpw(byte_enterred, byte_db):
                messagebox.showinfo("Succès", "Connexion réussie pour l'utilisateur: " + username)
            else:
                messagebox.showerror("Erreur", "Mot de passe incorrect.")
        else:
            messagebox.showerror("Erreur", "Utilisateur non trouvé.")
    except Exception as e:
        messagebox.showerror("Erreur", "Erreur lors de la connexion: " + str(e))
    finally:
        cursor.close()
        db_connection.close()

# Fonction qui va hasher le mot de passe

# Fenêtre
def window_login(parent):
    global loginPseudo, loginPassword


    window = tk.Toplevel(parent)
    window.title("Login")

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

    # Crée un cadre dans la fenêtre pour organiser les widgets
    frame = tkinter.Frame(window, bg=hex_color)

    # entrée du pseudo
    Label(frame, text="Pseudo", bg="white").grid(row=0, column=0, padx=10, pady=10)
    loginPseudo = StringVar()
    Entry(frame, textvariable=loginPseudo, width=20).grid(row=0, column=1, padx=10, pady=10)

    Label(frame, text="Mot de Passe").grid(row=1, column=0, padx=10, pady=10)
    loginPassword = StringVar()
    Entry(frame, textvariable=loginPassword, show='*', width=20).grid(row=1, column=1, padx=10, pady=10)

    # Bouton de connexion
    loginButton = Button(frame, text="Se Connecter", command=partial(loginUser))
    loginButton.grid(row=2, column=0, columnspan=2, pady=10)

    def quit(e):
        Tk.destroy(window)

    btn_logout = Button(frame, text="Logout")
    btn_logout.grid(row=3, column=0, columnspan=2, pady=10)
    btn_logout.bind("<Button-1>", quit)

    frame.pack()