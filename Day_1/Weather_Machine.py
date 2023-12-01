import os
import re

repo_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
parent_file_path = os.path.abspath(os.path.dirname(__file__))

def get_num_string():
  pass

def weather_machine():
  sum_cal_values = 0
  with open(os.path.join(parent_file_path, "Calibration_Document.txt"), "r") as file:
    for line in file:
      digits = re.findall(r'\d+', line.strip())
      int_string = "".join(list(map(str, digits)))
      cal_value = f"{int_string[0]}{int_string[-1]}"
      sum_cal_values += int(cal_value)
  return sum_cal_values

print(weather_machine())