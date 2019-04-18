"""
-------------------------------------------------------
q1.py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2015-01-27
-------------------------------------------------------
"""

from stack_array import Stack
OP = ['+', '-', '*', '/', '**', '%']
def postfix(s):
    """
    -------------------------------------------------------
    Evaluates a postfix expression string
    -------------------------------------------------------
    Preconditions:
       s - the postfix string to evaluate. Tokens are separated by
       spaces. Valid operators are +, -, *, /, **, %. Operands
       are assumed to be float. (str)
    Postconditions:
       Returns:
       answer - the result of evaluating s, None if the stack does
       not contain exactly one float value after evaluating s (float)
    -------------------------------------------------------
    """
    temp = ''
    stack = Stack()
    for i in range(len(s)):
        if s[i].isdigit() == True:
            temp += s[i]
        elif s[i] == " ":
            if s[i-1] not in OP:
                stack.push(temp)
                temp = ''
        elif s[i] in OP:
            value1 = str(stack.pop())
            value2 = str(stack.pop())
            answer = eval(value2 + s[i] + value1)
            stack.push(answer)
            temp = ''
    return answer
    
    
s = "1 2 4 * + 5 -"
print(postfix(s))