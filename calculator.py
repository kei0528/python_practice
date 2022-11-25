def add (n1, n2) :
  return n1 + n2

def substract (n1, n2) :
  return n1 - n2

def multiply (n1, n2) :
  return n1 * n2

def divide (n1, n2) :
  return n1 / n2

operations = {
  "+" : add,
  "-" : substract,
  "*" : multiply,
  "/" : multiply,
}

num1 = float(input('What is the first number: '))

for operator in operations :
  print(operator)
  
num2 = float(input('What is the second number: '))

operation_key = input('Pick an operation from the line above: ')

print(f'{num1} {operation_key} {num2} = {operations[operation_key](num1, num2)}')