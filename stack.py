def infix_to_postfix(expression):
    stack= []
    result = ""
    priority = {'+':1, '-':1, '*':2, '/':2, '^':3}
    for char in expression:
        if char.isalnum():
            result+=char
        elif char =='(':
            stack.append(char)
        elif char == ')':
            while stack[-1]!='(':
                result += stack.pop()
            stack.pop()
        else:
            while stack and priority[char]<=priority.get(stack[-1], 0):
                result += stack.pop()
            stack.append(char)
    while stack:
        result += stack.pop()
    return result

def calculate_postfix(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                result = a + b
            elif char == '-':
                result = a - b
            elif char == '*':
                result = a * b
            elif char == '/':
                result = a / b
            stack.append(result)
    return stack[-1]

# Пример использования
#postfix_expression = "52+3*"
postfix_expression = input()
result = calculate_postfix(postfix_expression)
print(infix_to_postfix(postfix_expression))
print(result)

