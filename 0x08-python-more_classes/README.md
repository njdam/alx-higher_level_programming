# Python - More Classes and Objects

## Inheritance

In Python, classes can inherit attributes and methods from other classes, which is known as inheritance. The class that inherits from another class is called a subclass or derived class, and the class being inherited from is called the superclass or base class. Inheritance allows for code reuse and the creation of specialized classes.

```
class ParentClass:
    # ...

class ChildClass(ParentClass):
    # ...
```

Method Overriding: Inheritance also allows for method overriding, where a subclass can provide its own implementation of a method that is already defined in the superclass. When a method is called on an instance of a subclass, the subclass's implementation is used instead of the superclass's implementation. This allows subclasses to modify or extend the behavior of inherited methods. Here's an example:

```
class ParentClass:
    def greet(self):
        print("Hello, I am the parent.")

class ChildClass(ParentClass):
    def greet(self):
        print("Hello, I am the child.")

parent = ParentClass()
parent.greet()  # Output: Hello, I am the parent.

child = ChildClass()
child.greet()  # Output: Hello, I am the child.
```

Multiple Inheritance: Python supports multiple inheritance, which means a class can inherit from multiple base classes. This allows a subclass to inherit attributes and methods from multiple sources. To specify multiple base classes, separate them with commas in parentheses after the class name. Here's an example:

```
class BaseClass1:
    # ...

class BaseClass2:
    # ...

class DerivedClass(BaseClass1, BaseClass2):
    # ...
```

## Methods

Special Methods (Magic Methods): Python provides a set of special methods that start and end with double underscores (e.g., `__init__`, `__str__`). These methods provide functionality to the classes and objects, enabling customization of behavior. For example, the `__init__` method is used to initialize objects, and the `__str__` method is used to provide a string representation of an object. By implementing these special methods, you can define how your objects interact with built-in Python functions and operators.


The `__str__` and `__repr__` methods are special methods in Python classes that define how an object should be represented as a string. They provide human-readable or unambiguous string representations of an object, respectively.
The `__str__` method is used to provide a string representation that is intended to be readable by humans. It should return a string that represents the object in a concise and informative way.

The `__repr__` method is used to provide an unambiguous string representation of the object. It should return a string that can be used to recreate the object or that represents the object in a way that uniquely identifies it.

The main difference between `__str__` and `__repr__` is their intended purpose. `__str__` is meant to provide a human-readable representation of an object, while `__repr__` is meant to provide an unambiguous representation of the object, often used for debugging and development purposes.

`A class attribute` is an attribute that is shared by all instances of a class. It is defined within the class but outside of any instance methods. All instances of the class have access to the same value of the class attribute.

`An object attribute`, also known as an instance attribute, is an attribute that is specific to each instance of a class. Each instance can have its own value for an object attribute.

`A class method` is a method that is bound to the class and not the instance of the class. It receives the class as its first argument, typically named cls, instead of the instance (self). Class methods are defined using the @classmethod decorator.

`Class methods` are often used to create alternative constructors or perform operations that are related to the class as a whole rather than a specific instance. They can be called on the class itself, without the need to create an instance.

`A static method` is a method that belongs to a class but does not have access to the class or instance attributes. It is defined within a class using the @staticmethod decorator and does not receive any special first argument like self or cls.

`Static methods` are typically used when a method does not depend on any instance or class-specific data, and it can be called on the class itself or an instance of the class. They are often used for utility functions or operations that do not modify or rely on the state of the class or its instances.

[Reference](https://chat.openai.com/)
