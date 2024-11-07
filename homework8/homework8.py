import random

def get_user_ticket(ticket):
    user_choices = []
    print("Выберите по одному числу из каждой строки:")
    for i, row in enumerate(ticket):
        while True:
            try:
                choice = int(input(f"Введите число из строки {i + 1}: {row}: "))
                
                if choice in row:
                    user_choices.append(choice)
                    break
                else:
                    print("Ошибка: выберите число, которое находится в указанной строке.")
            except ValueError:
                print("Ошибка: введите целое число.")
    return user_choices

def get_random_ticket(ticket):
    return [random.choice(row) for row in ticket]

def calculate_matches(user_ticket, random_ticket):
    return len(set(user_ticket) & set(random_ticket))

def main():
    ticket = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    
    user_ticket = get_user_ticket(ticket)
    random_ticket = get_random_ticket(ticket)
    
    print("\nВаш выбор:", user_ticket)
    print("Случайный выбор:", random_ticket)
    
    matches = calculate_matches(user_ticket, random_ticket)
    
    if matches == 0:
        print("К сожалению, вы не выиграли ничего. Попробуйте снова!")
    elif 1 <= matches <= 4:
        print("Поздравляем! Вы выиграли, плюсы:", "+" * matches)
    elif matches == 5:
        print("Поздравляем! Вы выиграли в лотерею: ++++++++++ (10 плюсов)")

main()
