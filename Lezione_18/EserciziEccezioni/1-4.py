'''Database of dates:  Write a class that manages a database of dates with the format gg.mm.aaaa implementing methods to add a new date, 
delete a given date, modify a date, and perform a query on a given date is required.  A query on a given date allows for retrieving a given new date. 
Note that a date is an object for your database; it must be instantiated from a string.'''

class InvalidFormat(Exception):
    """Wrong date format"""
    
class DateAlreadyIn(Exception):
    """Date inside dates already"""

class DateNotFound(Exception):
    """Date not found"""

class DateInvalid(Exception):
    """Date invalid"""

class Database:
    
    def __init__(self):
        self.dates = []

    def check_date(self, date: str = None) -> bool:
        
        #Check if no input
        if date is None:
            raise DateNotFound("Date must be provided")

        #Check type
        if type(date) != str:
            raise InvalidFormat("Date must be provided in str format")

        #Check format
        if len(date) != 10 or date[2] != "." or date[5] != ".":
            raise InvalidFormat("Use gg.mm.aaaa format")

        gg = date[:2]
        mm = date[3:5]
        aaaa = date[6:]

        #Check all numbers
        if not gg.isdigit() or not mm.isdigit() or not aaaa.isdigit():
            raise InvalidFormat("Use gg.mm.aaaa format")

        #Create variables for gg mm aaaa
        gg = int(gg)  
        mm = int(mm)  
        aaaa = int(aaaa) 

        #Check full date
        if gg < 1 or gg > 31: 
            raise DateInvalid("Invalid day")
        if mm < 1 or mm > 12:
            raise DateInvalid("Invalid month")
        if aaaa < 1 or aaaa > 9999:  
            raise DateInvalid("Invalid year")
        
        #Check month 30 days
        if mm in [4, 6, 9, 11] and gg > 30:
            raise DateInvalid("Invalid day for this month")
        
        #Check february
        if mm == 2:
            if (aaaa % 4 == 0 and aaaa % 100 != 0) or (aaaa % 400 == 0):
                if gg > 29:
                    raise DateInvalid("Invalid day for february")
            elif gg > 28:
                raise DateInvalid("Invalid day for february")

        return True  

    def query_date(self, date: str = None):
        
        #Check if date in dates and print date found
        try:
            self.check_date(date)
            
            if date in self.dates:
                print(f"Date found: {date}")
            else:
                raise DateNotFound(f"Date {date} not found")
        
        except (InvalidFormat, DateInvalid, DateNotFound) as x:
            print(f"Error: {x}")

    def add_date(self, date: str = None):
        
        #Check if date already in dates and add date
        try:    
            self.check_date(date)
            
            if date not in self.dates:    
                self.dates.append(date)
                print(f"Date {date} added")
            else:
                raise DateAlreadyIn(f"Date {date} already in dates")
        
        except (DateAlreadyIn, InvalidFormat, DateInvalid, DateNotFound) as x:
            print(f"Error: {x}")

    def delete_date(self, date: str = None):
       
        #Check if date in dates and remove date 
        try:    
            self.check_date(date)
        
            if date in self.dates:
                self.dates.remove(date)
                print(f"Date {date} deleted")
            else:
                raise DateNotFound(f"Date {date} not found")
       
        except (DateNotFound, InvalidFormat, DateInvalid) as x:
            print(f"Error: {x}")
    
    def modify_date(self, old_date: str = None, new_date: str = None):
        
        #Check if old date in dates and update to new date
        try:
            self.check_date(old_date)
            self.check_date(new_date) 
        
            if old_date in self.dates:
                for i in range(len(self.dates)):
                    if self.dates[i] == old_date:
                        self.dates[i] = new_date  
                        print(f"Date {old_date} updated to {new_date}")
                        return 
            else:
                raise DateNotFound(f"Date {old_date} not found")

        except (DateNotFound, InvalidFormat, DateInvalid, DateAlreadyIn) as x:
            print(f"Error: {x}")
    




x = Database()

x.add_date("05.10.1998")  
x.add_date("05.09.1959")  
x.add_date("12.09.1992")  
x.add_date("05.12.1")
x.add_date("asjhf")  
x.add_date(23)  
x.add_date("33/22/1111")  
x.add_date("12/12/1234") 
x.add_date("31.12.1845") 
x.add_date(345) 
x.add_date() 
x.add_date("31.2.1")
x.add_date("01.12.1212")

x.modify_date("05.09.1959", "12.12.2022") 
x.modify_date(2, "12.12.2022")  
x.modify_date("31.12.1845", "31.12.2025")  
x.modify_date()
x.modify_date(23)
x.modify_date("23.13.0")

x.delete_date("31.12.1845") 
x.delete_date(2)  
x.delete_date("22.11.2222")  

x.query_date("05.10.1998")  
x.query_date(17)  
x.query_date("88.13.0")  
x.query_date("12.12.1212")  
x.query_date()
x.add_date(False)
x.add_date(x)