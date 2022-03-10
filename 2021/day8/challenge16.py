import numpy as np

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

digit_boolean_of_7 = {
    0: [True, True, True, False, True, True, True],
    1: [False, False, True, False, False, True, False],
    2: [True, False, True, True, True, False, True],
    3: [True, False, True, True, False, True, True],
    4: [False, True, True, True, False, True, False],
    5: [True, True, False, True, False, True, True],
    6: [True, True, False, True, True, True, True],
    7: [True, False, True, False, False, True, False],
    8: [True, True, True, True, True, True, True],
    9: [True, True, True, True, False, True, True],
}

check_length = np.vectorize(len)


def decode_segments(segments):
    segments = np.array(segments)
    joined_segments = np.array("".join(segments))

    is_a_1 = check_length(segments) == 2
    is_a_4 = check_length(segments) == 4

    letters_of_1 = list(segments[is_a_1]).pop()
    letters_of_4 = list(segments[is_a_4]).pop()

    for letter in letters:

        count = np.char.count(joined_segments, letter)

        if count == 4:
            segment5 = letter
        elif count == 6:
            segment2 = letter
        elif count == 7:
            if letter in letters_of_4:
                segment4 = letter
            else:
                segment7 = letter
        elif count == 8:
            if letter in letters_of_1:
                segment3 = letter
            else:
                segment1 = letter
        elif count == 9:
            segment6 = letter
        else:
            pass

    return [segment1, segment2, segment3, segment4, segment5, segment6, segment7]


def letters_to_number(signal, output):
    codex = decode_segments(signal)
    result_str = ''
    for val in output:
        value_as_boolean = [c in val for c in codex]
        for digit, boolean_rep in digit_boolean_of_7.items():
            if value_as_boolean == boolean_rep:
                result_str = result_str + str(digit)
    return result_str


def main():
    decoded_output = np.array([])

    for line in open('input_data', 'r').read().split('\n'):
        signal_list = line.split(' ')[:10]
        output_list = line.split(' ')[-4:]

        signal_as_digit = letters_to_number(signal_list, output_list)
        decoded_output = np.append(decoded_output, int(signal_as_digit))

    print(np.sum(decoded_output))
    pass


if __name__ == "__main__":
    main()
