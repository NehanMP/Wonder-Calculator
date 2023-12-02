# Creating Variables
from xmlrpc.client import boolean

endProgram = False

# Main Menu
print("           WONDER CALCULATOR")
print("           =================")
print("1. Enter positive integer numbers.")
print("2. Display Highest value.")
print("3. Display Lowest value.")
print("4. Display Average value.")
print("5. Display Even numbers.")
print("6. Exit")

# Process
operation = input("Please indicate your option : ")
if(operation == "6"):
  exit()

while (endProgram == False):
  count = 1
  num = 0
  validNum = False
  inputArr = []
  enterNewNumbers = False
  
  while(operation != "1"):
    operation = input("Error! Please enter the first option to input numbers : ")
  if(operation == "1"):
    num = int(input("How many numbers do you want to input? : "))

  while (validNum == False):
    if (num > 0 and num  <= 10):
      validNum = True
    else:
      num = int(input("Error! Maximum numbers that can be entered is 10. Please enter a valid number : "))

  while (count<=num):
    inputArr.append(int(input("Enter a number : ")))
    count = count + 1

  maxValue = inputArr[0]
  minValue = inputArr[0]
  sum = 0

  for x in inputArr:
    if (x > maxValue):
      maxValue = x

    if (x < minValue):
      minValue = x

    sum = sum + x

  avgValue = sum/num

  while (enterNewNumbers == False):
    control = False
    operation = input("Please indicate your option (2/3/4/5): ")
    while(control == False):
    
     if (operation == "2"):
      control = True
      print("Max value: " + str(maxValue))
     elif (operation == "3"):
      control = True
      print("Min value: " + str(minValue))
     elif(operation == "4"):
      control = True
      print("Average value: " +  str(format(avgValue,".2f")))
     elif (operation == "5"):
      control = True
      print("Even numbers: ",end = '')
      for x in inputArr:
        if(x % 2 == 0):          
          print(str(x) + " ", end = '')
      print()
     else:
      operation = input("Option not valid. Enter a valid option: ")

    flow = input("Do you want to continue? (Yes/No) : ")

    project = False

    while(project == False):
     
     if (flow == "Yes"):
      project = True
      more = input("Do you need to enter new numbers? (Yes/No): ")
     else:
      exit()

     if (more == "Yes"):
      operation = "1"
      enterNewNumbers = True
