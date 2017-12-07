from stack import Stack
import string

def infixToPost(infixexpr):

    prec ={}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    opStack = Stack()
    postFixList = []

    tokenList = infixexpr.split()

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

def main():
    inFix1 = "( A + B ) * ( C + D )"
    postFix1 = infixToPost(inFix1)
    print(postFix1)
main()

