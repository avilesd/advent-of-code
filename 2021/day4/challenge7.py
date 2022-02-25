import pandas as pd
import numpy as np

df_random_nums = pd.read_csv("input_data_firstRow", nrows=1, header=None).values[0]

matrix_list = [[[int(num_str)
                 for num_str in line.split()]
                for line in one_matrix.split('\n')]
               for one_matrix in open('input_data', 'r').read().split('\n\n')]


for i in range(0, len(matrix_list)):
    matrix_list[i] = np.array(matrix_list[i])


def is_board_bingo(bingo_matrix, bingo_numbers):
    row_bingo = False
    col_bingo = False
    
    row_matrix = bingo_matrix
    col_matrix = bingo_matrix.T

    for i in range(bingo_matrix.shape[0]):
        row_bool = np.isin(row_matrix[i], bingo_numbers)
        row_bingo = row_bool.all()

        col_bool = np.isin(col_matrix[i], bingo_numbers)
        col_bingo = col_bool.all()

        if row_bingo or col_bingo:
            return True

    return row_bingo or col_bingo


def main():
    bingo_list = list()
    stop_bingo = False

    for num in df_random_nums:
        if stop_bingo:
            break

        bingo_list.append(num)

        for mat in matrix_list:
            bingo_reached = is_board_bingo(mat, bingo_list)
            if bingo_reached:
                last_pulled_num = bingo_list[-1]

                non_picked_nums_bool = np.isin(mat, bingo_list, invert=True)
                non_picked_nums = mat[non_picked_nums_bool]
                non_picked_nums_sum = sum(non_picked_nums)

                stop_bingo = True
                break

    print("The last pulled bingo number was: {}".format(last_pulled_num))
    print("The sum of the non-picked numbers of the winning bingo board is: {}".format(non_picked_nums_sum))
    print("Both last numbers multiplied result in: {}".format(non_picked_nums_sum*last_pulled_num))


if __name__ == '__main__':
    main()
