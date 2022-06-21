input_data = [line for line in open('input_data', 'r').read().split('\n')]
test_data = [line for line in open('test_data', 'r').read().split('\n')]

ok_basic_chunks = ['[]', '()', '{}', '<>']
wrong_basic_chunks = ['[)', '[}', '[>',
                      '(]', '(}', '(>',
                      '{]', '{)', '{>',
                      '<]', '<)', '<}']


def find_delete_ok_chunks(some_string, to_delete_list):
    result_string = some_string

    for s in to_delete_list:
        result_string = result_string.replace(s, '-')

    return result_string.replace('-', '')


def contains_wrong_pairs(line, wrong_pairs):
    count_wrong_chunks = 0

    for wrong_chunk in wrong_pairs:
        count_wrong_chunks += line.count(wrong_chunk)

    return count_wrong_chunks > 0


def first_wrong_pair(line, wrong_pairs):
    list_of_positions = []

    for wrong_chunk in wrong_pairs:
        list_of_positions.append(line.find(wrong_chunk))

    list_valid_positions = [i for i in list_of_positions if i >= 0]

    return min(list_valid_positions)


def recursive_find_first_wrong_pair(line, wrong_pairs):
    is_corrupted = contains_wrong_pairs(line, wrong_pairs)

    if is_corrupted:
        pos_wrong = first_wrong_pair(line, wrong_pairs)
        # ToDo get the expected closing part of the found opening
        result = line[pos_wrong + 1]
    else:
        sub_line = find_delete_ok_chunks(line, ok_basic_chunks)

        if len(sub_line) == 0:
            result = 'complete_line'
        elif len(line) == len(sub_line):
            result = 'correct_incomplete_line'
        else:
            result = recursive_find_first_wrong_pair(sub_line, wrong_pairs)

    return result


def main():
    result_string = ''
    for line in input_data:
        result_string += recursive_find_first_wrong_pair(line, wrong_basic_chunks)
    answer = result_string.count(')') * 3\
             + result_string.count(']') * 57\
             + result_string.count('}') * 1197\
             + result_string.count('>') * 25137
    # print(result_string)
    print(answer)


if __name__ == "__main__":
    main()