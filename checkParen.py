from stack import Stack

def is_matched(p1,p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False



def isBalanced(paren_string):
    s = Stack()
    index = 0
    isOrder = True

    while index < len(paren_string) and isOrder:
        paren = paren_string[index]
        if paren in '([{':
            s.push(paren)
        else:
            if not s.isEmpty():
                top = s.remove()
                if not is_matched(top, paren):
                    isOrder = False
            else:
                isOrder = False

        index +=1

    if isOrder and s.isEmpty():
        return True
    else:
        return False


print(isBalanced('{}]'))
