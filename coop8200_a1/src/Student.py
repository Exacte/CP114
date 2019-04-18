"""
-------------------------------------------------------
Student class definition.
Stores simple student data.
-------------------------------------------------------
Author:  mason cooper
ID:  140328200
Email:   coop8200@wlu.ca
Version: 2015-01-15
-------------------------------------------------------
"""
import valid_date

class Student:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    GENDERS = ("F", "M", "T")  # Define allowed gender values.

    def __init__(self, student_id, surname, forename, gender, birth_date):
        """
        -------------------------------------------------------
        Initializes the student values.
        Use: s = Student( student_id, surname, forename, gender, birth_date )
        -------------------------------------------------------
        Preconditions:
          student_id - 9 digit student ID (str)
          surname - student family (str)
          forename - student given name (str)
          gender - student gender [a character in GENDER] (str)
          birth_date - a student birth date of the form YYYY/MM/DD (str)
        Postconditions:
          Student attributes are initialized.
        -------------------------------------------------------
        """
        assert gender in Student.GENDERS, \
            "Gender must be one of {}".format(Student.GENDERS)
        assert len(student_id) == 9 and student_id.isdigit(), \
            "Student ID must be a 9 digit string"
        assert valid_date.is_iso_date(birth_date), "Invalid birth date."

        self.student_id = student_id
        self.surname = surname
        self.forename = forename
        self.gender = gender
        self.birth_date = birth_date
        return

    def __str__(self):
        """
        -------------------------------------------------------
        Returns a string version of a student in the format
        surname, forename, gender: student ID
        Use: print( "{}".format(s))
        -------------------------------------------------------
        Postconditions:
          returns
          string - a formatted version of the student data (str)
        -------------------------------------------------------
        """
        string = """{}
{}, {}
{}, {}""".format(self.student_id, self.surname,
            self.forename, self.gender, self.birth_date,)
        return string

    def __eq__(self, rhs):
        """
        -------------------------------------------------------
        Compares against another student for equality.
        Use: s1 == s2
        -------------------------------------------------------
        Preconditions:
          rhs - [right hand side] student to compare to (student)
        Postconditions:
          returns
          result - True if student IDs match, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = self.student_id == rhs.student_id
        return result

    def __lt__(self, rhs):
        """
        -------------------------------------------------------
        Determines if this student precedes another.
        If student IDs don't match (using already defined == operator),
        compares students by name then by ID.
        Use: s1 < s2
        -------------------------------------------------------
        Preconditions:
          rhs - [right hand side] student to compare to (student)
        Postconditions:
          returns
          result - True if student less than rhs, False otherwise (boolean)
        -------------------------------------------------------
        """
        if self == rhs:
            result = False
        else:
            # Compare the data values by putting them into tuples.
            result = \
            (self.surname.lower(), self.forename.lower(), self.birth_date) < \
            (rhs.surname.lower(), rhs.forename.lower(), rhs.birth_date)
        return result

    def __le__(self, rhs):
        """
        -------------------------------------------------------
        Determines if this student precedes is or equal to another.
        Uses already defined == and < operators.
        Use: s1 <= s2
        -------------------------------------------------------
        Preconditions:
          rhs - [right hand side] student to compare to (student)
        Postconditions:
          returns
          result - True if student less than or equal to rhs,
          False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self == rhs or self < rhs)
        return result
    
def get_student():
    """
    -------------------------------------------------------
    Ask the user to input student information from the keyboard.
    Use: s = get_student()
    -------------------------------------------------------
    Postconditions:
        returns
        student - contains the data from the keyboard (Student)
    -------------------------------------------------------
    """
    student_id = input("Student ID: ")
    surname = input("Surname Name: ")
    forname = input("Given Name: ")
    gender = input("Gender: ")
    birth_date = input("Birth Date: ")
    student = Student(student_id, surname, forname, gender, birth_date)
    return student
print(get_student())