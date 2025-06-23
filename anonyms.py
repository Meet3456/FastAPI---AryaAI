'''
A @classmethod in Python is a method that belongs to the class itself, rather than an instance(object) of the class.

It is used when you want to define a method that operates on the [class] as a whole, rather than on [individual objects (instances)] of the class.

First Argument: The first parameter of a class method is conventionally named cls (short for "class"). It refers to the [class itself, not an instance]

Use Case: Class methods are often used for [factory methods], where you want to create instances of the class in a specific way, or for operations that are relevant to the class as a whole.
'''
class MyClass:
    # belongs to the class
    class_variable = "I am a class variable"

    def __init__(self,val):
        self.instance_variable = val

    # Belongs to the class itself and not the instance
    @classmethod
    def show_class_variable(cls):
        return cls.class_variable
    
    @classmethod
    def create_with_default(cls):
        # Factory method to create an instance(object) with a default value
        return cls("default value")     
    
# Example usage
print(MyClass.show_class_variable())

obj1 = MyClass("xyz")

obj = MyClass.create_with_default()
# Accessing the class variable using the instance(POSSIBLE)
print(obj.instance_variable)



