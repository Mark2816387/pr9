def collect_odd_numbers():
    numbers = []
    
    while True:
        user_input = input("Введите число (или 'end' для завершения): ")
        
        if user_input.lower() == 'end':
            break
        
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Ошибка: введите корректное число или 'end' для завершения.")

    odd_numbers = [num for num in numbers if int(num) % 2 != 0]
    
    print("Нечетные элементы списка:", odd_numbers)

collect_odd_numbers()
