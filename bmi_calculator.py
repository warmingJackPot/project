def calculate_bmi(weight_kg, height_m):
    """
    Рассчитывает ИМТ.
    :param weight_kg: вес в килограммах (число > 0)
    :param height_m: рост в метрах (число > 0)
    :return: ИМТ (округлённый до 2 знаков)
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Вес и рост должны быть больше нуля")
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)