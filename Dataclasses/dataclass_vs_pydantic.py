from dataclasses import dataclass

from pydantic import BaseModel, field_validator


# Dataclass with no validation or serialization
@dataclass
class PersonData:
    name: str
    age: int
    height: float


# Pydantic model with validation, serialization, and type conversion
class Person(BaseModel):
    name: str
    age: int
    height: float

    @field_validator("name")
    def name_must_not_contain_numbers(cls, v):
        if any(char.isdigit() for char in v):
            raise ValueError("name must not contain numbers")
        return v

    class Config:
        populate_by_name = True
        json_encoders = {float: lambda v: round(v, 2)}


# Creating objects with invalid data
person_data = PersonData(name="John123", age=30, height="1.853")

# Validation errors
print(person_data)  # PersonData(name='John123', age=30, height='1.8')
try:
    person = Person(name="John123", age=30, height="1.853")

    print(person)  # raises ValidationError: 1 validation error for Person
    # name
    #   name must not contain numbers (type=value_error)
except Exception as e:
    print(e)


person = Person(name="John", age=30, height="1.853")
# Serialization errors
person_data_json = person_data.__dict__
person_json = person.model_dump_json()
print(person_json)
print(person_data_json)
