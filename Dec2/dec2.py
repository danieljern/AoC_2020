import time
import re

def main():
    start_time = time.time()
    valid_passwords_part1 = password_check_part1("input.txt")
    valid_passwords_part2 = password_check_part2("input.txt")
    print(f"Part1: Number of valid passwords in input = {valid_passwords_part1}")
    print(f"Part2: Number of valid passwords in input = {valid_passwords_part2}")
    print("--- %s seconds ---" % (time.time() - start_time))

def password_check_part1(txtfile):
    counter = 0
    for line in open(txtfile).read().split('\n'):
        min, max = [int(digit) for digit in re.findall(r'[0-9]?\d', line)]
        key = re.search(r"([a-zA-Z]*?):", line).group().split(':')[0]
        password = re.split(r'[\s]', line)[2]
        if (password.count(key) >= min and password.count(key) <= max):
            counter = counter + 1
    return counter

def password_check_part2(txtfile):
    counter = 0
    for line in open(txtfile).read().split('\n'):
        index1, index2 = [int(digit) for digit in re.findall(r'[0-9]?\d', line)]
        key = re.search(r"([a-zA-Z]*?):", line).group().split(':')[0]
        password = re.split(r'[\s]', line)[2]
        if (password[index1-1] == key or password[index2-1] == key) and (password[index1-1] != password[index2-1]):
            counter = counter + 1
    return counter


if __name__ == "__main__":
    main()