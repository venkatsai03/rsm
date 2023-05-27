class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        if self.is_running:
            print("The vehicle is already running.")
        else:
            self.is_running = True
            print("Starting the vehicle.")

    def stop(self):
        if not self.is_running:
            print("The vehicle is already stopped.")
        else:
            self.is_running = False
            print("Stopping the vehicle.")

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Running: {'Yes' if self.is_running else 'No'}")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors, fuel_type):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.fuel_type = fuel_type


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, top_speed):
        super().__init__(make, model, year)
        self.top_speed = top_speed


class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity, num_axles):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity
        self.num_axles = num_axles


# Creating instances of the vehicles
myCar = Car("Toyota", "Camry", 2022, 4, "Petrol")
myMotorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021, 180)
myTruck = Truck("Ford", "F-150", 2020, "2000 kg", 2)

# Performing operations on the vehicles
myCar.start()
myCar.display_info()
myCar.stop()

print()

myMotorcycle.start()
myMotorcycle.display_info()
myMotorcycle.stop()

print()

myTruck.start()
myTruck.display_info()
myTruck.stop()
