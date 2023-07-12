# Python - Inheritance

In Python, `inheritance` is a fundamental concept in object-oriented programming (OOP). It allows a class to inherit attributes and behaviors from another class, known as the `parent` or `base` `class`. The class that inherits from the parent class is called the `child` or `derived` `class`.

To establish inheritance in Python, you define a `child` class and specify the `parent` class in parentheses after the child class name when defining the class.

Here's an example:
```
class ParentClass:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f"Hello, {self.name}!")

class ChildClass(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def say_age(self):
        print(f"I am {self.age} years old.")

# Creating an instance of the child class
child = ChildClass("John", 25)

# Accessing inherited method from the parent class
child.say_hello()  # Output: Hello, John!

# Accessing the child class's own method
child.say_age()  # Output: I am 25 years old.
```

In the example above, `ParentClass` is the parent class, and `ChildClass` is the child class inheriting from it. The child class can access the attributes and methods defined in the parent class. In the child class's `__init__` method, the `super()` function is used to call the parent class's `__init__` method, allowing the child class to inherit and initialize the `name` attribute from the parent class.
