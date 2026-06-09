# Python Assignment.
## Question 0 
def calculate_square_area_perimiter(side):    
    area =side * side
    perimeter = 4 * side
    return [area, perimeter]

def calculate_rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return [area, perimeter]

def calculate_circle_area_perimeter(radius):
    import math
    area = math.pi * radius * radius
    perimeter = 2 * math.pi * radius
    return area, perimeter

def calculate_triangle_area_perimeter(base, height, side1, side2):
    area = 0.5 * base * height
    perimeter = base + side1 + side2
    return area, perimeter

def main():
    print("Choose an option:")
    print("1: Calculate area and perimeter of square and rectangle")
    print("2: Calculate area and perimeter of circle")
    print("3: Calculate area and perimeter of triangle")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("1: Calculate for square")
        print("2: Calculate for rectangle")
        sub_choice = int(input("Enter your choice: "))
        if sub_choice == 1:
            side = float(input("Enter the side length of the square: "))
            
        elif sub_choice == 2:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area, perimeter = calculate_rectangle_area_perimeter(length, width)
        else:
            print("Invalid choice")
            return
    elif choice == 2:
        radius = float(input("Enter the radius of the circle: "))
        area, perimeter = calculate_circle_area_perimeter(radius)
    elif choice == 3:
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        side1 = float(input("Enter the length of the first side of the triangle: "))
        side2 = float(input("Enter the length of the second side of the triangle: "))
        area, perimeter = calculate_triangle_area_perimeter(base, height, side1, side2)
    else:
        print("Invalid choice")
        return

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")

if __name__ == "__main__":
          main()

## Question 1 Write a program in Python which asks you to input any number of hours & converts it into seconds.
### Function to convert hours to seconds
def hours_to_seconds(hours):
    return hours * 3600

### Input the number of hours
hours = float(input("Enter the number of hours: "))

### Convert hours to seconds
seconds = hours_to_seconds(hours)

### Display the result
print(f"{hours} hours is equal to {seconds} seconds.")
## Question 2 Write a program in Python which asks you to input two numbers & returns the sum of them.
### Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

### Calculate the sum
sum_result = num1 + num2

### Display the result
print(f"The sum of {num1} and {num2} is {sum_result}.")
## Question 3. Write a program in Python that asks you to enter two numbers, compares them & tells you which of them is bigger or both are equal.
### Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

### Compare the numbers
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num2 > num1:
    print(f"{num2} is greater than {num1}.")
else:
    print(f"{num1} and {num2} are equal.")
## Question 4 Write a program in Python that asks you to enter a text string & returns string 'a' replaced with '0' (for example, networkwalks should be returned as networkw0lks).
### Input a text string
text = input("Enter a text string: ")

### Replace 'a' with '0'
modified_text = text.replace('a', '0')

### Display the result
print(f"The modified text is: {modified_text}")
## Question 5 Write a program in Python that asks you to enter a text string & tells you its length
### Input a text string
text = input("Enter a text string: ")

### Calculate the length of the text
length = len(text)

### Display the result
print(f"The length of the text is: {length} characters.")
## Question 6 Write a program in Python that will produce the following output using a For loop:
### For loop example to generate a pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end=' ')
    print()
## Question 7 Write a program in Python that will produce the following output using a While loop:
### While loop example to generate a pattern
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*', end=' ')
        j += 1
    print()
    i += 1
## Question 8 Write a program in Python which asks you to input two numbers & returns the average of them.
### Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

### Calculate the average
average = (num1 + num2) / 2

### Display the result
print(f"The average of {num1} and {num2} is {average}.")
## Question 9 Write a program in Python that will produce the following output:
### Example output generation program
print("Generated output:")
print("*")
print("* *")
print("* * *")
print("* * * *")
print("* * * * *")
## Question 10 nWhat will be the output of the following Python code?
var1 = 1
var2 = 2
var3 = "3"
print(var1 + var2 + var3)
