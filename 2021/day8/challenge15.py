from itertools import chain


def main():
    four_patterns = []

    for line in open('input_data', 'r').read().split('\n'):
        output = line.split(' ')[-4:]
        four_patterns.append(output)

    patterns = list(chain(*four_patterns))
    count = 0

    for pattern in patterns:
        if len(pattern) in [2, 4, 3, 7]:
            count += 1

    print(count)
    pass


if __name__ == "__main__":
    main()
