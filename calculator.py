def calculator():
    print("Простой калькулятор")
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    
    while True:
        choice = input("Введите номер операции (или введите 'q' для выхода):\n")
        
        if choice == 'q':
            print("Выход из калькулятора. До свидания!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                
                if choice == '1':
                    print(f"Результат: {num1} + {num2} = {num1 + num2}")
                elif choice == '2':
                    print(f"Результат: {num1} - {num2} = {num1 - num2}")
                elif choice == '3':
                    print(f"Результат: {num1} * {num2} = {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"Результат: {num1} / {num2} = {num1 / num2}")
                    else:
                        print("Ошибка: Деление на ноль невозможно.")
            except ValueError:
                print("Ошибка: Введите числовое значение.")
        else:
            print("Ошибка: Неверный выбор. Попробуйте снова.")

calculator()