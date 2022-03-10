import numpy as np

input_data = np.array([int(str_num) for str_num in open('input_data', 'r').read().split(',')])

optimal_x = np.median(input_data)
min_sum = np.min(np.sum(np.abs((input_data-optimal_x))))


def main():
    print(f"The ideal horizontal position is: {int(optimal_x)}, and the minimized sum: {int(min_sum)}")
    pass


if __name__ == "__main__":
    main()
