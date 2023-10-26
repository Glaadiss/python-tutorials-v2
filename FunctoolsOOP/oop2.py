class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


person = Person("John", 30)
print(person.name)  # John
person.name = "Jane"
print(person.name)  # Jane

print(person.age)  # 30
person.age = 35
print(person.age)  # 35
