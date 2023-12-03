import os
import re

repo_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
parent_file_path = os.path.abspath(os.path.dirname(__file__))

MAX_CUBES = {
  "red": 12,
  "green": 13,
  "blue": 14
}

def check_game_possibility(game_dict):
  for color in game_dict.keys():
    if game_dict[color] > MAX_CUBES[color]:
      return False
  return True

def get_game_dict(game_list):
  game_dict = {
    "red": 0,
    "green": 0,
    "blue": 0
  }
  inputs = game_list.split(", ")
  for color in inputs:
    color_split = color.split(" ")
    ammount = int(color_split[0])
    color = color_split[1]
    game_dict[color] = ammount
  return game_dict

def sum_of_games(game_ids):
  final_sum = 0
  for game_id in game_ids:
    final_sum += int(game_id)
  return final_sum

def update_true_dict(true_game_dict, game_dict):
  for color in true_game_dict.keys():
    if game_dict[color] > true_game_dict[color]:
      true_game_dict[color] = game_dict[color]


def get_possible_games(
    games_list,
    possible_game,
    possible_list,
    game_id,
    true_game_dict,
    impossible_list
  ):
  for game in games_list:
    game_dict = get_game_dict(game)
    update_true_dict(true_game_dict, game_dict)
    possible = check_game_possibility(game_dict)
    if possible and possible_game:
      possible_game = True
    else:
      possible_game = False
  if possible_game:
    possible_list.append(game_id)
  else:
    impossible_list.append(game_id)
  return possible_game

def multiply_min_game_results(true_game_dict):
  cube_total = 1
  for color_value in true_game_dict.values():
    cube_total *= color_value
  return cube_total

def bag_game():
  possible_list = []
  impossible_list = []
  cube_total = 0
  with open(os.path.join(parent_file_path, "Input.txt"), "r") as file:
    for line in file:
      strip  = line.strip()
      game_split = strip.split(": ")
      game_id_name = game_split[0]

      game_id = game_id_name.split(" ")[1]
      games_list = game_split[1].split("; ")
      possible_game = True
      true_game_dict = {
        "red": 0,
        "green": 0,
        "blue": 0
      }
      get_possible_games(
        games_list,
        possible_game,
        possible_list,
        game_id,
        true_game_dict,
        impossible_list
      )
      cube_total += multiply_min_game_results(true_game_dict)

  return sum_of_games(possible_list), cube_total

if __name__ == "__main__":
  print(bag_game())
  ## Part 1 solution was 2439