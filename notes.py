# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    def __init__(self, n="no name", a=0):
        self.name = n
        self.age = a
        
    def __str__(self):
        s = f"{self.name} is {self.age} years old"
        return s

logan = Dog("logan",8)
becker = Dog("becker",4)
kepa = Dog("kepa", 4)

print(logan)
print(becker)
print(kepa)