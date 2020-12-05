import time

def main():
    start_time = time.time()
    # Write input from .txt to array
    expenses = [int(line) for line in open("input1.txt").read().split('\n')]
    print(f"X * Y * Z = {find_triple_factor(expenses)}")
    print("--- %s seconds ---" % (time.time() - start_time))


def find_triple_factor(numbers):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if (2020 - numbers[i] - numbers[j] in numbers):
                return numbers[i] * numbers[j] * (2020 - numbers[i] - numbers[j])

if __name__ == "__main__":
    main()