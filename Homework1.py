
def is_prime(number):
    if number <= 1:
        return False
    if number != int(number):
        return False  # Перевірка на цілість
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

try:
    num = float(input("Введіть число: "))
    if is_prime(num):
        print(f"{int(num)} є простим числом.")
    else:
        print(f"{int(num)} не є простим числом.")
except ValueError:
    print("Введене значення не є числом.")
