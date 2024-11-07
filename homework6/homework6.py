import random

def generate_random_list():
    return [random.randint(1, 1000) for _ in range(10)]

def swap_min_max(numbers):
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))
    
    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
    return numbers

def main():
    predefined_list = [3, 8, 2, 10, 5, 12, 4, 15, 6, 20]

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

    swapped_list = swap_min_max(numbers)
    print("Список после замены минимального и максимального элементов:", swapped_list)

main()
