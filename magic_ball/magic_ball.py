from random import choice

def is_valid_a(a):
	return True if a.upper() == "Y" or a.upper() == "N" else False

ans = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай", "Предрешено", 
"Вероятнее всего", "Спроси позже", "Мой ответ - нет", "Никаких сомнений", "Хорошие перспективы", 
"Лучше не рассказывать", "По моим данным - нет", "Определённо да", "Знаки говорят - да",
"Сейчас нельзя предсказать", "Перспективы не очень хорошие", "Можешь быть уверен в этом", 
"Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print('Привет Мир, Я магический шар, и я знаю ответ на любой твой вопрос.')

name = input('Как тебя зовут? ')
print('\nПривет',  name)

a = "Y"

while a.upper() == "Y":
	q = input('\nЗадай мне свой вопрос: ')
	print(choice(ans))
	a = input("\nЗадать ещё один вопрос?(Y / N) ")
	while not is_valid_a(a):
		a = input("\nВведите Y или N: ")

print("\nВозвращайся если возникнут вопросы!")