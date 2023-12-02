import re

if __name__ == "__main__":
  power_sum = 0
  
  with open("input.txt", "r") as f:
    for line in f.readlines():
      game, pulls = line.split(':')
      game = int(re.search("[0-9]+", game).group(0))
      min_red = 0
      min_green = 0
      min_blue = 0
      for pull in pulls.split(';'):
        for pull_split in pull.split(','):
          color = re.search("blue|green|red", pull_split).group(0)
          count = int(re.search("[0-9]+", pull_split).group(0))

          if color == "red" and count > min_red:
            min_red = count
          if color == "green" and count > min_green:
            min_green = count
          if color == "blue" and count > min_blue:
            min_blue = count

      power_sum += min_red * min_green * min_blue

  print(power_sum)