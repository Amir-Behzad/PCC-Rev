"""
4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
"""

numbers = [number for number in range(1, 1000001)]
#print(numbers)

min = min(numbers)
max = max(numbers)

print(f"min: {min}")
print(f"max: {max}")

print(f"Sum of the numbers: {sum(numbers)}")
