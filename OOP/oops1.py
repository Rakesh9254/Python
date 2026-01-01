class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "Started")


c1 = Car("Tata")
c1.start()
