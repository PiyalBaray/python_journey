class Laptop:
    @staticmethod
    def cal_dis(price, discount):
        final_price = price - (discount * price / 100)
        print(f"Discount price = {final_price}")


Laptop.cal_dis(4000, 10)