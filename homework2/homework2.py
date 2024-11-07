def get_squares_between():
    try:
        a = int(input("Введите число a: "))
        b = int(input("Введите число b: "))
        
        if a > b:
            a, b = b, a
            
        squares = [x**2 for x in range(a + 1, b)]

        if a == b:
            print("между числами нет квадратов целых чисел")
        
        print("Список квадратов чисел между", a, "и", b, ":", squares)
    except ValueError:
        print("Ошибка: Введите только целые числа!")
    
get_squares_between()
