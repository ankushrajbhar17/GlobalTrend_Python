def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed and code by ankush rajbhar"
print(divide(10,2))
print(divide(10,0))#using 0 in this Line
