"""
Change with steps
"""


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(numbers)                      # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    numbers[1::2] = [0, 0, 0, 0, 0, 0]
    print(numbers)                      # [1, 0, 3, 0, 5, 0, 7, 0, 9, 0, 11, 0]


if __name__ == '__main__':
    main()