input_data = [line for line in open('input_data', 'r').read().split('\n')]

ok_basic_chunks = ['[]', '()', '{}', '<>']
dict_ok_pairs = {'[':'2', '(':'1', '{':'3', '<':'4'}
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


def recursive_find_first_wrong_pair(line, wrong_pairs):
    is_corrupted = contains_wrong_pairs(line, wrong_pairs)

    if is_corrupted:
        return ''
    else:
        sub_line = find_delete_ok_chunks(line, ok_basic_chunks)

        if len(sub_line) == 0:
            result = sub_line
        elif len(line) == len(sub_line):
            result = sub_line
        else:
            result = recursive_find_first_wrong_pair(sub_line, wrong_pairs)

    return result


def score_sub_line(sub_line, dict_weight):
    for key, value in dict_weight.items():
        sub_line = sub_line.replace(key, value)

    converted_sub_line = sub_line[::-1]

    score = 0

    for s in converted_sub_line:
        score = score*5 + int(s)
    return score


def main():
    valid_scores = []
    for line in input_data:
        sub_line = recursive_find_first_wrong_pair(line, wrong_basic_chunks)

        if len(sub_line) > 0:
            converted_sub_line = score_sub_line(sub_line, dict_ok_pairs)
            valid_scores.append(converted_sub_line)

    valid_scores.sort()
    middle_index = (len(valid_scores)-1)/2
    middle_score = valid_scores[int(middle_index)]
    print(middle_score)
    pass


if __name__ == "__main__":
    main()
