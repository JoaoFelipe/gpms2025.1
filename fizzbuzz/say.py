
from typing import List

def is_fizz(number: int) -> bool:
    return number % 3 == 0

def is_buzz(number: int) -> bool:
    return number % 5 == 0

def is_fizzbuzz(number: int) -> bool:
    return is_fizz(number) and is_buzz(number)

def say(number: int) -> bool:
    if is_fizzbuzz(number):
        return "fizzbuzz"
    if is_fizz(number):
        return "fizz"
    if is_buzz(number):
        return "buzz"
    return str(number)

def game(first: int = 1, last: int = 100) -> List[str]:
    return [
        say(number)
        for number in range(first, last + 1)
    ]
