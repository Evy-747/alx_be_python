#prompt user for input
number = int(input("Enter a number to see its multiplication table:"))

#generate multiplication for number using for loop 
for i in range (1,11):
    result = number * i
    print (f" {number} * {i} = {result}")
