point = 0                 # балл
number_of_questions = 0   # количество вопросов

questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]


print("Привет!")
print("Предлагаю проверить свои знания английского!")
ready = input("Наберите ready, чтобы начать! ")

if ready == "ready":
    for i in range(len(questions)):          # цикл для прохождения всех вопросов
        answer = input(f"{questions[i]} ")
        if answer == answers[i]:             # проверка на правильность ответа
            print("Ответ верный!\nВы получаете 10 баллов!\n")
            point += 10
            number_of_questions += 1
        else:
            print(f"Неправильно.\nПравильный ответ: {answers[i]}\n")

    percent = (number_of_questions * 100) // len(questions)

    print(f"""Вот и всё!
    Вы ответили на {number_of_questions} вопросов из {len(questions)} верно.
    Вы заработали {point} баллов.
    Это {percent} процентов.\n""")

else:
    print("Кажется, вы не хотите играть. Очень жаль.")