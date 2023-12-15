'''
Auteur : Amine Kaddouri
Version : 1.0
Date : 27.11.2023
Description : Création de l'affichage des résultat du joueur entré
'''
import tkinter as tk
from tkinter import *
import database
import geo01
import crud

db_connection = database.db_connection

# cette fonction va prendre les données dans la bd qui va etre ensuite utiliser dans la fonction suivante
def select_data():
    query = ("select pseudo, exercice, DateHeure, Temps, nbTotal, nbOK from resultats")
    cursor = db_connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data

# fonction pour créé le tableau pour afficher les résultats

def display(mytuple):
    global frame5
    for line in range(0, len(mytuple)):
        for col in range(0, len(mytuple[line])):
            (tk.Label(frame5, text=mytuple[line][col], width=15, font=("Arial", 10)).grid(row=line+1, column=col,padx=2, pady=2))

# fonction qui va prendre ce que l'utilisateur à écrit dans les entrés
def select_data_2(pseudo, exercice, date_debut, date_fin):
    query = "SELECT pseudo, exercice, DateHeure, Temps, nbTotal, nbOK FROM resultats WHERE pseudo = '' AND exercice = '' AND DateHeure >= '' AND DateHeure <= ''"
    cursor = db_connection.cursor()
    cursor.execute(query, (pseudo, exercice, date_debut, date_fin))
    data = cursor.fetchall()
    return data

# fonction pour afficher le total des résultats en bas
def data_total(a):
    if entre1.get() == "":
        query = ("select count(id), SEC_TO_TIME(SUM(TIME_TO_SEC(result.Temps))), sum(nbTotal) ,sum(nbOK) from result")
        cursor = db_connection.cursor()
        cursor.execute(query)
        total = cursor.fetchall()
        return total
    else:
        query = ("select count(id), SEC_TO_TIME(SUM(TIME_TO_SEC(result.Temps))), sum(nbTotal) ,sum(nbOK) from result where pseudo = (%s)")
        cursor = db_connection.cursor()
        cursor.execute(query, (a,))
        total = cursor.fetchall()
        return total

# fonction avec tout les parametres de la fenetre
def open_window_result(window):
    global frame5, label7, label8, label9, label10, label11, label12,entre1, entre2, entre3, entre4

    # parametre de la fenetre
    window = Tk()
    window.title("Affichage braintraining")
    window.geometry('1100x900')

    # frame
    frame1 = Frame(window)
    frame1.pack()
    frame2 = Frame(window)
    frame2.pack()
    frame3 = Frame(window, background="white")
    frame3.pack()
    frame4 = Frame(window)
    frame4.pack()
    frame8 = Frame(window)
    frame8.pack()

    frame5 = Frame(window)
    frame5.pack()
    frame6 = Frame(window)
    frame6.pack()
    frame7 = Frame(window)
    frame7.pack()
    frame9 = Frame(window)
    frame9.pack()

    # couleur de la fenetre
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color
    window.configure(bg=hex_color)

    # Premier label de titre
    label = Label(frame1, text="TRAINING : AFFICHAGE", font=("Arial Bold", 20))
    label.pack()

    # entré de l'utilisateur
    label2 = Label(frame3, text="Pseudo:")
    label2.pack(side = LEFT)

    entre1 = Entry(frame3)
    entre1.pack(side = LEFT)

    label3 = Label(frame3, text="Exercice:")
    label3.pack(side=LEFT)

    entre2 = Entry(frame3)
    entre2.pack(side=LEFT)

    label4 = Label(frame3, text="Date début:")
    label4.pack(side=LEFT)

    entre3 = Entry(frame3)
    entre3.pack(side=LEFT)

    label5 = Label(frame3, text="Date fin:")
    label5.pack(side=LEFT)

    entre4 = Entry(frame3)
    entre4.pack(side=LEFT)

    # Bouton pour voir le résultat

    label6 = Label(frame7, text="Total",font=("Arial Bold", 15))
    label6.pack(side=LEFT)

    label7 = Label(frame5, text="Elève",font=("Arial Bold",13))
    label7.grid(row=0,column=0)

    label8 = Label(frame5, text="Exercie",font=("Arial Bold",13))
    label8.grid(row=0,column=1)

    label9 = Label(frame5, text="Date Heure",font=("Arial Bold",13))
    label9.grid(row=0,column=2)

    label10 = Label(frame5, text="Temps",font=("Arial Bold",13))
    label10.grid(row=0,column=3)

    label11 = Label(frame5, text="nb Total",font=("Arial Bold",13))
    label11.grid(row=0,column=4)

    label12 = Label(frame5, text="nb Ok",font=("Arial Bold",13))
    label12.grid(row=0,column=5)

    # affiche l'utilisateur entré
    def entry_player(e):
        for widget in frame5.winfo_children():
            widget.grid_forget()

        # Récupérer les entrées des utilisateurs
        pseudo = entre1.get()
        exercice = entre2.get()
        date_debut = entre3.get()
        date_fin = entre4.get()

        # Convertir les chaînes vides en None
        pseudo = pseudo if pseudo else None
        exercice = exercice if exercice else None
        date_debut = date_debut if date_debut else None
        date_fin = date_fin if date_fin else None

        # Utilise les valeurs récupérées dans la fonction select_data_2
        data = select_data_2(pseudo, exercice, date_debut, date_fin)
        display(data, frame5)

        total = data_total(pseudo)
        display(total, frame9)


    # Bouton pour voir le résultat
    bouton = Button(frame4, text="Voir résultats", command=entry_player)
    bouton.pack(side=LEFT)


    # fonction pour ouvrir la fenetre
    def display_crud(event):
        crud.open_window_crud(window)


    # affichage du tableau des résultats
    select_data()
    data = select_data()
    display(data)

    # affichage du tableau du total
    entry_player(e)
    total = data_total()
    display(total)
    window.mainloop()