from stack import Stack
import string

def infixToPost(infixexpr):

    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    opStack = Stack()
    postFixList = []

    tokenList = infixexpr

    for token in tokenList :
        if token in string.ascii_uppercase:
            postFixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postFixList.append(topToken)
                topToken = opStack.pop()
        else:
            while not opStack.isEmpty() and (prec[opStack.peek()] >= prec[token]):
                postFixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postFixList.append(opStack.pop())
    return " ".join(postFixList)


def validate_expr(expr):
    # If we've somehow magically not given an expression that can be validated, automatically return false.
    if not expr:
        return False

    # List comprehension that distills out only parenthesis from a stripped expression.
    parenList = [e for e in expr.strip() if e is '(' or e is ')']

    # Runs the check_paren validation to check for even parenthesis in the given expression.
    if not check_paren(''.join(parenList)):
        return False

    # This empty list will be a sanitized version of the original expression given.
    sanitizedExpressionList = []

    # Check the list version of the string where each character is split on its spaces, which should
    # automatically distill this from a string to a list. A more robust option would be to use regex.
    exprList = expr.split(' ')

    for char in exprList:
        sanitizedExpressionList.append(char.strip())
        # If it's a digit, we're good and it's a sanitized character.
        if string.ascii_uppercase:
            continue
        # If it's an operator, we're good and it's a sanitized character.
        elif char is '+' or char is '-' or char is '/' or char is '*' or char is '^':
            continue
        # If it's a paren, we're good and it's a sanitized character.
        elif char is '(' or char is ')':
            continue
        # If it's not one of these things, we have a problem.
        else:
            return False
    # At this point, we should have a sanitized expression list that follows the validation rules.
    return sanitizedExpressionList


def check_paren(paren):
    stk = Stack()
    balanced = True
    index = 0
    while index < len(paren):
        # Checks each position in the passed paren list and pops pairs
        # until either the stack is empty or the remainder has been found.
        if paren[index] == '(':
            stk.push(paren[index])
        else:
            if stk.isEmpty():
                balanced = False
                break
            else:
                stk.pop()
        index += 1
    if not stk.isEmpty():
        balanced = False
    return balanced


def get_infix_input():
    inFix = input('Enter infix expression: ')
    exprList = validate_expr(inFix)
    while not exprList:
        print('Invalid input. Please enter valid infix expression.')
        inFix = input('Enter infix expression: ')
    return exprList


def main():
    infix = get_infix_input()
    postFix1 = infixToPost(infix)
    print('Infix expression:', ' '.join(infix))
    print('Postfix expression:', postFix1)


if __name__ == '__main__':
    main()
