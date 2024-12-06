from logic import *
import random

levels = {

    "easy": ["dairy", "mouse", "computer"],

    "medium": ["programming", "algorithm", "developer"],

    "hard": ["neural network", "machine learning", "artificial intelligence"]

}
print("Добро пожаловать в игру!")
print("Выберите один из трёх уровней сложности: easy, medium, hard")
difficulty=input()
if difficulty=="easy":
    random_word=random.choice(levels["easy"])
    print(f"Скажи слово {random_word}")
    word=speech_en()
    if random_word==word.lower():
        print("Правильно")
    else:
        print("Неправильно")
elif difficulty=="medium":
    random_word=random.choice(levels["medium"])
    print(f"Скажи слово {random_word}")
    word=speech_en()
    if random_word==word.lower():
        print("Правильно")
    else:
        print("Неправильно")
elif difficulty=="hard":
    random_word=random.choice(levels["hard"])
    print(f"Скажи слово {random_word}")
    word=speech_en()
    if random_word==word.lower():
        print("Правильно")
    else:
        print("Неправильно")