from datetime import datetime

def check_birthdate(year, month, day):
    today = datetime(2020,1,26)
    birthdate = datetime(year,month,day)
    if today > birthdate:
        return True
    return False

def calculate_age(year, month, day):
    today = datetime(2020,1,26)
    birthdate = datetime(year,month,day)
    age_of_user = int((today-birthdate).days /365)
    print("you are %s year old" %(age_of_user))



year=int(input("enter your year"))
month=int(input("enter your month"))
day=int(input("enter your day"))
if check_birthdate(year,month,day) == True:
    calculate_age(year,month,day)
else:
    print("Invalid birthdate")

