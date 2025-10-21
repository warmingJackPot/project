# main.py
from bmi_calculator import calculate_bmi

def main():
    print("Калькулятор индекса массы тела (ИМТ)")
    print("-" * 50)
    
    try:
        weight = float(input("Введите ваш вес (в килограммах): "))
        height = float(input("Введите ваш рост (в метрах): "))
        
        bmi = calculate_bmi(weight, height)
        
        print(f"\nВаш ИМТ: {bmi}")
        
        # Добавим интерпретацию результата
        if bmi < 18.5:
            category = "недостаточный вес"
        elif 18.5 <= bmi < 25:
            category = "нормальный вес"
        elif 25 <= bmi < 30:
            category = "избыточный вес"
        else:
            category = "ожирение"
            
        print(f"Это соответствует категории: {category}")
        
    except ValueError as e:
        if "could not convert" in str(e):
            print("\n❌ Ошибка: введите числа, а не текст!")
        else:
            print(f"\n❌ Ошибка: {e}")
    except KeyboardInterrupt:
        print("\n\nВыход по запросу пользователя. До свидания!")

if __name__ == "__main__":
    main()