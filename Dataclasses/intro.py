from dataclasses import dataclass


# Regular class
class Person:
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, height={self.height})"

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age and self.height == other.height
        return False

    def __hash__(self):
        return hash((self.name, self.age, self.height))


# Dataclass
@dataclass(frozen=True)
class PersonData:
    name: str
    age: int
    height: float


# Creating objects
person = Person("John", 30, 1.8)
person_data = PersonData("John", 30, 1.8)

person2 = Person("John", 30, 1.8)
person_data2 = PersonData("John", 30, 1.8)

# Printing objects
print(person)  # Person(name=John, age=30, height=1.8)
print(person_data)  # PersonData(name='John', age=30, height=1.8)

# Comparison
print(person == person2)  # False
print(person_data == person_data2)  # False

# Hashing
print(hash(person))
print(hash(person_data))

person.name = "Jane"  # No error

try:
    person_data.name = "Jane"  # Error: dataclasses.FrozenInstanceError: cannot assign to field 'name'
except Exception as e:
    print(e)
