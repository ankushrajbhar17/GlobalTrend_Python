def arithmetic_operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b if b != 0 else "Error: Division by zero."
    else:
        return "Error: Invalid operator."
print("I'm adding 2 number -",arithmetic_operation(5,5,"+"))
