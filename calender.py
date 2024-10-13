def show_menu():
    print("What do you want?")
    print("Enter 1 for Whole year")
    print("Enter 2 for month of the year")
    print("Enter 3 for specific day of the year")
    print("Enter 4 for the exist")

def Whole_year():
    import calendar
    year=int(input("Enter a year: "))
    cal = calendar.calendar(year)
    print(cal)

def month_year():
    import calendar
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    cal=calendar.month(year,month)
    print(cal)

def day_year():
    import calendar
    year=int(input("Enter a year: "))
    month=int(input("Enter a month: "))
    day=int(input("Enter a day"))
    cal = calendar.weekday(year,month,day)
    days_weekend=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    print(days_weekend[cal])
    
def get_lost():
    print("Get lost from here")
        
while True:
    show_menu()
    choice = int(input("Enter a digit: "))
    if choice == 1:
        Whole_year()
    elif choice == 2:
        month_year()
    elif choice == 3:
        day_year()
    elif choice == 4:
        get_lost()
    else:
        print("Enter a correct digit")
    break