class Vehicle: #create a class called Vehicle.
    def print_vehicleType(self, vehicleType): #function displays the vehicle type when it's callled.
        print("Vehicle type: ", vehicleType)

class Automobile(Vehicle): #create a class that inherited the function from class Vehicle and displays the year, make, model, number of doors, roof type when it's called.
    def print_CarInfo(self, year, make, model, doors, roof):
        print("Year:", year)
        print("Make:", make)
        print("Model:", model)
        print("Number of doors:", doors)
        print("Type of roof:", roof)

vehicle = Automobile()    #create an instance of Automobile() class.

print("This is the program that displays the vehicle's information.")

vehicleType = str(input("Enter your vehicle type (car, truck, plane, boat, or broomstick): ")) #get the vehicle type input from the user.
while (vehicleType.capitalize() != "Car" and "Truck" and "Plane" and "Boat" and "Broomstick"): #check if the vehicle type is in the list or not.
    
    print("Your input is invalid.\n")
    
    vehicleType = str(input("Enter your vehicle type (car, truck, plane, boat, or broomstick): "))

Year = int(input("Enter your vehicle's year: ")) #get the year of the vehicle that is manufactured from the user.
while (Year <= 0): #check if the year is valid.
    
    print("Your input is invalid.")

    Year = int(input("Enter your vehicle's year: "))

Make = str(input("Enter your vehicle's make: ")) #get the vehicle's make from the user.

Model = str(input("Enter your vehicle's model: ")) #get the vehicle's model from the user.

Doors = int(input("Enter the number of your vehicle's doors (2 or 4): ")) #get the number of vehicle's doors from the user.
while (Doors != 2 and 4): #check if the number of doors is in the option.
    
    print("Your input is invalid.\n")
    
    Doors = int(input("Enter the number of your vehicle's doors (2 or 4): "))

Roof = str(input("Enter the type of your vehicle's roof (solid or sunroof): ")) #get the roof type of vehicle from the user.
while (Roof.capitalize() != "Solid" and "Sunroof"): #check if the roof type is in the option.
    
    print("Your input is invalid.\n")
    
    Roof = str(input("Enter the type of your vehicle's roof (solid or sunroof): "))


print("")

vehicle.print_vehicleType(vehicleType.capitalize()) #call the function print_vehicleType() from Automobile() class that displays the vehicle type.
vehicle.print_CarInfo(Year, Make.capitalize(), Model.capitalize(), Doors, Roof.capitalize()) #call the function print_CarInfo() from the Automobile() class that displays the year, make, model, doors, roof.