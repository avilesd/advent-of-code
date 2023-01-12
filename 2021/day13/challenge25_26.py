import pandas as pd
import numpy as np

for file in open('input_data', 'r').read().split('\n\n'):
    if file[0].isdigit():
        coordinates = set(tuple(int(coord)
                                for coord in pair_coord.split(','))
                          for pair_coord in file.split('\n'))
    else:
        instructions = [tuple(instruction
                              for instruction in fold_text.split('along ')[1:][0].split('='))
                        for fold_text in file.split('\n')]


def main():
    just_first = 0

    for instruction in instructions:
        if instruction[0] == 'y':
            y_fold = int(instruction[1])
            for dots in coordinates.copy():
                y_orig = dots[1]
                if y_orig > y_fold:
                    new_dot = (dots[0], abs(y_orig - 2*y_fold))
                    coordinates.remove(dots)
                    coordinates.add(new_dot)
            if just_first == 0:
                length_after_first_fold = coordinates.__len__()
            just_first += 1
        else:
            x_fold = int(instruction[1])
            for dots in coordinates.copy():
                x_orig = dots[0]
                if x_orig > x_fold:
                    new_dot = (abs(x_orig - 2*x_fold), dots[1])
                    coordinates.remove(dots)
                    coordinates.add(new_dot)
            if just_first == 0:
                length_after_first_fold = coordinates.__len__()
            just_first += 1

    print(coordinates)
    print(f'The amount of dots after one fold is: {length_after_first_fold}')
    print(f'The amount of dots after {instructions.__len__()} folds is: {coordinates.__len__()}')

    # Part 2
    max_x_coordinate = max([coord[0] for coord in coordinates])
    max_y_coordinate = max([coord[1] for coord in coordinates])
    print(max_x_coordinate)
    print(max_y_coordinate)

    df = pd.DataFrame(pd.DataFrame(np.zeros((max_x_coordinate+2, max_y_coordinate+2)).astype(int)))
    df.replace(0, '.', inplace=True)

    for coord in coordinates:
        df.iloc[coord[0], coord[1]] = '#'

    print(df.T.iloc[:, 0:14])
    print(df.T.iloc[:, 14:30])
    print(df.T.iloc[:, 30:])


if __name__ == "__main__":
    main()
