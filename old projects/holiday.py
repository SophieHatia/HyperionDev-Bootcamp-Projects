city_flight = input("Which city will you be flying to? \n1) Rome  2) New York  3) Hong Kong  4) Sydney  5) Cairo\n Write 1 - 5 for your choice " )
num_nights = input("How many nights will you be staying? ")
rental_days = input("For how many days will you be hiring a car? " )

num_nights = float(num_nights)
city_flight = int(city_flight)
rental_days = float(rental_days)

def hotel_cost(num_nights, night_price = 120):
    hotel_cost = num_nights * night_price
    return hotel_cost

def plane_cost(city_flight):
    if city_flight == 1:
        plane_cost = 85
        return plane_cost
    elif city_flight == 2:
        plane_cost = 424
        return plane_cost
    elif city_flight == 3:
        plane_cost = 681
        return plane_cost
    elif city_flight == 4:
        plane_cost = 1201
        return plane_cost
    elif city_flight == 5:
        plane_cost = 432
        return plane_cost
    else: 
        return "Please choose a city from the list"
    
def car_rental(rental_days, rental_price = 40):
    car_rental = rental_days * rental_price
    return car_rental

def holiday_cost(hotel_cost, plane_cost, car_rental):
    holiday_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return holiday_cost

print("The cost of the hotel for these nights=", hotel_cost(num_nights))
print("The price of the flights to this city=", plane_cost(city_flight))
print("The price to rent a car for this many nights=", car_rental(rental_days))
print("The total price of the holiday=", holiday_cost(hotel_cost,plane_cost,car_rental))
