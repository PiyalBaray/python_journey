class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))

# Using class method as constructor
p1 = Person.from_string("Piyal-20")

print(p1.name)
print(p1.age)

