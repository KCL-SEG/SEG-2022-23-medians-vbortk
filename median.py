"""Median calculator."""
def median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        return ((numbers[len(numbers)//2]+numbers[(len(numbers)//2) - 1]) / 2)
    return numbers[len(numbers)//2]

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
print(median(numbers))