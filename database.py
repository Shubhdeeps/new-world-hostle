import sqlite3
from constants import list_items
from history import render_enteries


conn = sqlite3.connect('hostle.db')
cur = conn.cursor()

def run_database():
    global list_items
    global cur
    cur.execute("CREATE TABLE IF NOT EXISTS hostletable (name TEXT, booking_id INTEGER, country TEXT, passport TEXT, gender TEXT, date_from TEXT, date_to TEXT, room_type TEXT, room_number TEXT, unique (booking_id))")
    cur.execute('DELETE FROM hostletable;',)
    for item in list_items:
        try:
            data_tuple = (item["name"], item["booking_id"], item["country"], item["passport"], item["gender"],item["date_from"],item["date_to"],item["room_type"],item["room_number"])
            cur.execute("INSERT INTO hostletable VALUES" + str(data_tuple))
            conn.commit()
        except:
            pass


def get_database_enteries():
    global conn, cur, list_items
    data = cur.execute('SELECT * FROM hostletable')
    from residents import Resident
    for row in data:
        resident = Resident()
        resident.set_details_database(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        list_items.append(resident.get_details())
    render_enteries()


def delete_database_entry(booking_id):
    global conn
    conn = sqlite3.connect('hostle.db')
    cur = conn.cursor()
    delete_query = """DELETE FROM hostletable WHERE booking_id=""" + str(booking_id)
    cur.execute(delete_query)
    conn.commit()
    if conn:
        conn.close()

