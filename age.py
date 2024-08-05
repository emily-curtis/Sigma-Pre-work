from datetime import datetime
def calculate_years(user_date):
    date = datetime.strptime(user_date, '%d-%m-%Y')
    now = datetime.today()
    if (now.month, now.day) < (date.month, date.day):
        age = now.year - date.year - 1
    elif (now.month, now.day) >= (date.month, date.day):
        age = now.year - date.year
    return age        

user_date = input("Please enter a date in the format dd-mm-yyyy: ")
total_time = calculate_years(user_date)
print("The total time between then and now is: {}".format(total_time))