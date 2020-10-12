import math

functions = [
  "add",
  "subtract",
  "multiply",
  "divide",
  "square",
  "square root"
]

def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

def square(num1):
  return num1 ** 2

def square_root(num1):
  return math.sqrt(num1)

while True:
  for index, opp in enumerate(functions, start=1):
    print(index,"-", opp)

  opp = input("Choose the operation, or type exit so exit>")

  if opp == 'exit':
    break
  
  num1 = float(input("Fist Number: "))


  if(int(opp) < 5):
    num2 = float(input("Second Number: "))

  if int(opp) > 0 or int(opp) < len(functions) + 1:
    if opp == "1":
      print(add(num1, num2), "\n")
    elif opp == "2":
      print(subtract(num1,num2), "\n")
    elif opp == "3":
      print(multiply(num1,num2), "\n")
    elif opp == "4":
      print(divide(num1,num2), "\n")
    elif opp == "5":
      print(square(num1), "\n")
    elif opp == "6":
      print(square_root(num1), "\n")
  else:
    print("Operation invalid")