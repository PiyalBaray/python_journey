class car:
    def __init__(self):
        self.car_name = input("Enter your car company name : ")
        self.model = input("Say model name : ")
        self.age = int(input("HOw many days old "))


car_company = car()
print(f'Your car company is {car_company.car_name} \n Model number is {car_company.model} \n Car age is {car_company.age} days')