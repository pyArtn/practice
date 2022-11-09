import datetime

def valid_braces(string):
    start = datetime.datetime.now()
    stack = []
    for i in string:
        if i in ("(", "{", "["):
            stack.append(i)
        elif i in (")", "}", "]"):
            try:
                if stack[-1]+i in ("{}", "[]", "()"):
                    stack.pop()
            except IndexError:
                return False
    print(datetime.datetime.now()-start)
    if len(stack) == 0:
        return True
    return False

print(valid_braces("([{}])()([{}])()([{}])()([{}])()([{}])()([{}])()([{}])()([{}])()([{}])()([{}])()([{}])()([{}])()([{}])()([{}])()([{}])()([{}])()([{}])()([{}])()"))
print(valid_braces("[(])"))