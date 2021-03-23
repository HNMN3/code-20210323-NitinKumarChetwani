import logging

import pandas as pd

from app.config import get_config

logger = logging.getLogger('app')


def calculate_bmi_score():
    config = get_config()
    input_records_df = pd.read_json(config.input_json_file_path, orient='records')

    input_records_df["BMI"] = input_records_df.WeightKg / (input_records_df.HeightCm / 100)
    input_records_df["BMI"] = input_records_df["BMI"].round(1)

    input_records_df["BMI Category"] = pd.cut(input_records_df["BMI"], bins=config.bmi_ranges,
                                              labels=config.bmi_category)

    input_records_df["Health Risk"] = pd.cut(input_records_df["BMI"], bins=config.bmi_ranges,
                                             labels=config.health_risk)

    input_records_df.to_json(config.output_json_file_path, orient='records')

    overweight_patients = input_records_df[input_records_df["BMI Category"] == config.OVERWEIGHT_KEY]
    overweight_patients_count = len(overweight_patients)
    return overweight_patients_count


if __name__ == '__main__':
    calculate_bmi_score()
