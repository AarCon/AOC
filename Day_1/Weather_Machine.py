import os
import re
import copy

repo_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
parent_file_path = os.path.abspath(os.path.dirname(__file__))

number_map = {
  "zero": 0,
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
  "ten": 10,
}

def find_all_string_numbers(string):
  new_list = [*string]
  count = 0
  for number in number_map.keys():
    for m in re.finditer(number, string):
      new_list.insert(m.end(), str(number_map[number]))
      count += 1
  join_list = "".join(new_list)
  return join_list

def weather_machine():
  sum_cal_values = 0
  with open(os.path.join(parent_file_path, "Calibration_Document.txt"), "r") as file:
    for line in file:
      strip = line.strip()
      new_line = find_all_string_numbers(strip)
      digits = re.findall(r'\d+', new_line)
      int_string = "".join(list(map(str, digits)))
      cal_value = f"{int_string[0]}{int_string[-1]}"
      sum_cal_values += int(cal_value)
  return sum_cal_values

if __name__ == "__main__":
  print(weather_machine())
