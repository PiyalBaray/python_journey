class Address:
    def __init__(self):
        self.village = input("Enter your village name: ")
        self.polish_station = input("Enter your police station name: ")
        self.post_office = input("Enter your post office name: ")
        self.pin = int(input("Enter your pin code: "))

add = Address()

print(f"Your village name {add.village} p.s is {add.polish_station} and p.o is {add.post_office} also pin code is {add.pin}")