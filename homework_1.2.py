# Input four-digit natural number from the console
num = input("Введіть чотиризначне  число: ")

# Ensure the number is four digits long
if len(num) != 4 or not num.isdigit():
    print("Введіть чотиризначне  число")
else:
    # Compute the product of the digits
    product = 1
    for i in num:
        product *= int(i)
    print("Добуток цифр:", product)

    # Reverse the number
    reversed_num = ""
    for i in reversed(num):
        reversed_num += i
    print("Обернене число:", reversed_num)

    # Sort the digits
    sorted_num = sorted(num)
    sorted_digits = "".join(sorted_num)
    print("Сортування", sorted_digits)
1