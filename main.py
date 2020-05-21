numbers = list(range(1, 51))
print(numbers, "\n")
numbers.extend(list(range(51, 61)))
print(numbers, "\n")

multiple_of_2 = [n for n in numbers if n % 2 == 0]
print(multiple_of_2, "\n")

multiple_of_3 = [n for n in numbers if n % 3 == 0]
print(multiple_of_3, "\n")
print(jej)
