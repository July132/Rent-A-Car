cars = [{"id": 1, "brand": "Lamborghini", "model": "Huracan", "rental_price": 100, "available": True},
        {"id": 2, "brand": "Ferrari", "model": "Superfast", "rental_price": 150, "available": True},
        {"id": 3, "brand": "McLaren", "model": "765LT", "rental_price": 90, "available": True},
        {"id": 4, "brand": "Rolls-Royce", "model": "Cullinan", "rental_price": 75, "available": True}
        ]


def rent_car(car_id: int):
    for car in cars:
        if car["id"] == car_id:
            car["available"] = False
            return f"You have rented the {car['brand']} {car['model']}.\n"
    return "Car is unavailable or invalid car ID.\n"


def return_car(car_id: int, days: int):
    for car in cars:
        if car["id"] == car_id and not car["available"]:
            car["available"] = True
            return f"You have returned the {car['brand']} {car['model']}. The total cost is ${car['rental_price'] * days}.\n"
    return "Invalid car ID or no cars rented.\n"


def display_cars():
    print("Available Cars:")
    for car in cars:
        status = "Available" if car["available"] else "Rented"
        print(f"ID: {car['id']} - {car['brand']} {car['model']} - ${car['rental_price']}/day - {status}")
    print()

def main_menu():
    print("Welcome to RentACar!")
    print("1. View Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. Exit")
    option = int(input("Please choose an option (1-4): "))
    print()
    if option == 1:
        display_cars()
    elif option == 2:
        id = int(input("What is the id of the car you wish to rent?: "))
        print(rent_car(id))
    elif option == 3:
        id = int(input("What is the id of the car you wish to return?: "))
        days_rented = int(input("How many days did you rent this car?: "))
        print(return_car(id, days_rented))
    elif option == 4:
        raise exit("Exiting car rental.")
    else:
        exit("Error")


while True:
    main_menu()
