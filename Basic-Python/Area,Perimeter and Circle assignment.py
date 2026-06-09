# A python Program that is used to;
## Calculate the area, perimeter and circumference of circle, rectangle, square and triangle.

import math
## main menu that contain options 1 to 3 and what the program does.
def main_menu():
    while True:
        print("\nThis program calculates the area, perimeter, and circumference of squares, rectangles, triangles, and circles.")
        print("Main Menu:")
        print("1) Calculate for Square and Rectangle")
        print("2) Calculate for Triangle")
        print("3) Calculate for Circle")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            square_rectangle_menu()
        elif choice == '2':
            triangle_menu()
        elif choice == '3':
            circle_menu()
        else:
            handle_invalid_choice(main_menu)
## This is the operations of choice one.(square and rectangle)
def square_rectangle_menu():
    while True:
        print("\nSquare and Rectangle Menu:")
        print("1) Square")
        print("2) Rectangle")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            square_operations()
        elif choice == '2':
            rectangle_operations()
        else:
            handle_invalid_choice(square_rectangle_menu)
## This are the options under triangle menu.(Option Two, Main-Menu)
### It contain tree options for area, perimeter and circumference.
def triangle_menu():
    while True:
        print("\nTriangle Menu:")
        print("1) Calculate Area")
        print("2) Calculate Perimeter")
        print("3) Calculate Circumference")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            calculate_triangle_area()
        elif choice == '2':
            calculate_triangle_perimeter()
        elif choice == '3':
            print("Circumference doesn't apply to triangles.")
            post_calculation_menu()
        else:
            handle_invalid_choice(triangle_menu)
##This are the options under circle menu(Option Three, Main-Menu)
###It also contain two option for area and circumference.            
def circle_menu():
    while True:
        print("\nCircle Menu:")
        print("1) Calculate Area")
        print("2) Calculate Circumference")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            calculate_circle_area()
        elif choice == '2':
            calculate_circle_circumference()
        else:
            handle_invalid_choice(circle_menu)
## This are the operations under square (Area, Perimeter and Circumference)
def square_operations():
    while True:
        print("\nSquare Operations:")
        print("1) Calculate Area")
        print("2) Calculate Perimeter")
        print("3) Calculate Circumference")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            calculate_square_area()
        elif choice == '2':
            calculate_square_perimeter()
        elif choice == '3':
            print("Circumference doesn't apply to squares.")
            post_calculation_menu()
        else:
            handle_invalid_choice(square_operations)
## Shows the operations under Rectangle (Area, Perimeter and Circumference)            
def rectangle_operations():
    while True:
        print("\nRectangle Operations:")
        print("1) Calculate Area")
        print("2) Calculate Perimeter")
        print("3) Calculate Circumference")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            calculate_rectangle_area()
        elif choice == '2':
            calculate_rectangle_perimeter()
        elif choice == '3':
            print("Circumference doesn't apply to rectangles.")
            post_calculation_menu()
        else:
            handle_invalid_choice(rectangle_operations)
## It shows the requirement of area under square.(side length)
def calculate_square_area():
    side = float(input("Enter the side length of the square: "))
    area = side ** 2
    print(f"The area of the square is: {area}")
    post_calculation_menu()
## It shows the requirement of perimeter under square.(side length)
def calculate_square_perimeter():
    side = float(input("Enter the side length of the square: "))
    perimeter = 4 * side
    print(f"The perimeter of the square is: {perimeter}")
    post_calculation_menu()
## It shows the requirement of area under rectangle.(length,width)
def calculate_rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area}")
    post_calculation_menu()
## It shows the requirement of perimeter under rectangle.(length,width)
def calculate_rectangle_perimeter():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    perimeter = 2 * (length + width)
    print(f"The perimeter of the rectangle is: {perimeter}")
    post_calculation_menu()
## It shows the requirement of area under triangle.(base-length,height)
def calculate_triangle_area():
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")
    post_calculation_menu()
## It shows the requirement of perimeter under triangle.(1st side, 2nd side, 3rd side)
def calculate_triangle_perimeter():
    side1 = float(input("Enter the length of the first side of the triangle: "))
    side2 = float(input("Enter the length of the second side of the triangle: "))
    side3 = float(input("Enter the length of the third side of the triangle: "))
    perimeter = side1 + side2 + side3
    print(f"The perimeter of the triangle is: {perimeter}")
    post_calculation_menu()
## It shows the requirement of area under circle.(radius)
def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"The area of the circle is: {area}")
    post_calculation_menu()
## It shows the requirement of circumference under circle.(radius)
def calculate_circle_circumference():
    radius = float(input("Enter the radius of the circle: "))
    circumference = 2 * math.pi * radius
    print(f"The circumference of the circle is: {circumference}")
    post_calculation_menu()
## IT shows how invalid choice are handled in between options.
def handle_invalid_choice(previous_menu_function):
    while True:
        print("Invalid choice. Please try again.")
        print("1) Back")
        choice = input("Enter your choice (1): ")

        if choice == '1':
            previous_menu_function()
            break
        else:
            print("Invalid choice. Please try again.")
## IT shows post calculation menu after completion of calculation under an option.
## IT displays two options (Return to Main Menu, Exit).         
def post_calculation_menu():
    while True:
        print("\nWould you like to:")
        print("1) Return to Main Menu")
        print("2) Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            main_menu()
            break
        elif choice == '2':
            print("Thank you! See you again! 😂")
            exit()
        else:
            handle_invalid_choice(post_calculation_menu)

if __name__ == "__main__":
    main_menu()
