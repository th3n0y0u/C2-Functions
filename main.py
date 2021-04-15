# get Name function
def getName():
  userName = input("Please tell me your name: ")
  # userName varaiable is specific to this function
  return userName

def greeting(name): # parameter variables are specific to the function
  print("Hi " + name)

greeting(getName())
greeting(getName())
greeting(getName())

# ask the user for two numbers
# num1 = int(input("Please input a number: "))
# num2 = int(input("Please input a number: "))

# write a function that takes num 1 and num2 as parameters
# print the sum

def numbers(numList):
  total = 0
  for i in numList:
    total += i 
  print("The sum is " + str(total))

numbers([1,2,3,4,5,6,7,8,9,10]) #55

# function for product
def multiplynumbers(numList):
  total = 1
  for i in numList:
    total *= i
  print("The product is " + str(total))

multiplynumbers([1,2,3,4,5,6,7,8,9,10])