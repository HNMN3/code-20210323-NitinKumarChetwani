import os


class DefaultConfig:
    input_json_file_path = "input.json"
    output_json_file_path = "output.json"
    debug = True
    bmi_ranges = [0, 18.4, 24.9, 29.9, 34.9, 39.9, float('inf')]
    OVERWEIGHT_KEY = "Overweight"
    bmi_category = ['Underweight', 'Normal weight', OVERWEIGHT_KEY, 'Moderately obese', 'Severely obese',
                    'Very severely obese']
    health_risk = ['Malnutrition risk', 'Low risk', 'Enhanced risk', 'Medium risk', 'High risk',
                   'Very high risk']


class DevelopmentConfig(DefaultConfig):
    pass


class ProductionConfig(DefaultConfig):
    debug = False


class TestConfig(DefaultConfig):
    input_json_file_path = "test_input.json"
    output_json_file_path = "test_output.json"


def get_config() -> DefaultConfig:
    env = os.environ.get("ENV") or "default"
    configs = {
        'default': DefaultConfig(),
        'development': DevelopmentConfig(),
        'test': TestConfig(),
        'production': ProductionConfig(),
    }
    return configs.get(env) or DefaultConfig()
