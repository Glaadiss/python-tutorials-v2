from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str


user = User(name="John Doe", age=30, email="john.doe@example.com")
user_dict = user.model_dump()

print(user_dict)
# Output: {'name': 'John Doe', 'age': 30, 'email': 'john.doe@example.com'}

invalid_user = User(name="Jane Doe", age=30, email="jane.doe@example.com")
# Raises a ValueError: "invalid literal for int() with base 10: '30'"


def add_numbers(a: int, b: int) -> int:
    return a + b


result = add_numbers(1, 2)
print(result)

invalid_result = add_numbers(1, "2")
print(invalid_result)
