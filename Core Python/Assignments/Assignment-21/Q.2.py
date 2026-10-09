# 2. Create class television that has members to hold the model number ,screen size
# and price. Take a member function to take input from user, If more than 4 digits
# are entered for model number, if screen size is smaller than 12 inches or greater
# than 70 inches or if the price is negative or greater than 5000 Rs, then throw an
# exception.
# Write a main() that instantiates an object and allows the user to enter and display
# data. If exception is caught, replace all data member values with zero
class Television:
    def __init__(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0

    def input_data(self):
        self.model_number = int(input("Enter model number: "))
        self.screen_size = float(input("Enter screen size in inches: "))
        self.price = float(input("Enter price in Rs: "))

        if self.model_number > 9999:
            raise ValueError("Model number must not exceed 4 digits")

        if self.screen_size < 12 or self.screen_size > 70:
            raise ValueError("Screen size must be between 12 and 70 inches")

        if self.price < 0 or self.price > 5000:
            raise ValueError("Price must be between 0 and 5000 Rs")

    def display(self):
        print("\n--- Television Details ---")
        print("Model Number:", self.model_number)
        print("Screen Size:", self.screen_size, "inches")
        print("Price: Rs.", self.price)


def main():
    tv = Television()

    try:
        tv.input_data()
    except (ValueError, Exception) as e:
        print("Error:", e)
        tv.model_number = 0
        tv.screen_size = 0
        tv.price = 0

    tv.display()


main()

