import csv 
from constants import list_items
from display_message import Popup
from constants import window

def write_csv():
    global list_items
    csvfile = open('resident.csv', 'w', newline = '')
    riter = csv.writer(csvfile, delimiter = ',')
    riter.writerow(['Name', 'Booking Id', 'Country', 'Passport Number', 'Gender', 'Check In', 'Check Out', 'Room Type', 'Room Number'])
    for item in list_items:
        riter.writerow(list(item.values()))
    csvfile.close()
    messagebox1 = Popup(window, "Exported", "Successfully exported CSV file")
    messagebox1.flex_box()

def write_text():
    global list_items
    textfile = open('resident.txt', 'w', newline = '')
    riter = csv.writer(textfile, delimiter = ',')
    riter.writerow(['Name', 'Booking Id', 'Country', 'Passport Number', 'Gender', 'Check In', 'Check Out', 'Room Type', 'Room Number'])
    for item in list_items:
        riter.writerow(list(item.values()))
    textfile.close()
    messagebox1 = Popup(window, "Exported", "Successfully exported TEXT file")
    messagebox1.flex_box()

def read_csv():
    from constants import single_rooms, double_rooms, female_dorms, male_dorms
    for x in list_items:
        if(x['room_type'] == 'male dorm'):
            male_dorms.append(x["room_number"])
        if(x['room_type'] == 'female dorm'):
            female_dorms.append(x["room_number"])
        if(x['room_type'] == 'single room'):
            single_rooms.append(x["room_number"])
        if(x['room_type'] == 'double room'):
            double_rooms.append(x["room_number"])
    list_items.clear()
    try:
        file = open('importable.csv')
        csvfile = csv.reader(file, delimiter=',')
        from residents import Resident
        from history import render_enteries
        for row in csvfile:
            print(row)
            resident = Resident()
            resident.set_details_database(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            list_items.append(resident.get_details())
        render_enteries()
        file.close()
        messagebox1 = Popup(window, "Imported", "importable.csv successfully inported")
        messagebox1.flex_box()
    except:
        messagebox1 = Popup(window, "Error", "Failed to import file")
        messagebox1.flex_box()

def about_application():
    messagebox1 = Popup(window, "About Application", "Application name is New World Hostle. Version 1.0.0")
    messagebox1.flex_box()


def developer_information():
    messagebox1 = Popup(window, "About Developers", "The Application is created by Shubhdeep Singh. website: https://shubhdeeps.github.io/ss/")
    messagebox1.flex_box()