numbers = input("введіть числа (з пробілом) ")

numbers = list(map(int, numbers.split()))

less_than_five = [num for num in numbers if num < 5]

print("Відповідь: ", less_than_five)
