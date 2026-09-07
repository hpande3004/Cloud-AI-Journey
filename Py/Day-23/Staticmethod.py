'''Static Method'''
class Calculator:
    @staticmethod
    def add(a,b):
        return a + b

print("The addition is:", Calculator.add(15, 21))   #Output

class MathUtil:
    @staticmethod
    def is_even(num):
        return num % 2 == 0

print("Is 10 even?", MathUtil.is_even(10))
print("Is 7 even?", MathUtil.is_even(7))