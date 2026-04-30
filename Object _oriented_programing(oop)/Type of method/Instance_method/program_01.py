class Laptop:
    storage_type = "SSD"

    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    def get_info(self):
        print(f"Laptop has {self.ram} RAM and {self.storage} {self.storage_type}")


l1 = Laptop("16GB", "512GB")
l1.get_info()