import mysql.connector

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
