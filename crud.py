'''
Auteur : Amine Kaddouri
Version : 1.0
Date : 12.12.2023
Description : Création de l'affichage du crud
'''

import tkinter as tk
from tkinter import *
from database import *
import geo01
from result import *

def open_window_crud():
    # parametre de la fenetre
    window = Tk()
    window.title("CRUD")
    window.geometry('1100x900')
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color
    window.configure(bg=hex_color)

    # frame
    frame1 = Frame(window)
    frame1.pack()
    frame2 = Frame(window)
    frame2.pack()
    frame3 = Frame(window)
    frame3.pack()
    frame4 = Frame(window)
    frame4.pack()


    # fonction pour ajouter un nouveau résultats
    def add_result():
        global entre1,entre2,entre3,entre4

        # label qui apparait quand la personne veut ajouter un résultat
        label = Label(frame1, text="CRUD", font=("Arial Bold", 20))
        label.pack()
        # label
        label2 = Label(frame2, text="pseudo")
        label2.grid(row=0, column=0)
        # entré
        entre1 = Entry(frame2)
        entre1.grid(row=0, column=1)

        label3 = Label(frame2, text="exercie")
        label3.grid(row=1, column=0)

        entre2 = Entry(frame2)
        entre2.grid(row=1, column=1)

        label4 = Label(frame2, text="DateDébut")
        label4.grid(row=2,column=0)

        entre3 = Entry(frame2)
        entre3.grid(row=2, column=1)

        label5 = Label(frame2, text="DateFin")
        label5.grid(row=3, column=0)

        entre4 = Entry(frame2)
        entre4.grid(row=3, column=1)

        # requete sql qui va crée les resultats dans la db
        def create_new_result():
            create = f" values ('{entre1.get()}', '{entre2.get()}', '{entre3.get()}', '{entre4.get()}')"
            query = ("insert into result (name, exercise, date_hour, duration)")
            query = query + create
            print(query)
            cursor = db_connection.cursor()
            cursor.execute(query, )

        bouton_create = tk.Button(frame3, text="create", command=create_new_result)
        bouton_create.pack()

    open_window_crud()
    add_result()
    window.mainloop()




