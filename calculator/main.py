import art


# caluculator

def add(n1, n2):
     return n1 + n2

def subtract(n1, n2):
     return n1 - n2

def divide(n1, n2):
     return n1 / n2

def multiply(n1, n2):
     return n1 * n2

operations = {
     "+": add,
     "-": subtract,
     "*": multiply,
     "/": divide
}

art.print_logo()

num1 = int(input("First number?: "))
num2 = int(input("Second number?: "))
op = (input("Operation: "))

function = operations[op]
answer = function(num1, num2)
print(f"{num1} {op} {num2}  = {answer}")

num3 = int(input("New number?: "))
op = (input("New Operation: "))

function = operations[op]
new_answer = function(answer, num3)
print(f"{answer} {op} {num3}  = {new_answer}")
answer = new_answer
