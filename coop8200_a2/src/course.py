"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2015-01-21
-------------------------------------------------------
"""
class Course:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    
    CODENUM = ["1","2","3","4"]
    TERMNUM = ["01", "05", "09"]
    TERM = ["Winter", "Spring", "Fall"]
    CREDIT = [0.25, 0.5, 1.0]
    
    def __init__(self, code, title, credit, term):
        
        """
        -------------------------------------------------------
        Initializes the Course values.
        Use: c = Course( code, title, term )
        -------------------------------------------------------
        Preconditions:
          code - 5 character course code in the form 'XXnnn' where
          'XX' are upper case letters and 'nnn' are digits, with the
          first digit from 1 to 4 inclusive (str)
          title - course title (str)
          credit - credit value of course, one of 0.25, 0.5, or 1.0 (float)
          term - term course is offered in the form 'YYYYSS' where
          'YYYY' is a year and 'SS' is a season, one of '01', '05', '09' (str)
        Postconditions:
          Course attributes are initialized.
        -------------------------------------------------------
        """
        
        assert code[2] in Course.CODENUM, \
            "first number must be one of {}.".format(Course.CODENUM)

        assert len(code) == 5 and code[:1].isalpha() and code[2:].isdigit(), \
            "Must be in format XXnnn, where X is a upper case letter and n is a number."
        assert title[0].isalpha() and title[1].isalpha(), \
            "Course title must only consist of letters."
        assert float(credit) in Course.CREDIT, \
            "credit value must be one of {}.".format(Course.CREDIT)
        assert term[4:6] in Course.TERMNUM, \
            "term must be in form YYYYSS, where SS is one of {}". format(Course.TERMNUM)
        
        self.code = code
        self.title = title
        self.credit = credit
        self.term = term
        
        return
    
    def _term_name(self):
        """
        -------------------------------------------------------
        Generates and returns a text version of a term code.
        Use: term_name = c._term_name()
        -------------------------------------------------------
        Postconditions:
          returns
          result - the term name in the form 'YYYY Season' where 'YYYY'
          is a four digit year, and 'Season' is one of 'Winter', 'Spring',
          or 'Fall' as appropriate (str)
        -------------------------------------------------------
        """
        
        year = self.term[0:3]
        season = self.term[4:]
        if season == self.TERMNUM[1]:
            result = "{}{}".format(year, self.TERM[0])
            
        elif season == self.TERMNUM[2]:
            result = "{}{}".format(year, self.TERM[1])
            
        else:
            result = "{}{}".format(year, self.TERM[2])
            
        return result
    
    def __str__(self):
        """
        -------------------------------------------------------
        Returns a string version of a course in the format
        course code: title (credit) - term name
        Use: print( "{}".format(s))
        -------------------------------------------------------
        Postconditions:
          returns
          string - a formatted version of the course data (str)
        -------------------------------------------------------
        """
        
        string = "{}: {} ({}) - {}".format(self.code, self.title, self.credit, self._term_name())
        return string
    
    def __eq__(self, rhs):
        """
        -------------------------------------------------------
        Compares against another course for equality.
        Use: c1 == c2
        -------------------------------------------------------
        Preconditions:
          rhs - [right hand side] course to compare to (Course)
        Postconditions:
          returns
          result - True if course IDs match, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = False
        
        if self.code == rhs.code:
            result = True
            
        return result
    
    def __lt__(self, rhs):
        """
        -------------------------------------------------------
        Determines if this course precedes another.
        If course IDs don't match (using already defined == operator),
        compares courses by code then by term.
        Use: c1 < c2
        -------------------------------------------------------
        Preconditions:
          rhs - [right hand side] course to compare to (Course)
        Postconditions:
          returns
          result - True if course less than rhs, False otherwise (boolean)
        -------------------------------------------------------
        """
        
        if self == rhs:
            result = False
        else:
            result = (self.code.lower(), self.term.lower()) < (rhs.code.lower(), rhs.term.lower())
        
        return result
    def __le__(self, rhs):
        """
        -------------------------------------------------------
        Determines if this course precedes is or equal to another.
        Uses already defined == and < operators.
        Use: c1 <= c2
        -------------------------------------------------------
        Preconditions:
          rhs - [right hand side] course to compare to (Course)
        Postconditions:
          returns
          result - True if course less than or equal to rhs,
          False otherwise (boolean)
        -------------------------------------------------------
        """
        
        result = (self == rhs or self < rhs)
        return result
    
    def write(self, file_variable):
        """
        -------------------------------------------------------
        Writes this course to a comma-delimited open file.
        Use: s.write( file_variable )
        -------------------------------------------------------
        Preconditions:
          file_variable - a file variable, open for writing or appending (file)
        Postconditions:
          writes the contents of this course to file_variable with each line in
          the format "code,title,credit,term"
        -------------------------------------------------------
        """
        file_variable.write(",".join(map(str, [self.code, self.title, self.credit,  self.term])))
        
        
