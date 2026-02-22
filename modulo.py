# Auto-Generated
# File Name: test.py 
# Author: scotton
# Creation Date: February-21-2026
# Modified Date: February-21-2026


def fizzbuzz(num: int = 3):
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    fizzbuzz()