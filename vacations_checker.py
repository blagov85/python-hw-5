from datetime import date
from vacations_calendar import calendar

def check(date_str):
    if not(isinstance(date_str, str)):
        return 'Argument of function is not string'
    date_str = date_str.strip()
    if (len(date_str) == 0):
        return 'Argument of function is empty'
    
    dmY = date_str.split('/')
    if(len(dmY) != 3):
        return 'Argument of function must be date in format dd/mm/YYYY'
    for el in dmY:
        el = el.strip()
        if not(el.isdigit()):
            return 'Argument of function must be date'
    
    day = int(dmY[0])
    month = int(dmY[1])
    year = int(dmY[2])

    for holiday in calendar:
        dm = holiday.split('/')
        dayHoliday = int(dm[0])
        monthHoliday = int(dm[1])
        if date(year, month, day) == date(year, monthHoliday, dayHoliday):
            return calendar[holiday]
    return 'None'