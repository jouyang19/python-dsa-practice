"""
Stack: Parentheses Balanced ( ** Interview Question)
Check to see if a string of parentheses is balanced or not.

By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order. For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string. On the other hand, the string "(()))" has an imbalance, as the last two parentheses do not match, so it is not balanced.  Also, the string ")(" is not balanced because the close parenthesis needs to follow the open parenthesis.

Your program should take a string of parentheses as input and return True if it is balanced, or False if it is not. In order to solve this problem, use a Stack data structure.

Function name:
is_balanced_parentheses

Remember: this is not a method within the Stack class, this is a separate function.  Indent all the way to the left.
"""

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()



# WRITE IS_BALANCED_PARENTHESES FUNCTION HERE #
#                                             #
#    This is a separate function that is      #
#    not a method within the Stack class.     #
#    Indent all the way to the left.          #
#                                             #
###############################################
def is_balanced_parentheses(string):
    my_stack = Stack()
    for p in string:
        if p == '(':
            my_stack.push(p)
        elif p == ')':
            if my_stack.is_empty():
                return False
            my_stack.pop()

    return my_stack.is_empty()
    
is_balanced_parentheses('((()))())')

def test_is_balanced_parentheses():
    try:
        assert is_balanced_parentheses('((()))') == True
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        assert is_balanced_parentheses('()') == True
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        assert is_balanced_parentheses('(()())') == True
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert is_balanced_parentheses('(()') == False
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert is_balanced_parentheses('())') == False
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        assert is_balanced_parentheses(')(') == False
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

    try:
        assert is_balanced_parentheses('') == True
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        assert is_balanced_parentheses('()()()()') == True
        print('Test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

    try:
        assert is_balanced_parentheses('(())(())') == True
        print('Test case 9 passed')
    except AssertionError:
        print('Test case 9 failed')

    try:
        assert is_balanced_parentheses('(()()())') == True
        print('Test case 10 passed')
    except AssertionError:
        print('Test case 10 failed')

    try:
        assert is_balanced_parentheses('((())') == False
        print('Test case 11 passed')
    except AssertionError:
        print('Test case 11 failed')

# test_is_balanced_parentheses()

"""
The function creates a new stack using the Stack() class, and then iterates through each character in the input string using a for loop.

For each character, the function checks if it is an opening parenthesis, represented by the ( character. If it is an opening parenthesis, the function pushes it onto the stack using the push method of the stack.

If the character is a closing parenthesis, represented by the ) character, the function checks if the stack is empty or if the top of the stack, which is the most recent opening parenthesis that has not been closed, is not an opening parenthesis. If either of these conditions is true, the function returns False because the parentheses are not balanced.

If the top of the stack is an opening parenthesis, the function pops it from the stack using the pop method of the stack. The function continues iterating through the input string until all characters have been processed.

After processing all the characters, the function returns True if the stack is empty, which indicates that all opening parentheses have been matched with a closing parenthesis, and False otherwise.



Big O:

Time Complexity

The for loop iterates through each character in parentheses, making it O(n).

The stack.push() and stack.pop() operations are O(1).

Combining these, the overall time complexity is O(n).



Space Complexity

In the worst case, the stack could store all opening parentheses, making it O(n).







Code with inline comments:



def is_balanced_parentheses(parentheses):
    # Create a new stack
    stack = Stack()
 
    # Iterate over each character in the string
    for p in parentheses:
        # If the character is an opening parenthesis, 
        # push it onto the stack
        if p == '(':
            stack.push(p)
        # If the character is a closing parenthesis, 
        # pop the top element off the stack
        # and check if it matches the opening parenthesis
        elif p == ')':
            # If the stack is empty or the top element 
            # is not an opening parenthesis,
            # the parentheses are not balanced
            if stack.is_empty() or stack.pop() != '(':
                return False
 
    # If the stack is empty, the parentheses are balanced
    return stack.is_empty()

"""