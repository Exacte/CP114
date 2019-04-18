"""
-------------------------------------------------------
valid_date.py
validate our wonderful days of birth
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2015-01-15
-------------------------------------------------------
"""
CURRENT_YEAR = 2015
MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_year(year):
    """
    -------------------------------------------------------
    confirms a year has once pasted through the present
    -------------------------------------------------------
    Preconditions:
       year - a string of a year that could possibly exist in our past time line
    Postconditions:
       returns:
       confirm - a boolean value confirming the existence of the year in our glorious history
    -------------------------------------------------------
    """
    confirm = False
    if len(year) == 4 and year.isdigit() == True and CURRENT_YEAR >= int(year):
        confirm = True 
    return confirm

def is_month(month):
    """
    -------------------------------------------------------
    month
    -------------------------------------------------------
    Preconditions:
       month - a string of a month that appears on the calendar
    Postconditions:
       returns:
       confirm - a boolean value confirming the precondition
    -------------------------------------------------------
    """
    confirm = False
    if len(month) == 2 and month.isdigit() == True  and 12 >= int(month) >= 1 :
        confirm = True 
    return confirm
        
def is_day(day):
    """
    -------------------------------------------------------
    day, week, thing, it does what expected
    -------------------------------------------------------
    Preconditions:
       day - a string of a day..... thats it
    Postconditions:
       returns:
       confirm - a boolean value confirming if its a day... yup a day!
    -------------------------------------------------------
    """
    confirm = False
    if len(day) == 2 and day.isdigit() == True  and 31 >= int(day) >= 1 :
        confirm = True 
    return confirm

def is_leap_year(year):
    """
    -------------------------------------------------------
    leap years for.. every 4 years
    -------------------------------------------------------
    Preconditions:
       year - a string of a year that could possibly exist in our past time line
    -------------------------------------------------------
    """
    if ((int(year) % 4) == 0 and (int(year) % 100) != 0) or (int(year) % 400) == 0:
        MONTHS[1] = 29

def is_iso_date(date):
    """
    -------------------------------------------------------
    validates if you were born or if your lying.
    -------------------------------------------------------
    Preconditions:
       date - a possible date in our wonderful time line
    Postconditions:
       returns:
       confirm - a boolean value confirming you were born
    -------------------------------------------------------
    """
    confirm = False
    if len(date) == 10:
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]
        if date[4] == date[7]:
            if int(month) == 2:
                if int(day) <= MONTHS[int(month)-1]:
                    if is_year(year) == True and is_month(month) == True and is_day(day) == True:
                        confirm = True
            else:
                if int(day) <= MONTHS[int(month)-1]:
                    if is_year(year) == True and is_month(month) == True and is_day(day) == True:
                        confirm = True
    return confirm