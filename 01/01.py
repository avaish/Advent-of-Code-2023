import re


def convert(word):
  match word:
    case "one":
      return "1"
    case "two":
      return "2"
    case "three":
      return "3"
    case "four":
      return "4"
    case "five":
      return "5"
    case "six":
      return "6"
    case "seven":
      return "7"
    case "eight":
      return "8"
    case "nine":
      return "9"
    case _:
      return word


if __name__ == "__main__":
  sum = 0

  with open("01/input.txt", "r") as f:
    for line in f.readlines():
      nums = re.finditer(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine|ten))',
                        line)
      nums = [num.group(1) for num in nums]
      nums = list(map(convert, nums))
      sum += int(nums[0] + nums[-1])

  print(sum)