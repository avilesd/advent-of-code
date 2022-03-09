import numpy as np

input_array = [int(str_num) for str_num in open('input_data', 'r').read().split(',')]


def lanternfish_state(previous_state, days):
    """
    Iteratively determines the new population of a previous state after a number of 'days' (iterations)

    Lazy solution to the AoC 2021.6.1 challenge
    :return: list of integers representing the final state of the lanternfish
    """
    helper_state = list(np.array(previous_state)-1)
    new_state = list()

    for i in helper_state:
        if i == -1:
            new_state.append(6)
            new_state.append(8)
        else:
            new_state.append(i)

    if days == 1:
        result = new_state
    else:
        result = lanternfish_state(new_state, days-1)

    return result


def main():
    print(len(lanternfish_state(input_array, 80)))


if __name__ == "__main__":
    main()
