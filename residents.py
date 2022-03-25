
class Person:
    def __init__(self, booking_id, name, country):
        self.booking_id = booking_id
        self.name = name
        self.country = country
    
    def getEntries(self):
        return{
            "booking_id" : self.booking_id,
            "name": self.name,
            "country": self.country
        }



h1 = Person(12221, "John Smith", "Estonia")
h2 = Person(22221, "Tim Smith", "Estonia")
h3 = Person(32221, "Nay Smith", "Estonia")
h4 = Person(42221, "Mob Smith", "Estonia")
h5 = Person(52221, "Sohn Smith", "Estonia")

# enteries should not exeed 5
entries = [h1.getEntries(), h2.getEntries(), h3.getEntries(), h4.getEntries(), h5.getEntries()]

def delete_resident_entry(booking_id):
    global entries
    delete = _entry_to_be_del(booking_id)
    entries.remove(delete)
    return booking_id

def get_enteries():
    global entries
    return entries

def _entry_to_be_del(booking_id):
    global entries
    for x in entries:
        if(x["booking_id"] == booking_id):
            return x
    
    