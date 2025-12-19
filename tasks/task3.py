# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    # tasks/task3.py
# Считываем два слова (каждое на новой строке)
    word1 = input()
    word2 = input()
# Проверяем, равно ли первое слово "awesome" ИЛИ второе слово "awesome"
# Оператор "or" вернет True, если хотя бы одно условие истинно
    result = (word1 == "awesome") or (word2 == "awesome")
# Выводим результат (True или False)
    print(result)
 

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()