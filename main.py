class Vehicle:
    def print_vehicleType(self, vehicleType):
        print("Vehicle type: ", vehicleType)

class Automobile(Vehicle):
    def print_CarInfo(self, year, make, model, doors, roof):
        print("Year:", year)
        print("Make:", make)
        print("Model:", model)
        print("Number of doors:", doors)
        print("Type of roof:", roof)

vehicle = Automobile()    

print("This is the program that displays the vehicle's information.")

vehicleType = str(input("Enter your vehicle type (car, truck, plane, boat, or broomstick): "))
while (vehicleType.capitalize() != "Car" and "Truck" and "Plane" and "Boat" and "Broomstick"):
    print("Your input is invalid.\n")
    
    vehicleType = str(input("Enter your vehicle type (car, truck, plane, boat, or broomstick): "))

Year = int(input("Enter your vehicle's year: "))
while (Year <= 0):
    print("Your input is invalid.")

    Year = int(input("Enter your vehicle's year: "))

Make = str(input("Enter your vehicle's make: "))

Model = str(input("Enter your vehicle's model: "))

Doors = int(input("Enter the number of your vehicle's doors (2 or 4): "))
while (Doors != 2 and 4):
    print("Your input is invalid.\n")
    Doors = int(input("Enter the number of your vehicle's doors (2 or 4): "))

Roof = str(input("Enter the type of your vehicle's roof (solid or sunroof): "))
while (Roof.capitalize() != "Solid" and "Sunroof"):
    print("Your input is invalid.\n")
    Roof = str(input("Enter the type of your vehicle's roof (solid or sunroof): "))


print("")

vehicle.print_vehicleType(vehicleType.capitalize())
vehicle.print_CarInfo(Year, Make.capitalize(), Model.capitalize(), Doors, Roof.capitalize())