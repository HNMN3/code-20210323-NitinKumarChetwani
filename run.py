from app.main import calculate_bmi_score

if __name__ == '__main__':
    overweight_patients_count = calculate_bmi_score()
    print("Total number of overweight patients: {}".format(overweight_patients_count))
