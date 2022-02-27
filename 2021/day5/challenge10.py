from collections import Counter
from itertools import chain

list_tuple_str = [[[int(str_num)
                    for str_num in coord.split(',')]
                   for coord in pair_coord.split(' -> ')]
                  for pair_coord in open('input_data', 'r').read().split('\n')]

final_agg_coord = list()

for coord_pair in list_tuple_str:
    x1, y1 = coord_pair[0][0], coord_pair[0][1]
    x2, y2 = coord_pair[1][0], coord_pair[1][1]

    coord_in_line = (x1 == x2 or y1 == y2)
    coord_45deg_diagonal = (abs(x1-x2) == abs(y1-y2))

    if coord_in_line:

        x_min, y_min = min(x1, x2), min(y1, y2)
        x_max, y_max = max(x1, x2), max(y1, y2)

        if x1 == x2:
            length_of_line = abs(y2-y1) + 1
            x_base = [x1 for _ in range(length_of_line)]
            y_walk = [i for i in range(y_min, y_max + 1, 1)]

            full_line_coord = list(zip(x_base, y_walk))

        if y1 == y2:
            length_of_line = abs(x2-x1) + 1
            y_base = [y1 for _ in range(length_of_line)]
            x_walk = [i for i in range(x_min, x_max + 1, 1)]

            full_line_coord = list(zip(x_walk, y_base))

        final_agg_coord.append(full_line_coord)

    elif coord_45deg_diagonal:
        x_step = int(-(x1 - x2)/abs(x1 - x2))
        y_step = int(-(y1 - y2)/abs(y1 - y2))
        
        x_diagonal_walk = [i for i in range(x1, x2+x_step, x_step)]
        y_diagonal_walk = [i for i in range(y1, y2+y_step, y_step)]

        full_diagonal_coord = list(zip(x_diagonal_walk, y_diagonal_walk))
        final_agg_coord.append(full_diagonal_coord)


def main():
    counter = Counter(chain(*final_agg_coord))
    counter_items = counter.items()

    final_coord = [[key, value] for key, value in counter_items if value > 1]
    print("The total amount of points where lines cross vertically and horizontally is: {}".format(len(final_coord)))


if __name__ == "__main__":
    main()
