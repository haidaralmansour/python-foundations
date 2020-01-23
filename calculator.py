number1=input("enter the first number")
number2=input("enter the second number")
operation=input("choose the operation (+,-,/,*)")

if not number1.isdigit():
    number1 = input("The number you have entered is incorrect,input number 1 again: ")
if not number2.isdigit():
    number2 = input("The number you have entered is incorrect,input number 2 again: ")
if operation == "+":
    answer = int(number1)+int(number2)
elif operation == "-":
    answer=int(number1)-int(number2)
elif operation=="/":
    answer = int(number1)/int(number2)
elif operation=="*":
    answer=int(number1)*int(number2)
      
print("the answer is %s" %(answer))
    


    
