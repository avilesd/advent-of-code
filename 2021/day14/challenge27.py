from collections import Counter
from helpers import timeit

start_chain = []

for file in open('input_data', 'r').read().split('\n\n'):
    if file.__contains__('->'):
        substitute_rules = dict([tuple(rule
                                       for rule in substitute_rule.split(' -> '))
                                 for substitute_rule in file.split('\n')])
    else:
        start_chain = file
        pass


def new_chain(old_chain, rules, iterations):
    old_list = []
    result_list = []

    for i in range(len(old_chain) - 1):
        old_list.append(old_chain[i] + old_chain[i + 1])

    for i in range(len(old_list)):
        for k, v in rules.items():
            if old_list[i] == k:
                if i == len(old_list)-1:
                    result_list.append(old_list[i][0]+v+old_list[i][1])
                else:
                    result_list.append(old_list[i][0]+v)
    frequencies = Counter("".join(result_list))
    print(frequencies)
    if iterations == 1:
        return "".join(result_list)
    else:
        return new_chain("".join(result_list), rules, iterations-1)


@timeit
def main():
    final_chain = "".join(new_chain(start_chain, substitute_rules, 10))

    frequencies_val = Counter(final_chain).values()
    print(f"The answer is: {max(frequencies_val)-min(frequencies_val)}")


if __name__ == "__main__":
    main()
