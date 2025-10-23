#method overloading code for polymorphism concept
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c    
    def add(self, a, b):
        return a + b
    def add(self, a, b, c, d):
        return a + b + c + d
    def add(self, a, b, c, d, e):
        return a + b + c + d + e
    def add(self, *args):
        if not args:
            return None  # no arguments case
        result = args[0]
        for val in args[1:]:
            result += val
        return result    
math_ops = MathOperations()
print(math_ops.add(5, 10))            # integer addition
print(math_ops.add(5.5, 10.2))        # float addition  
print(math_ops.add("Hello, ", "World!")) # string concatenation
print(math_ops.add(1, 2, 3))          # adding three integers
print(math_ops.add(1, 2, 3, 4))       # adding four integers
print(math_ops.add(1, 2, 3, 4, 5))    # adding five integers
print(math_ops.add(1, 2, 3, 4, 5, 6)) # adding six integers
print(math_ops.add(1, 2, 3, 4, 5, 6, 7)) # adding seven integers
print(math_ops.add(1, 2, 3, 4, 5, 6, 7, 8)) # adding eight integers
print(math_ops.add(1, 2, 3, 4, 5, 6, 7, 8, 9)) # adding nine integers
print(math_ops.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # adding ten integers
print(math_ops.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) # adding eleven integers