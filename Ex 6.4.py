# Example 6_4
import math
def select_menu():
    print("Menu")
    print("1. circle 2. rectangle 3. Exit")
    menu = input("please choose : ")
    return(menu)
def cal_circle(radius):
    area = math.pi*radius*radius
    return(area)
def cal_rectangle(width, height):
    area = width*height
    return(area)
menu = ""
while menu != "3":
    print("Program calaulate area.")
    menu = select_menu()
    if menu == "1":
        radius = float(input("Enter radius : "))
        print("Area of circle = ", cal_circle(radius))
    elif menu == "2":
        width = int(input("Enter width : "))
        height = int(input("Enter height : "))
        print("Area of rectangle = ", cal_rectangle(width, height))
