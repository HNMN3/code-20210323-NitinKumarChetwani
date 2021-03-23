import json
import os
import unittest

from app.config import get_config
from app.main import calculate_bmi_score


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        super(TestMain, self).setUp()
        os.environ['ENV'] = 'test'
        self.config = get_config()

    def test_bmi_calculation(self):
        input_records = [
            {
                "Gender": "Male",
                "HeightCm": 171,
                "WeightKg": 30
            },
            {
                "Gender": "Male",
                "HeightCm": 161,
                "WeightKg": 40
            },
            {
                "Gender": "Male",
                "HeightCm": 180,
                "WeightKg": 50
            },
            {
                "Gender": "Female",
                "HeightCm": 166,
                "WeightKg": 50
            },
            {
                "Gender": "Female",
                "HeightCm": 150,
                "WeightKg": 55
            },
            {
                "Gender": "Female",
                "HeightCm": 167,
                "WeightKg": 82
            }
        ]

        expected_output = [
            {
                "Gender": "Male",
                "HeightCm": 171,
                "WeightKg": 30,
                "BMI": 17.5,
                "BMI Category": "Underweight",
                "Health Risk": "Malnutrition risk"
            },
            {
                "Gender": "Male",
                "HeightCm": 161,
                "WeightKg": 40,
                "BMI": 24.8,
                "BMI Category": "Normal weight",
                "Health Risk": "Low risk"
            },
            {
                "Gender": "Male",
                "HeightCm": 180,
                "WeightKg": 50,
                "BMI": 27.8,
                "BMI Category": "Overweight",
                "Health Risk": "Enhanced risk"
            },
            {
                "Gender": "Female",
                "HeightCm": 166,
                "WeightKg": 50,
                "BMI": 30.1,
                "BMI Category": "Moderately obese",
                "Health Risk": "Medium risk"
            },
            {
                "Gender": "Female",
                "HeightCm": 150,
                "WeightKg": 55,
                "BMI": 36.7,
                "BMI Category": "Severely obese",
                "Health Risk": "High risk"
            },
            {
                "Gender": "Female",
                "HeightCm": 167,
                "WeightKg": 82,
                "BMI": 49.1,
                "BMI Category": "Very severely obese",
                "Health Risk": "Very high risk"
            }
        ]

        # Arrange
        with open(self.config.input_json_file_path, 'w') as input_json_file_obj:
            json.dump(input_records, input_json_file_obj)

        # Act
        calculate_bmi_score()
        with open(self.config.output_json_file_path) as output_json_file_obj:
            actual_output = json.load(output_json_file_obj)

        # Assert
        self.assertListEqual(actual_output, expected_output)

    def test_overweight_patient_count(self):
        input_records = [
            {
                "Gender": "Male",
                "HeightCm": 171,
                "WeightKg": 50
            },
            {
                "Gender": "Male",
                "HeightCm": 161,
                "WeightKg": 40
            },
            {
                "Gender": "Male",
                "HeightCm": 180,
                "WeightKg": 50
            },
            {
                "Gender": "Female",
                "HeightCm": 166,
                "WeightKg": 50
            },
            {
                "Gender": "Female",
                "HeightCm": 150,
                "WeightKg": 40
            },
            {
                "Gender": "Female",
                "HeightCm": 167,
                "WeightKg": 82
            }
        ]
        expected_overweight_count = 3

        # Arrange
        with open(self.config.input_json_file_path, 'w') as input_json_file_obj:
            json.dump(input_records, input_json_file_obj)

        # Act
        actual_overweight_count = calculate_bmi_score()

        # Assert
        self.assertEqual(actual_overweight_count, expected_overweight_count)

    def tearDown(self) -> None:
        super(TestMain, self).tearDown()
        # Remove test json files
        test_files = [self.config.input_json_file_path, self.config.output_json_file_path]
        for file_name in test_files:
            if os.path.exists(file_name):
                os.remove(file_name)
