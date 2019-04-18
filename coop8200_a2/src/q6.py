"""
-------------------------------------------------------
q6.py
testing
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2015-01-23
-------------------------------------------------------
"""
from course import Course

def read_course(line):
    """
    -------------------------------------------------------
    Creates and returns a Course object from a line of string data.
    Use: course = read_course(line)
    -------------------------------------------------------
    Preconditions:
        line - a comma-delimited line of Course data in the format
        "code,title,credit,term" (str)
    Postconditions:
        returns
        course - contains the data from line (Course)
    -------------------------------------------------------
    """
    line = line.split(",")
    c = Course(line[0], line[1], line[2], line[3])
    
    return c

def read_courses(file_variable):
    """
    -------------------------------------------------------
    Creates and returns a list of Course objects from a file variable.
    Use: courses = read_courses(file_variable)
    -------------------------------------------------------
    Preconditions:
        file_variable - a file variable, open for reading (file)
    Postconditions:
        returns
        courses - a list of Course objects (list of Course)
    -------------------------------------------------------
    """
    courses = []
    line = file_variable.readline()
    while line != "":
        s = read_course(line)
        courses.append(s)
        line = file_variable.readline()
    return courses

"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
f = open("courses.txt", "r", encoding= "utf-8")
print(read_courses(f))
f.close()