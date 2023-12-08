'''
Auteur : Amine Kaddouri
Version : 1.0
Date : 27.11.2023
Description : insertion des élement de l'utilisateur dans la base de donnée
'''
import mysql.connector

# fonction qui permet de se connecter à la base de donnée
def open_db():
    return mysql.connector.connect(host='127.0.0.1', port='3306',
                                   user='root', password='', database='resultats',
                                   buffered=True, autocommit=True)

db_connection = open_db()


def save_game_bd(pseudo, exercise, date_hour, duration, nbtrials, nbsuccess):
    query = "INSERT INTO resultats (pseudo, exercice, DateHeure, Temps, nbTotal, nbOK) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (pseudo, exercise, date_hour, duration, nbtrials, nbsuccess))
    db_connection.commit()
    cursor.close()
