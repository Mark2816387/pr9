import random

def generate_random_list():
    return [random.randint(1, 250) for _ in range(10)]

def shift_right(numbers):
    if numbers:  
        numbers = [numbers[-1]] + numbers[:-1]
    return numbers

def main():
    predefined_list = [13, 8, 2, 10, 52, 12, 41, 15, 26, 20]

    while True:
        choice = input("Введите 1 для генерации случайного списка или 2 для использования встроенного списка: ")
        
        if choice == '1':
            numbers = generate_random_list()
            print("Сгенерированный список:", numbers)
            break
        elif choice == '2':
            numbers = predefined_list
            print("Встроенного список:", numbers)
            break
        else:
            print("Ошибка: введите 1 или 2 для выбора.")

    shifted_list = shift_right(numbers)
    print("Список после циклического сдвига вправо:", shifted_list)

main()
