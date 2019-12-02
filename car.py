class Car:
    def __init__(self, make, model, color, year, price, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.mileage = int(mileage)

    def car_make_model(self):
        print(f"The car is a {self.year, self.make, self.model}")

    def car_color(self):
        print(f'The color of the car is {self.color}')

    def car_price(self):
        print(f'The price of the car is{self.price}')

    def odometer(self):
        print(f'There are currently {self.mileage} on the Honda')

    def keep_playing(self):
        miles = 100
        print("Would you like to fast forward a year and put 100 miles on the car?")
        answer = input("Type Y or y to fast forward a year on the car if not press anything")
        if answer == 'y' and 'Y':
            print(f'There are now {self.mileage + miles} after a year of driving')
        else:
            exit()
