class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


c1 = Calculator()

print("Add:", c1.add(10, 5))
print("Subtract:", c1.subtract(10, 5))
print("Multiply:", c1.multiply(10, 5))
print("Divide:", c1.divide(10, 5))
