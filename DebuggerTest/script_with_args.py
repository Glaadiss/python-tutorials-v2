import argparse
import os


def calculate_sum(a: int, b: int):
    return a + b


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int, help="the first number")
    parser.add_argument("b", type=int, help="the second number")
    args = parser.parse_args()

    env_var = os.environ.get("MY_ENV_VAR")
    if not env_var:
        raise ValueError("MY_ENV_VAR environment variable is not set")

    result = calculate_sum(args.a, args.b)
    print(f"The sum of {args.a} and {args.b} is {result}")
