import unittest
from bmi_calculator import calculate_bmi

class TestBMICalculator(unittest.TestCase):

    def test_normal_bmi(self):
        # Человек: 70 кг, 1.75 м → ИМТ = 22.86
        self.assertEqual(calculate_bmi(70, 1.75), 22.86)

    def test_zero_weight_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_bmi(0, 1.75)

    def test_negative_height_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_bmi(70, -1.0)

    def test_obese_bmi(self):
        # 100 кг, 1.7 м → ИМТ ≈ 34.6
        self.assertEqual(calculate_bmi(100, 1.7), 34.6)