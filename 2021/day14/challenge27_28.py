from helpers import timeit
from collections import defaultdict
import math


def pair_output(freq_dict, reactions_dict, iterations):
    template_dict = defaultdict(int)

    for k, v in freq_dict.items():
        pair_to_increase_1 = reactions_dict[k][0]
        pair_to_increase_2 = reactions_dict[k][1]
        template_dict[pair_to_increase_1] += v
        template_dict[pair_to_increase_2] += v

    if iterations == 1:
        return template_dict
    else:
        return pair_output(template_dict, reactions_dict, iterations-1)


def element_count(pair_frequency):
    counter = defaultdict(float)
    for (k1, k2), v in pair_frequency.items():
        counter[k1] += v
        counter[k2] += v
    for element, v in counter.copy().items():
        counter[element] = math.ceil(counter[element]/2)

    return max(counter.values()), min(counter.values())


@timeit
def main():
    for file in open('input_data', 'r').read().split('\n\n'):
        if file.__contains__('->'):
            substitute_rules = dict([tuple(rule
                                           for rule in substitute_rule.split(' -> '))
                                     for substitute_rule in file.split('\n')])
        else:
            chain_pairs = []
            for i in range(len(file) - 1):
                chain_pairs.append(file[i] + file[i + 1])
            pass

    start_frequency_dict = defaultdict(int)
    pair_sub_dict = {k: (k[0]+v, v+k[1]) for k, v in substitute_rules.items()}

    for k in chain_pairs:
        start_frequency_dict[k] += 1

    chain_pair_10 = pair_output(start_frequency_dict, pair_sub_dict, 10)
    chain_pair_40 = pair_output(start_frequency_dict, pair_sub_dict, 40)
    max_10, min_10 = element_count(chain_pair_10)
    max_40, min_40 = element_count(chain_pair_40)

    print(f"Answer for part 1 is: {max_10 - min_10}")
    print(f"Answer for part 2 is: {max_40 - min_40}")


if __name__ == "__main__":
    main()
