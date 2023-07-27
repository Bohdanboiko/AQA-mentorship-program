а
import random

def play_game():
    while True:
        words = input("Введіть список слів, розділених комою: ").split(',')
        secret_word = random.choice(words)
        guess = input("Вгадайте слово : ")

        if guess == secret_word:
            print("вгадали")
        else:
            print(f"Ви не вгадали. Правильне слово '{secret_word}'.")

        play_again = input("Бажаєте зіграти ще раз? (так/ні): ")
        if play_again.lower() != "так":
            break

play_game()

