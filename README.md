# BMI Calculator App

This application takes a list of users data including weight and height, and calculates their BMI Score, Health risk,
and BMI Category and final stores them into JSON format.

It uses the Pandas library and Vectorized operations to do the calculations which works pretty well on large set of data
as well.

## Requirements

- Python 3.8+

## Set up the project

Install the requirements using following command

```shell
pip install -r requirements.txt
```

## Running the tests

To make sure that application works correctly, run the tests using following command

```shell
nose2
```

## Using the application

Populate the user records in input.json file as a list of following json object

```json
{
  "Gender": "Male",
  "HeightCm": 171,
  "WeightKg": 50
}
```

Then run the application with following command
```shell
python run.py
```