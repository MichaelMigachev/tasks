
point = 0                 # балл
number_of_questions = 0   # количество вопросов


print("Привет! Предлагаю проверить свои знания английского! Напиши, как тебя зовут!")
name = input()
print(f"Привет, {name}, начинаем тренировку!")

# первый вопрос
answer = input("My name ___ Vova.")

if answer == "is":
    print("Ответ верный!\nВы получаете 10 баллов!\n")
    point += 10
    number_of_questions += 1
else:
    print("Неправильно.\nПравильный ответ: is\n")

# второй вопрос
answer = input("I ___ a coder.")

if answer == "am":
    print("Ответ верный!\nВы получаете 10 баллов!\n")
    point += 10
    number_of_questions += 1
else:
    print("Неправильно.\nПравильный ответ: am\n")

# третий вопрос
answer = input("I live ___ Moscow.")

if answer == "in":
    print("Ответ верный!\nВы получаете 10 баллов!\n")
    point += 10
    number_of_questions += 1
else:
    print("Неправильно.\nПравильный ответ: in\n")

percent = (number_of_questions * 100) // 3

print(f"""Вот и всё, {name}!
Вы ответили на {number_of_questions} вопросов из 3 верно.
Вы заработали {point} баллов.
Это {percent} процентов.\n""")

