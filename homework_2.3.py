import random

def play_game():
    words = input("Введіть список слів, розділених комою: ").split(',')
    secret_word = random.choice(words)
    guess = input("Вгадайте слово : ")

    if guess == secret_word:
        print("вгадали")
    else:
        print(f"Ви не вгадали. Правильне слово '{secret_word}'.")

play_game()
