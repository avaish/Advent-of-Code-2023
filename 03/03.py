import math
import re


def process_line(prev_line, current_line, next_line, line_count):
  gear_list = []

  nums = re.finditer(r'([0-9]+)', current_line)
  for num in nums:
    min_range = max(num.span()[0] - 1, 0)
    max_range = min(num.span()[1] + 1, len(current_line))

    if prev_line is not None:
      gears = re.finditer(r'[^0-9.]', prev_line[min_range:max_range])
      for gear in gears:
        gear_list.append(
            ((line_count - 1, min_range + gear.span()[0]), int(num.group())))

    gears = re.finditer(r'[^0-9.]', current_line[min_range:max_range])
    for gear in gears:
      gear_list.append(((line_count, min_range + gear.span()[0]), int(num.group())))

    if next_line is not None:
      gears = re.finditer(r'[^0-9.]', next_line[min_range:max_range])
      for gear in gears:
        gear_list.append(
            ((line_count + 1, min_range + gear.span()[0]), int(num.group())))

  return gear_list


if __name__ == "__main__":
  prev_line = None
  current_line = None
  next_line = None
  line_count = -1
  gear_dict = {}

  with open("input.txt", "r") as f:
    for line in f.readlines():
      prev_line = current_line
      current_line = next_line
      next_line = line.strip()

      if current_line is not None:
        gear_list = process_line(prev_line, current_line, next_line, line_count)
        for gear in gear_list:
          gear_dict.setdefault(gear[0], set()).add(gear[1])

      line_count += 1

    prev_line = current_line
    current_line = next_line
    next_line = None

    if current_line is not None:
      gear_list = process_line(prev_line, current_line, next_line, line_count)
      for gear in gear_list:
        gear_dict.setdefault(gear[0], set()).add(gear[1])

  gear_sum = 0
  for gear in gear_dict:
    if len(gear_dict[gear]) > 1:
      gear_sum += math.prod(gear_dict[gear])

  print(gear_sum)
