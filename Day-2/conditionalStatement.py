# Write the python program were the user gives the input and check the traffic light
#if the light is green then display stop if the light is yellow display wait if the 
#display is red display stop
light = input("Enter the light:")
light = light.lower()
if light == 'green':
    print("GO")
elif light == 'yellow':
    print("WAIT")
elif light == 'red':
    print("STOP")
else:
    print("Light is not valid")
##########################################################################################
# Write the program to find the given number is odd or even
num = int(input("Enter the number:"))
if num % 2 == 0:
    print("The given number is even")
else:
    print("The given number is odd")
##########################################################################################
#Write the program to find the given number is negative and positive
n = int(input("Enter the interger:"))
if n > 0:
    print("The given number is Positive")
elif n == 0:
    print("The given number is equal to Zero")
else :
    print("The given number is Negative")