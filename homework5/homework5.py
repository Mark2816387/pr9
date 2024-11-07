import random

def generate_random_list():
    return [random.randint(1, 500) for _ in range(10)]

def filter_larger_than_previous(numbers):
    return [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]

def main():
    predefined_list = [3, 18, 2, 102, 5, 2, 4, 12, 6, 28]

    while True:
        choice = input("Введите: 1 для генерации случайного списка или 2 для использования встроенного списка: ")
        
        if choice == '1':
            numbers = generate_random_list()
            print("Сгенерированный список:", numbers)
            break
        elif choice == '2':
            numbers = predefined_list
            print("Встроенный список список:", numbers)
            break
        else:
            print("Ошибка: введите 1 или 2 для выбора.")

    result = filter_larger_than_previous(numbers)
    print("Элементы списка, которые больше предыдущего элемента:", result)

main()
