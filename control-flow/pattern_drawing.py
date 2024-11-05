#pattern_drawing.py

#prompt user for pattern size 
size = int(input("Enter the size of the pattern: "))

#initialize the row counter for while loop 
row = 1

#construct the pattern using asterisks 
while row <= size:
    for col in range (size):
        print ( "*" , end="" )
    print()
    row += 1
