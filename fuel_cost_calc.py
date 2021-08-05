def calculate_fuel_cost(distance, price_per_litre, mpg):
    price_per_gallon = price_per_litre * 4.5
    price_per_mile = price_per_gallon / mpg
    cost_per_journey = distance * price_per_mile
    print(round(price_per_gallon))
    print(price_per_mile)
    print("Your journey will cost £" + str(cost_per_journey) + " per day")
calculate_fuel_cost(8, 1.39, 40)
