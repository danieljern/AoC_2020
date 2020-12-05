import time

def main():
    start_time = time.time()
    # Write input from .txt to the list expenses
    expenses = [int(line) for line in open("input1.txt").read().split('\n')]
    print(f"X * Y = {find_combo_factor(expenses)}")
    print("--- %s seconds ---" % (time.time() - start_time))


def find_combo_factor(numbers):
    for i in range(len(numbers)):
        if (2020 - numbers[i] in numbers):
            return numbers[i] * (2020 - numbers[i])


if __name__ == "__main__":
    main()
