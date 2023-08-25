def is_palindrome(string):
    clean_string = ''.join(char for char in string.lower() if char.isalnum())
    return clean_string[0] == clean_string[-1]

input_string = input("Введіть рядок: ")
if is_palindrome(input_string):
    print("Рядок є паліндромом.")
else:
    print("Рядок не є паліндромом.")
