import unittest
from bmi_calculator import calculate_bmi


class TestBMICalculator(unittest.TestCase):

    def test_normal_bmi_calculation(self):
        """Тест: корректный расчёт ИМТ для обычных значений"""
        result = calculate_bmi(70, 1.75)
        self.assertAlmostEqual(result, 22.86, places=2)

    def test_high_bmi_calculation(self):
        """Тест: расчёт при высоком весе"""
        result = calculate_bmi(100, 1.7)
        self.assertAlmostEqual(result, 34.60, places=2)

    def test_zero_weight_raises_error(self):
        """Тест: ошибка при весе = 0"""
        with self.assertRaises(ValueError):
            calculate_bmi(0, 1.75)

    def test_negative_height_raises_error(self):
        """Тест: ошибка при отрицательном росте"""
        with self.assertRaises(ValueError):
            calculate_bmi(70, -1.0)

    def test_fractional_values(self):
        """Тест: работа с дробными числами"""
        result = calculate_bmi(55.5, 1.65)
        self.assertAlmostEqual(result, 20.39, places=2)



if __name__ == '__main__':
    unittest.main()