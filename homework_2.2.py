import re


email = input("Емейл: ")

pattern = r"^[a-zA-Z0-9]+\.[a-zA-Z0-9]+@eleks\.com$"

# юзаємо re.match() 
if re.match(pattern, email):
    print(email, "Емейл валідний")
else:
    print(email, "Емейл не елекса")
